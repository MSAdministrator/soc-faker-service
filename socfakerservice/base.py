import pendulum
from flask import url_for, render_template, session, redirect, flash
from socfakerservice import app


def __return_sorted_navbar_dict(value):
    return_dict = {}
    for key,val in dict(sorted(value.items())).items():
        return_dict[key] = sorted(val, key = lambda i: i['name'])
    return return_dict

def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)

@app.context_processor
def site_map():
    route_dict = {}
    for rule in app.url_map.iter_rules():
        # Filter out rules we can't navigate to in a browser
        # and rules that require parameters
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            if url.startswith('/products/elastic/document/'):
                if 'Elastic' not in route_dict:
                    route_dict['Elastic'] = []
                route_dict['Elastic'].append({
                    'name': url.replace('/products/elastic/document/fields/', '').replace('/',' ').replace('_',' ').title(),
                    'path': url
                })
            elif url.startswith('/products/elastic'):
                if 'Elastic' not in route_dict:
                    route_dict['Elastic'] = []
                route_dict['Elastic'].append({
                    'name': url.replace('/products/elastic', '').replace('/',' ').replace('_',' ').title(),
                    'path': url
                })
            elif url.startswith('/products/azure/vm/details'):
                if 'Azure' not in route_dict:
                    route_dict['Azure'] = []
                route_dict['Azure'].append({
                    'name': url.replace('/products/azure/', '').replace('/',' ').replace('_',' ').title(),
                    'path': url
                })
            elif url.startswith('/products/azure/vm/metrics'):
                if 'Azure' not in route_dict:
                    route_dict['Azure'] = []
                route_dict['Azure'].append({
                    'name': url.replace('/products/azure/', '').replace('/',' ').replace('_',' ').title(),
                    'path': url
                })
            elif url.startswith('/products/azure/vm/topology'):
                if 'Azure' not in route_dict:
                    route_dict['Azure'] = []
                route_dict['Azure'].append({
                    'name': url.replace('/products/azure/', '').replace('/',' ').replace('_',' ').title(),
                    'path': url
                })
            elif url.startswith('/products/azure/details'):
                if 'Azure' not in route_dict:
                    route_dict['Azure'] = []
                route_dict['Azure'].append({
                    'name': 'Details',
                    'path': url
                })
            elif url.startswith('/vulnerability'):
                if 'Vulnerability' not in route_dict:
                    route_dict['Vulnerability'] = []
                route_dict['Vulnerability'].append({
                    'name': url.replace('/vulnerability/', '').replace('/',' ').replace('_',' ').title(),
                    'path': url
                })
            else:
                ignore = False
                for item in ['/api/', '/products/','/thanks', '/index','/token']:
                    if url.startswith(item):
                        ignore = True
                if not ignore:          
                    key = url.lstrip('/').split('/')[0].replace('_',' ').capitalize()
                    if key not in route_dict:
                        route_dict[key] = []
                    route_dict[key].append({
                        'path': url,
                        'name': url.split('/')[-1].capitalize()
                    })
    route_dict = __return_sorted_navbar_dict(route_dict)
    return dict(route_dict=route_dict)

from .model import TokenModel
from .token import Token
from .tokenmanager import TokenManager

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/token', methods=['GET', 'POST'])
def token():
    form = Token()
    if form.validate_on_submit():
        if form.email.data:
            existing_registration = TokenModel.objects(email=form.email.data).first()
            if existing_registration:
                token_manager = TokenManager(form.email.data)
                TokenModel.objects(email=form.email.data).update(**{
                    'token': token_manager.token,
                    'last_request_date': pendulum.now().to_iso8601_string()
                })
                token_manager.send_email()
                session['email'] = token_manager.email
                return redirect(url_for('thanks'))
            else:
                token_manager = TokenManager(form.email.data)
                registration = TokenModel(email=token_manager.email, token=token_manager.token)
                registration.save()
                token_manager.send_email()
                session['email'] = token_manager.email
                return redirect(url_for('thanks'))
        else:
            flash('A valid email address is required')
            return redirect(url_for('index'))
    return render_template('token.html', form=form)

@app.route('/thanks', methods=['GET'])
def thanks():
    return render_template('thanks.html', email=session['email'])
