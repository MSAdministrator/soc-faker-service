from flask import Blueprint, render_template, request, abort, jsonify, Response
from socfakerservice import status, HTMLRenderer, set_renderers
from socfakerservice.model import TokenModel
from socfaker import SocFaker

socfaker = SocFaker()

api_bp = Blueprint(
    'api',
    __name__
)


def validate_request(request):
    auth_header = request.headers.get('soc-faker')
    if auth_header:
        existing_registration = TokenModel.objects(token=auth_header).first()
        if existing_registration:
            return True
    abort(401)

@api_bp.errorhandler(401)
def unauthorized(error):
    return Response('Unauthorized to access this resource', 401, {'Content-Type': 'application/json'})

@api_bp.route("/agent", methods=['GET'])
def socfaker_socfaker_agent():
    """
    Access generated data related to an endpoint agent

        Returns:
            Agent: Returns an object with properties related to an endpoint agent
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.agent))

@api_bp.route("/agent/ephermeral_id", methods=['GET'])
def socfaker_agent_ephermeral_id():
    """
    A unique and random ephermal ID that changes

        Returns:
            str: A unique 8 character length hex ID
        
    """
    if validate_request(request):
        return { 'value': socfaker.agent.ephermeral_id }

@api_bp.route("/agent/id", methods=['GET'])
def socfaker_agent_id():
    """
    A agent ID which is typically static across the lifetime of the 
           agent (per instance of this class)

        Returns:
            str: A static but unique 8 character length ID representing the agent ID
        
    """
    if validate_request(request):
        return { 'value': socfaker.agent.id }

@api_bp.route("/agent/name", methods=['GET'])
def socfaker_agent_name():
    """
    A custom name of the agent

        Returns:
            str: A custom name of the agent
        
    """
    if validate_request(request):
        return { 'value': socfaker.agent.name }

@api_bp.route("/agent/type", methods=['GET'])
def socfaker_agent_type():
    """
    The type of agent.

        Options are: 'filebeat', 'auditbeat', 'functionbeat', 
                     'heartbeat', 'winlogbeat', 'packetbeat'

        Returns:
            str: A agent type
        
    """
    if validate_request(request):
        return { 'value': socfaker.agent.type }

@api_bp.route("/agent/version", methods=['GET'])
def socfaker_agent_version():
    """
    The agent version

        Returns:
            str: Currently set to a static value of 7.8.0
        
    """
    if validate_request(request):
        return { 'value': socfaker.agent.version }

### AGENT ROUTES ###
### ALERT ROUTES ###

@api_bp.route("/alert", methods=['GET'])
def socfaker_socfaker_alert():
    """
    Alert or Detection properties

        Returns:
            Alert: Returns an object with properties about a alert or detection
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.alert))

@api_bp.route("/alert/action", methods=['GET'])
def socfaker_alert_action():
    """
    An action taken based on the alert

        Returns:
            str: Returns a random action based on the alert
        
    """
    if validate_request(request):
        return { 'value': socfaker.alert.action }

@api_bp.route("/alert/direction", methods=['GET'])
def socfaker_alert_direction():
    """
    The direction of the alert (network based)

        Returns:
            str: Random direction of from or to
        
    """
    if validate_request(request):
        return { 'value': socfaker.alert.direction }

@api_bp.route("/alert/location", methods=['GET'])
def socfaker_alert_location():
    """
    The country the alert originated from

        Returns:
            str: A random country an alert was generated from
        
    """
    if validate_request(request):
        return { 'value': socfaker.alert.location }

@api_bp.route("/alert/signature_name", methods=['GET'])
def socfaker_alert_signature_name():
    """
    Returns the name of a signature that the Alert triggered upon

        Returns:
            Str: returns a random alert signature name
        
    """
    if validate_request(request):
        return { 'value': socfaker.alert.signature_name }

@api_bp.route("/alert/status", methods=['GET'])
def socfaker_alert_status():
    """
    The current alert status

        Returns:
            str: Returns whether the alert was successful 
                 or unsuccessful
        
    """
    if validate_request(request):
        return { 'value': socfaker.alert.status }

@api_bp.route("/alert/summary", methods=['GET'])
def socfaker_alert_summary():
    """
    Returns the summary of an alert

        Returns:
            str: Returns a string of this instance of an alert.  
                 Contains a status, action, type, direction, and location.
        
    """
    if validate_request(request):
        return { 'value': socfaker.alert.summary }

@api_bp.route("/alert/type", methods=['GET'])
def socfaker_alert_type():
    """
    Returns an alert type

        Returns:
            str: Returns a random alert type
        
    """
    if validate_request(request):
        return { 'value': socfaker.alert.type }

### ALERT ROUTES ###
### APPLICATION ROUTES ###

@api_bp.route("/application", methods=['GET'])
def socfaker_socfaker_application():
    """
    Generated data related to a application

        Returns:
            Application: Returns an object with properties about an application
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.application))

@api_bp.route("/application/account_status", methods=['GET'])
def socfaker_application_account_status():
    """
    A random account status for the application

        Returns:
            str: Returns whether an account is enabled or 
                 disabled for an application
        
    """
    if validate_request(request):
        return { 'value': socfaker.application.account_status }

@api_bp.route("/application/logon_timestamp", methods=['GET'])
def socfaker_application_logon_timestamp():
    """
    Logon timestamp of a user/service for an applicaiton

        Returns:
            str: Returns an ISO 8601 timestamp in the past
        
    """
    if validate_request(request):
        return { 'value': socfaker.application.logon_timestamp }

@api_bp.route("/application/name", methods=['GET'])
def socfaker_application_name():
    """
    The name of an application

        Returns:
            str: Returns a random application name based on common 
                 applications used in enterprises
        
    """
    if validate_request(request):
        return { 'value': socfaker.application.name }

@api_bp.route("/application/status", methods=['GET'])
def socfaker_application_status():
    """
    Returns the application status

        Returns:
            str: Returns the application status of 
                 Active, Inactive, or Legacy
        
    """
    if validate_request(request):
        return { 'value': socfaker.application.status }

### APPLICATION ROUTES ###
### CLOUD ROUTES ###

@api_bp.route("/cloud", methods=['GET'])
def socfaker_socfaker_cloud():
    """
    Generated data related to cloud infrastructure

        Returns:
            Cloud: Returns an object with properties about cloud infrastructure
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.cloud))

@api_bp.route("/cloud/id", methods=['GET'])
def socfaker_cloud_id():
    """
    A cloud instance ID

        Returns:
            str: A random GUID for a cloud instance ID
        
    """
    if validate_request(request):
        return { 'value': socfaker.cloud.id }

@api_bp.route("/cloud/instance_id", methods=['GET'])
def socfaker_cloud_instance_id():
    """
    A random hex instance ID

        Returns:
            str: A random HEX character instance ID
        
    """
    if validate_request(request):
        return { 'value': socfaker.cloud.instance_id }

@api_bp.route("/cloud/name", methods=['GET'])
def socfaker_cloud_name():
    """
    The name of a cloud VM/container instance

        Returns:
            str: A random generated name of a cloud VM or container instance
        
    """
    if validate_request(request):
        return { 'value': socfaker.cloud.name }

@api_bp.route("/cloud/provider", methods=['GET'])
def socfaker_cloud_provider():
    """
    The cloud provider

        Returns:
            str: A random cloud provider of either aws, azure, gcp, or digitalocean
        
    """
    if validate_request(request):
        return { 'value': socfaker.cloud.provider }

@api_bp.route("/cloud/region", methods=['GET'])
def socfaker_cloud_region():
    """
    The region of a cloud instance

        Returns:
            str: The region of a cloud instance
        
    """
    if validate_request(request):
        return { 'value': socfaker.cloud.region }

@api_bp.route("/cloud/size", methods=['GET'])
def socfaker_cloud_size():
    """
    The size of a instance (based on AWS naming convention)

        Returns:
            str: A random size of an instance based on AWS naming convention
        
    """
    if validate_request(request):
        return { 'value': socfaker.cloud.size }

@api_bp.route("/cloud/zone", methods=['GET'])
def socfaker_cloud_zone():
    """
    A random generated availability zone in common cloud platforms like AWS & Azure

        Returns:
            str: A string representing a cloud availability zone
        
    """
    if validate_request(request):
        return { 'value': socfaker.cloud.zone }

### CLOUD ROUTES ###
### COMPUTER ROUTES ###

@api_bp.route("/computer", methods=['GET'])
def socfaker_socfaker_computer():
    """
    Generated data about a computer system

        Returns:
            Computer: Returns an object with properties about a computer system
        
    """
    if validate_request(request):
        return {'value': socfaker.computer}

@api_bp.route("/computer/architecture", methods=['GET'])
def socfaker_computer_architecture():
    """
    Architecture of a computer instance

        Returns:
            str: Architecture of computer system of either x86_64 or x86
        
    """
    if validate_request(request):
        return { 'value': socfaker.computer.architecture }

@api_bp.route("/computer/disk", methods=['GET'])
def socfaker_computer_disk():
    """
    The disk size of a computer instance

        Returns:
            list: Returns a list of B,KB,MB,GB, and TB size of a computers disk
        
    """
    if validate_request(request):
        return { 'value': socfaker.computer.disk }

@api_bp.route("/computer/ipv4", methods=['GET'])
def socfaker_computer_ipv4():
    """
    The operating system ipv4 address

        Returns:
            str: A random operating system ipv4 address
        
    """
    if validate_request(request):
        return { 'value': socfaker.computer.ipv4 }

@api_bp.route("/computer/mac_address", methods=['GET'])
def socfaker_computer_mac_address():
    """
    A generated MAC address for a computer instance

        Returns:
            str: A random MAC Address
        
    """
    if validate_request(request):
        return { 'value': socfaker.computer.mac_address }

@api_bp.route("/computer/memory", methods=['GET'])
def socfaker_computer_memory():
    """
    The memory size of a computer instance

        Returns:
            list: Returns a list of B,KB,MB,GB, and TB size of a computers memory size
        
    """
    if validate_request(request):
        return { 'value': socfaker.computer.memory }

@api_bp.route("/computer/name", methods=['GET'])
def socfaker_computer_name():
    """
    The name of a comptuer

        Returns:
            str: A random name of a computer 
        
    """
    if validate_request(request):
        return { 'value': socfaker.computer.name }

@api_bp.route("/computer/os", methods=['GET'])
def socfaker_computer_os():
    """
    The operating system full name of the computer instance

        Returns:
            str: A random operating system version
        
    """
    if validate_request(request):
        return { 'value': socfaker.computer.os }

@api_bp.route("/computer/platform", methods=['GET'])
def socfaker_computer_platform():
    """
    A random name of the computers platform

        Returns:
            str: Random name of a computers platform (e.g. worksation, server, etc.)
        
    """
    if validate_request(request):
        return { 'value': socfaker.computer.platform }

### COMPUTER ROUTES ###
### CONTAINER ROUTES ###

@api_bp.route("/container", methods=['GET'])
def socfaker_socfaker_container():
    """
    Generated data about a container

        Returns:
            Container: Returns an object with properties about a container
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.container))

@api_bp.route("/container/id", methods=['GET'])
def socfaker_container_id():
    """
    A container ID

        Returns:
            str: A hex container ID
        
    """
    if validate_request(request):
        return { 'value': socfaker.container.id }

@api_bp.route("/container/name", methods=['GET'])
def socfaker_container_name():
    """
    A random generated container name

        Returns:
            str: A randomly generated container name
        
    """
    if validate_request(request):
        return { 'value': socfaker.container.name }

@api_bp.route("/container/runtime", methods=['GET'])
def socfaker_container_runtime():
    """
    A container runtime

        Returns:
            str: Returns either docker or kubernetes
        
    """
    if validate_request(request):
        return { 'value': socfaker.container.runtime }

@api_bp.route("/container/tags", methods=['GET'])
def socfaker_container_tags():
    """
    Container tags

        Returns:
            list: A random list of container tags
        
    """
    if validate_request(request):
        return { 'value': socfaker.container.tags }

### CONTAINER ROUTES ###
### DNS ROUTES ###

@api_bp.route("/dns", methods=['GET'])
def socfaker_socfaker_dns():
    """
    DNS Information

        Returns:
            DNS: Returns an object with properties about DNS request, response, etc.
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.dns))

@api_bp.route("/dns/answers", methods=['GET'])
def socfaker_dns_answers():
    """
    A list of DNS answers during a DNS request

        Returns:
            list: A random list (count) of random DNS answers during a DNS request
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.dns.answers))

@api_bp.route("/dns/direction", methods=['GET'])
def socfaker_dns_direction():
    """
    The direction of a DNS request

        Returns:
            str: Returns a direction for a DNS request or response
        
    """
    if validate_request(request):
        return { 'value': socfaker.dns.direction }

@api_bp.route("/dns/header_flags", methods=['GET'])
def socfaker_dns_header_flags():
    """
    DNS Header flags

        Returns:
            str: A randomly selected DNS Header Flag
        
    """
    if validate_request(request):
        return { 'value': socfaker.dns.header_flags }

@api_bp.route("/dns/id", methods=['GET'])
def socfaker_dns_id():
    """
    A random DNS ID value from 10000,100000

        Returns:
            int: A random DNS ID value
        
    """
    if validate_request(request):
        return { 'value': socfaker.dns.id }

@api_bp.route("/dns/name", methods=['GET'])
def socfaker_dns_name():
    """
    Returns a randomly generated DNS name

        Returns:
            str: A random DNS Name
        
    """
    if validate_request(request):
        return { 'value': socfaker.dns.name }

@api_bp.route("/dns/op_code", methods=['GET'])
def socfaker_dns_op_code():
    """
    A DNS OP COde

        Returns:
            str: A random DNS OP Code for a DNS request
        
    """
    if validate_request(request):
        return { 'value': socfaker.dns.op_code }

@api_bp.route("/dns/question", methods=['GET'])
def socfaker_dns_question():
    """
    A DNS question during a DNS request

        Returns:
            dict: A random DNS question during a DNS request
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.dns.question))

@api_bp.route("/dns/record", methods=['GET'])
def socfaker_dns_record():
    """
    A randomly selected record type

        Returns:
            str: A random DNS record (e.g. A, CNAME, PTR, etc.)
        
    """
    if validate_request(request):
        return { 'value': socfaker.dns.record }

@api_bp.route("/dns/response_code", methods=['GET'])
def socfaker_dns_response_code():
    """
    A DNS Response Code

        Returns:
            str: A DNS response code as part of a response made during a DNS request
        
    """
    if validate_request(request):
        return { 'value': socfaker.dns.response_code }


### DNS ROUTES ###
### EMPLOYEE ROUTES ###

@api_bp.route("/employee", methods=['GET'])
def socfaker_socfaker_employee():
    """
    An employee object

        Returns:
            Employee: Returns an object with properties about a fake employee
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.employee))

@api_bp.route("/employee/account_status", methods=['GET'])
def socfaker_employee_account_status():
    """
    Account status of an employee

        Returns:
            str: Returns an employee's account status.  This is weighted towards enabled.
        
    """
    if validate_request(request):
        return { 'value': socfaker.employee.account_status }

@api_bp.route("/employee/department", methods=['GET'])
def socfaker_employee_department():
    """
    Employee department

        Returns:
            str: Returns a random employee department
        
    """
    if validate_request(request):
        return { 'value': socfaker.employee.department }

@api_bp.route("/employee/dob", methods=['GET'])
def socfaker_employee_dob():
    """
    Date of Birth of an employee

        Returns:
            str: Returns the date of birth (DOB) of an employee
        
    """
    if validate_request(request):
        return { 'value': socfaker.employee.dob }

@api_bp.route("/employee/email", methods=['GET'])
def socfaker_employee_email():
    """
    Email of an employee

        Returns:
            str: Returns the email address of an employee
        
    """
    if validate_request(request):
        return { 'value': socfaker.employee.email }

@api_bp.route("/employee/first_name", methods=['GET'])
def socfaker_employee_first_name():
    """
    First name of an employee

        Returns:
            str: Returns the first name of an employee
        
    """
    if validate_request(request):
        return { 'value': socfaker.employee.first_name }

@api_bp.route("/employee/gender", methods=['GET'])
def socfaker_employee_gender():
    """
    Gender of an employee

        Returns:
            str: Returns the gender of an employee
        
    """
    if validate_request(request):
        return { 'value': socfaker.employee.gender }

@api_bp.route("/employee/language", methods=['GET'])
def socfaker_employee_language():
    """
    The preferred employee language

        Returns:
            str: Returns a random language of an employee
        
    """
    if validate_request(request):
        return { 'value': socfaker.employee.language }

@api_bp.route("/employee/last_name", methods=['GET'])
def socfaker_employee_last_name():
    """
    Last name of an employee

        Returns:
            str: Returns the last name of an employee
        
    """
    if validate_request(request):
        return { 'value': socfaker.employee.last_name }

@api_bp.route("/employee/logon_timestamp", methods=['GET'])
def socfaker_employee_logon_timestamp():
    """
    Last logon timestamp of an employee

        Returns:
            str: Returns a random ISO 8601 timestamp of an employee in the past
        
    """
    if validate_request(request):
        return { 'value': socfaker.employee.logon_timestamp }

@api_bp.route("/employee/name", methods=['GET'])
def socfaker_employee_name():
    """
    Returns First and Last name of an employee

        Returns:
            str: Returns a random First and Last name of an employee
        
    """
    if validate_request(request):
        return { 'value': socfaker.employee.name }

@api_bp.route("/employee/phone_number", methods=['GET'])
def socfaker_employee_phone_number():
    """
    Phone number of an employee

        Returns:
            str: Returns a random phone number of an employee
        
    """
    if validate_request(request):
        return { 'value': socfaker.employee.phone_number }

@set_renderers(HTMLRenderer)
@api_bp.route("/employee/photo", methods=['GET'])
def socfaker_employee_photo():
    """
    Photo URL of an employee

        Returns:
            str: Returns a URL of a random photo for the employee
        
    """
    if validate_request(request):
        return f'<html><body><h1><img src="{socfaker.employee.photo}</h1></body></html>'

@api_bp.route("/employee/ssn", methods=['GET'])
def socfaker_employee_ssn():
    """
    SSN of an employee

        Returns:
            str: Returns the SSN of an employee
        
    """
    if validate_request(request):
        return { 'value': socfaker.employee.ssn }

@api_bp.route("/employee/title", methods=['GET'])
def socfaker_employee_title():
    """
    Employee title

        Returns:
            str: Returns a random employee title
        
    """
    if validate_request(request):
        return { 'value': socfaker.employee.title }

@api_bp.route("/employee/user_id", methods=['GET'])
def socfaker_employee_user_id():
    """
    User ID of an employee

        Returns:
            str: Returns a random user ID of an employee
        
    """
    if validate_request(request):
        return { 'value': socfaker.employee.user_id }

@api_bp.route("/employee/username", methods=['GET'])
def socfaker_employee_username():
    """
    Username of an employee

        Returns:
            str: Returns the username of an employee
        
    """
    if validate_request(request):
        return { 'value': socfaker.employee.username }

### EMPLOYEE ROUTES ###
### FILE ROUTES ###

@api_bp.route("/file", methods=['GET'])
def socfaker_socfaker_file():
    """
    A file object

        Returns:
            File: Returns an object with properties about a fake file object
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.file))

@api_bp.route("/file/accessed_timestamp", methods=['GET'])
def socfaker_file_accessed_timestamp():
    """
    The last accessed timestamp of a file in the past

        Returns:
            str: A randomly generated accessed timestamp is ISO 8601 format
        
    """
    if validate_request(request):
        return { 'value': socfaker.file.accessed_timestamp }

@api_bp.route("/file/attributes", methods=['GET'])
def socfaker_file_attributes():
    """
    Attributes of the file 

        Returns:
            list: A randomly selected list of file attributes
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.file.attributes))

@api_bp.route("/file/build_version", methods=['GET'])
def socfaker_file_build_version():
    """
    A build version of a file

        Returns:
            str: Returns the last digit in the version string
        
    """
    if validate_request(request):
        return { 'value': socfaker.file.build_version }

@api_bp.route("/file/checksum", methods=['GET'])
def socfaker_file_checksum():
    """
    A MD5 checksum of a file

        Returns:
            str: Returns a MD5 of the file
        
    """
    if validate_request(request):
        return { 'value': socfaker.file.checksum }

@api_bp.route("/file/directory", methods=['GET'])
def socfaker_file_directory():
    """
    The directory of a file

        Returns:
            str: The directory of a file
        
    """
    if validate_request(request):
        return { 'value': socfaker.file.directory }

@api_bp.route("/file/drive_letter", methods=['GET'])
def socfaker_file_drive_letter():
    """
    The drive letter of a file

        Returns:
            str: A randomly selected drive letter of a file
        
    """
    if validate_request(request):
        return { 'value': socfaker.file.drive_letter }

@api_bp.route("/file/extension", methods=['GET'])
def socfaker_file_extension():
    """
    The extension of a file

        Returns:
            str: The extension of a file
        
    """
    if validate_request(request):
        return { 'value': socfaker.file.extension }

@api_bp.route("/file/full_path", methods=['GET'])
def socfaker_file_full_path():
    """
    The full path of a file

        Returns:
            str: A randomly selected file name path
        
    """
    if validate_request(request):
        return { 'value': socfaker.file.full_path }

@api_bp.route("/file/gid", methods=['GET'])
def socfaker_file_gid():
    """
    The GID of a file

        Returns:
            str: A randomly generated GID of a file
        
    """
    if validate_request(request):
        return { 'value': socfaker.file.gid }

@api_bp.route("/file/hashes", methods=['GET'])
def socfaker_file_hashes():
    """
    A dict containing MD5, SHA1, and SHA256 hashes

        Returns:
            str: A randomly generated dict containing MD5, SHA1, and SHA256 hashes
        
    """
    if validate_request(request):
        return { 'value': socfaker.file.hashes }

@api_bp.route("/file/install_scope", methods=['GET'])
def socfaker_file_install_scope():
    """
    The install scope of a file

        Returns:
            str: Returns a random install scope of user-local or global for a file
        
    """
    if validate_request(request):
        return { 'value': socfaker.file.install_scope }

@api_bp.route("/file/md5", methods=['GET'])
def socfaker_file_md5():
    """
    A random generated MD5 hash

        Returns:
            str: A randomly generated MD5 file hash
        
    """
    if validate_request(request):
        return { 'value': socfaker.file.md5 }

@api_bp.route("/file/mime_type", methods=['GET'])
def socfaker_file_mime_type():
    """
    The mime type of a file

        Returns:
            str: A randomly selected file mime type
        
    """
    if validate_request(request):
        return { 'value': socfaker.file.mime_type }

@api_bp.route("/file/name", methods=['GET'])
def socfaker_file_name():
    """
    The name of a file

        Returns:
            str: A randomly selected file name
        
    """
    if validate_request(request):
        return { 'value': socfaker.file.name }

@api_bp.route("/file/sha1", methods=['GET'])
def socfaker_file_sha1():
    """
    A random generated SHA1 hash

        Returns:
            str: A randomly generated SHA1 file hash
        
    """
    if validate_request(request):
        return { 'value': socfaker.file.sha1 }

@api_bp.route("/file/sha256", methods=['GET'])
def socfaker_file_sha256():
    """
    A random generated SHA256 hash

        Returns:
            str: A randomly generated SHA256 file hash
        
    """
    if validate_request(request):
        return { 'value': socfaker.file.sha256 }

@api_bp.route("/file/signature", methods=['GET'])
def socfaker_file_signature():
    """
    The file signature

        Returns:
            str: Returns the signature name of Microsoft Windows
        
    """
    if validate_request(request):
        return { 'value': socfaker.file.signature }

@api_bp.route("/file/signature_status", methods=['GET'])
def socfaker_file_signature_status():
    """
    The signature status of a file

        Returns:
            str: A randomly selected signature status of Verified, Unknown, or Counterfit
        
    """
    if validate_request(request):
        return { 'value': socfaker.file.signature_status }

@api_bp.route("/file/signed", methods=['GET'])
def socfaker_file_signed():
    """
    Whether the file is signed or not

        Returns:
            str: Returns whether a file is signed or not
        
    """
    if validate_request(request):
        return { 'value': socfaker.file.signed }

@api_bp.route("/file/size", methods=['GET'])
def socfaker_file_size():
    """
    The file size

        Returns:
            str: A randomly generated file size
        
    """
    if validate_request(request):
        return { 'value': socfaker.file.size }

@api_bp.route("/file/timestamp", methods=['GET'])
def socfaker_file_timestamp():
    """
    The timestamp of a file in the past

        Returns:
            str: A randomly generated file timestamp is ISO 8601 format
        
    """
    if validate_request(request):
        return { 'value': socfaker.file.timestamp }

@api_bp.route("/file/type", methods=['GET'])
def socfaker_file_type():
    """
    The type of a file

        Returns:
            str: A randomly selected file type
        
    """
    if validate_request(request):
        return { 'value': socfaker.file.type }

@api_bp.route("/file/version", methods=['GET'])
def socfaker_file_version():
    """
    A random generated file version string

        Returns:
            str: A randomly generated file version string
        
    """
    if validate_request(request):
        return { 'value': socfaker.file.version }

### FILE ROUTES ###

@api_bp.route("/http", methods=['GET'])
def socfaker_socfaker_http():
    """
    Data related to HTTP requests and responses

        Returns:
            HTTP: Returns an object with properties about HTTP requests and responses
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.http))

@api_bp.route("/http/bytes", methods=['GET'])
def socfaker_http_bytes():
    """
    Random bytes for an HTTP request

        Returns:
            int: Random bytes for an HTTP request
        
    """
    if validate_request(request):
        return { 'value': socfaker.http.bytes }

@api_bp.route("/http/method", methods=['GET'])
def socfaker_http_method():
    """
    A randomly selected method for an HTTP request or response

        Returns:
            str: A randomly selected method for an HTTP request or response
        
    """
    if validate_request(request):
        return { 'value': socfaker.http.method }

@api_bp.route("/http/request", methods=['GET'])
def socfaker_http_request():
    """
    A randomly generated request dictionary based on Elastic ECS format

        Returns:
            dict: A random request dictionary containing body, bytes, method and referrer information 
        
    """
    if validate_request(request):
        return { 'value': socfaker.http.request }

@api_bp.route("/http/response", methods=['GET'])
def socfaker_http_response():
    """
    A randomly generated response dictionary based on Elastic ECS format

        Returns:
            dict: A random response dictionary containing body, bytes, and status code information 
        
    """
    if validate_request(request):
        return { 'value': socfaker.http.response }

@api_bp.route("/http/status_code", methods=['GET'])
def socfaker_http_status_code():
    """
    A randomly selected status_code for an HTTP request or response

        Returns:
            str: A randomly selected status code for an HTTP request or response
        
    """
    if validate_request(request):
        return { 'value': socfaker.http.status_code }

### FILE ROUTES ###
### LOCATION ROUTES ###

@api_bp.route("/location", methods=['GET'])
def socfaker_socfaker_location():
    """
    Fake location data

        Returns:
            Location: Returns an object with properties containing location information
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.location))

@api_bp.route("/location/city", methods=['GET'])
def socfaker_location_city():
    """
    A random city

        Returns:
            str: Returns a random city name
        
    """
    if validate_request(request):
        return { 'value': socfaker.location.city }

@api_bp.route("/location/continent", methods=['GET'])
def socfaker_location_continent():
    """
    A random continent

        Returns:
            str: Returns a random continent
        
    """
    if validate_request(request):
        return { 'value': socfaker.location.continent }

@api_bp.route("/location/country", methods=['GET'])
def socfaker_location_country():
    """
    A random country

        Returns:
            str: Returns a random country
        
    """
    if validate_request(request):
        return { 'value': socfaker.location.country }

@api_bp.route("/location/country_code", methods=['GET'])
def socfaker_location_country_code():
    """
    A random country code

        Returns:
            str: Returns a random country code
        
    """
    if validate_request(request):
        return { 'value': socfaker.location.country_code }

@api_bp.route("/location/latitude", methods=['GET'])
def socfaker_location_latitude():
    """
    Random Latitude coordinates

        Returns:
            str: Returns a random latitude coordinates
        
    """
    if validate_request(request):
        return { 'value': socfaker.location.latitude }

@api_bp.route("/location/longitude", methods=['GET'])
def socfaker_location_longitude():
    """
    Random Longitude coordinates

        Returns:
            str: Returns a random longitude coordinates
        
    """
    if validate_request(request):
        return { 'value': socfaker.location.longitude }

### LOCATION ROUTES ###
### LOGS ROUTES ###

@api_bp.route("/logs/syslog", methods=['POST'])
def socfaker_logs_syslog(type='ransomware', count=1):
    """
    The syslog method generates random syslog messages based on the type and count requested

        Args:
            type (str, optional): Generates random syslog files with ransomware traffic added randomly. Defaults to 'ransomware'.
            count (int, optional): The number of logs to generate. Defaults to 10.

        Returns:
            list: Returns a list of generated syslogs
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.logs.syslog(type=type, count=count)))

@api_bp.route("/logs/windows/eventlog", methods=['POST'])
def socfaker_windows_eventlog(count=1, computer_name=None, os_version='Windows', json=False):
    """
    Generate fake event logs based on the provided inputs

        Args:
            count (int, optional): The number of logs to generate. Defaults to 1.
            computer_name (str, optional): A computer name to use when generating logs. Defaults to None.
            os_version (str, optional): The Operating System version to use when generating logs. Defaults to 'Windows'.
            json (bool, optional): Whether or not to if validate_request(request):
        return data as JSON or XML. Defaults to False.

        Returns:
            list: Returns a list of generated Windows Event Logs
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.logs.windows.eventlog(count=count, computer_name=computer_name, os_version=os_version, json=json)))

@api_bp.route("/logs/windows/sysmon", methods=['POST'])
def socfaker_sysmon_get(count=1):
    """
    Returns a list of generated sysmon logs

        Args:
            count (int, optional): The number of sysmon logs to return. Defaults to 21.

        Returns:
            list: A list of generated sysmon logs
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.logs.windows.sysmon(count=count)))

### LOGS ROUTES ###
### NETWORK ROUTES ###

@api_bp.route("/network", methods=['GET'])
def socfaker_socfaker_network():
    """
    Access common generated network information

        Returns:
            Network: Returns an object with properties containing general
            or common network information
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.network))

@api_bp.route("/network/get_cidr_range", methods=['POST'])
def socfaker_network_get_cidr_range(cidr):
    """
    Returns an IPv4 range

        Returns:
            str: Returns CIDR range for an IPv4 address.
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.network.get_cidr_range(cidr=cidr)))

@api_bp.route("/network/ipv4", methods=['GET'])
def socfaker_network_ipv4():
    """
    Returns an IPv4 IP Address

        Returns:
            str: Returns an IPv4 Address.  If private the address will be 10.x.x.x or 172.x.x.x or 192.168.x.x.
        
    """
    if validate_request(request):
        return { 'value': socfaker.network.ipv4 }

@api_bp.route("/network/ipv6", methods=['GET'])
def socfaker_network_ipv6():
    """
    Returns an IPv6 IP Address

        Returns:
            dict: Returns a compressed and exploded IPv6 Address.
        
    """
    if validate_request(request):
        return { 'value': socfaker.network.ipv6 }

@api_bp.route("/network/netbios", methods=['GET'])
def socfaker_network_netbios():
    """
    Returns a netbios name

        Returns:
            str: Returns a random netbios name
        
    """
    if validate_request(request):
        return { 'value': socfaker.network.netbios }

@api_bp.route("/network/port", methods=['GET'])
def socfaker_network_port():
    """
    Returns a dictionary map of a port and it's common name

        Returns:
            dict: A random port and it's common name
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.network.port))

@api_bp.route("/network/protocol", methods=['GET'])
def socfaker_network_protocol():
    """
    Random network protocol

        Returns:
            dict: Returns a random network protocol and protocol number
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.network.protocol))

### NETWORK ROUTES ###
### OPERATING_SYSTEM ROUTES ###

@api_bp.route("/operating_system", methods=['GET'])
def socfaker_socfaker_operating_system():
    """
    Fake operating system information

        Returns:
            OperatingSystem: Returns an object with properties containing
            Operating System information
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.operating_system))

@api_bp.route("/operating_system/family", methods=['GET'])
def socfaker_operatingsystem_family():
    """
    The operating system family

        Returns:
            str: Returns a random operating system family
        
    """
    if validate_request(request):
        return { 'value': socfaker.operating_system.family }

@api_bp.route("/operating_system/fullname", methods=['GET'])
def socfaker_operatingsystem_fullname():
    """
    The operating system full name

        Returns:
            str: Returns a random operating system full name including name, type and version
        
    """
    if validate_request(request):
        return { 'value': socfaker.operating_system.fullname }

@api_bp.route("/operating_system/name", methods=['GET'])
def socfaker_operatingsystem_name():
    """
    The operating system name

        Returns:
            str: Returns a random operating system name
        
    """
    if validate_request(request):
        return { 'value': socfaker.operating_system.name }

@api_bp.route("/operating_system/version", methods=['GET'])
def socfaker_operatingsystem_version():
    """
    The operating system version

        Returns:
            str: Returns a random operating system version
        
    """
    if validate_request(request):
        return { 'value': socfaker.operating_system.version }

### OPERATING_SYSTEM ROUTES ###
### ORGANIZATION ROUTES ###

@api_bp.route("/organization", methods=['GET'])
def socfaker_socfaker_organization():
    """
    Fake organization information

        Returns:
            Organization: Returns an object with properties containing common
            organization information
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.organization))

@api_bp.route("/organization/division", methods=['GET'])
def socfaker_organization_division():
    """
    Returns a division within an organization

        Returns:
            str: Returns a division within an organization
        
    """
    if validate_request(request):
        return { 'value': socfaker.organization.division }

@api_bp.route("/organization/domain", methods=['GET'])
def socfaker_organization_domain():
    """
    Returns a domain name based on the organization name

        Returns:
            str: Returns a domain name based on the organizational name
        
    """
    if validate_request(request):
        return { 'value': socfaker.organization.domain }

@api_bp.route("/organization/name", methods=['GET'])
def socfaker_organization_name():
    """
    A randomly generated organization name

        Returns:
            str: A randomly generated organization name
        
    """
    if validate_request(request):
        return { 'value': socfaker.organization.name }

@api_bp.route("/organization/title", methods=['GET'])
def socfaker_organization_title():
    """
    Returns a title within an organization

        Returns:
            str: Returns a title within an organization
        
    """
    if validate_request(request):
        return { 'value': socfaker.organization.title }

### ORGANIZATION ROUTES ###
### PCAP ROUTES ###

@api_bp.route("/pcap", methods=['POST'])
def socfaker_pcap_generate(count=1, port=9600):
    """
    None
    """
    if validate_request(request):
        return jsonify(str(socfaker.pcap(count=count)))

### PCAP ROUTES ###
### REGISTRY ROUTES ###

@api_bp.route("/registry", methods=['GET'])
def socfaker_socfaker_registry():
    """
    Fake registry information

        Returns:
            Registry: Returns an object with properties containing
            common Windows registry information
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.registry))

@api_bp.route("/registry/hive", methods=['GET'])
def socfaker_registry_hive():
    """
    A random registry hive

        Returns:
            str: Returns a random registry hive
        
    """
    if validate_request(request):
        return { 'value': socfaker.registry.hive }

@api_bp.route("/registry/key", methods=['GET'])
def socfaker_registry_key():
    """
    A random registry key

        Returns:
            str: Returns a random registry key
        
    """
    if validate_request(request):
        return { 'value': socfaker.registry.key }

@api_bp.route("/registry/path", methods=['GET'])
def socfaker_registry_path():
    """
    A full registry path
        
        Returns:
            str: Returns a random full registry path
        
    """
    if validate_request(request):
        return { 'value': socfaker.registry.path }

@api_bp.route("/registry/root", methods=['GET'])
def socfaker_registry_root():
    """
    A random registry root path string

        Returns:
            str: Returns a random registry root path string
        
    """
    if validate_request(request):
        return { 'value': socfaker.registry.root }

@api_bp.route("/registry/type", methods=['GET'])
def socfaker_registry_type():
    """
    A random registry key type

        Returns:
            str: A random registry key type
        
    """
    if validate_request(request):
        return { 'value': socfaker.registry.type }

@api_bp.route("/registry/value", methods=['GET'])
def socfaker_registry_value():
    """
    A random registry key value

        Returns:
            str: A random registry key value
        
    """
    if validate_request(request):
        return { 'value': socfaker.registry.value }

### REGISTRY ROUTES ###
### TIMESTAMP ROUTES ###

@api_bp.route("/timestamp", methods=['GET'])
def socfaker_socfaker_timestamp():
    """
    Fake timestamp information

        Returns:
            Timestamp: Returns an object with methods to generate fake
            timestamps
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.timestamp))

@api_bp.route("/timestamp/date_string", methods=['POST'])
def socfaker_timestamp_date_string(years=81, months=5, days=162):
    """
    Returns a date string

        Args:
            years ([type], optional): The number of years subtracted from the current time. Defaults to random.randint(18,85).
            months ([type], optional): The number of months subtracted from the current time. Defaults to random.randint(1,12).
            days ([type], optional): The number of days subtracted from the current time. Defaults to random.randint(1,365).

        Returns:
            str: An date string for the generated timestamp
        
    """
    if validate_request(request):
        return {'value': socfaker.timestamp.date_string(years=years, months=months, days=days)}

@api_bp.route("/timestamp/in_the_future", methods=['POST'])
def socfaker_timestamp_in_the_future(years=0, months=0, days=4, hours=13, minutes=25, seconds=3):
    """
    Generates a timestamp in the future

        Args:
            years (int, optional): The number of years to add from the current time. Defaults to 0.
            months ([type], optional): The number of months to add from the current time. Defaults to random.randint(0,3).
            days ([type], optional): The number of days to add from the current time. Defaults to random.randint(1,15).
            hours ([type], optional): The number of hours to add from the current time. Defaults to random.randint(1,24).
            minutes ([type], optional): The number of minutes to add from the current time. Defaults to random.randint(1,60).
            seconds ([type], optional): The number of seconds to add from the current time. Defaults to random.randint(1,60).

        Returns:
            str: Returns an ISO 8601 timestamp string
        
    """
    if validate_request(request):
        return {'value': socfaker.timestamp.in_the_future(years=years, months=months, days=days, hours=hours, minutes=minutes, seconds=seconds)}

@api_bp.route("/timestamp/in_the_past", methods=['POST'])
def socfaker_timestamp_in_the_past(years=0, months=2, days=6, hours=19, minutes=37, seconds=5):
    """
    Generates a timestamp in the past

        Args:
            years (int, optional): The number of years to subtract from the current time. Defaults to 0.
            months ([type], optional): The number of months to subtract from the current time. Defaults to random.randint(0,3).
            days ([type], optional): The number of days to subtract from the current time. Defaults to random.randint(1,15).
            hours ([type], optional): The number of hours to subtract from the current time. Defaults to random.randint(1,24).
            minutes ([type], optional): The number of minutes to subtract from the current time. Defaults to random.randint(1,60).
            seconds ([type], optional): The number of seconds to subtract from the current time. Defaults to random.randint(1,60).

        Returns:
            str: Returns an ISO 8601 timestamp string
        
    """
    if validate_request(request):
        return {'value': socfaker.timestamp.in_the_past(years=years, months=months, days=days, hours=hours, minutes=minutes, seconds=seconds)}

@api_bp.route("/timestamp/current", methods=['GET'])
def socfaker_timestamp_current():
    """
    The current timestamp

        Returns:
            str: Returns the current timestamp in ISO 8601 format
        
    """
    if validate_request(request):
        return { 'value': socfaker.timestamp.current }


### TIMESTAMP ROUTES ###
### USER_AGENT ROUTES ###

@api_bp.route("/user_agent", methods=['GET'])
def socfaker_socfaker_user_agent():
    """
    Fake user agent information

        Returns:
            UserAgent: Returns an object with methods to generate fake
            user agent strings
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.user_agent))

### USER_AGENT ROUTES ###
### VULNERABILITY ROUTES ###


@api_bp.route("/vulnerability/critical", methods=['GET'])
def socfaker_vulnerability_critical():
    """
    Returns a list of critical vulnerabilities based on counts provided when instantiating the class

        Returns:
            list: Returns a list of critical vulnerabilities
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.vulnerability().critical))

@api_bp.route("/vulnerability/data", methods=['GET'])
def socfaker_vulnerability_data():
    """
    Returns all vulnerability data

        Returns:
            json: Returns json of all vulnerability data
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.vulnerability().data))

@api_bp.route("/vulnerability/high", methods=['GET'])
def socfaker_vulnerability_high():
    """
    Returns a list of high vulnerabilities based on counts provided when instantiating the class

        Returns:
            list: Returns a list of high vulnerabilities
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.vulnerability().high))


@api_bp.route("/vulnerability/informational", methods=['GET'])
def socfaker_vulnerability_informational():
    """
    Returns a list of informational vulnerabilities based on counts provided when instantiating the class

        Returns:
            list: Returns a list of informational vulnerabilities
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.vulnerability().informational))

@api_bp.route("/vulnerability/low", methods=['GET'])
def socfaker_vulnerability_low():
    """
    Returns a list of low vulnerabilities based on counts provided when instantiating the class

        Returns:
            list: Returns a list of low vulnerabilities
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.vulnerability().low))

@api_bp.route("/vulnerability/medium", methods=['GET'])
def socfaker_vulnerability_medium():
    """
    Returns a list of medium vulnerabilities based on counts provided when instantiating the class

        Returns:
            list: Returns a list of medium vulnerabilities
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.vulnerability().medium))

@api_bp.route("/vulnerability/host", methods=['GET'])
def socfaker_vulnerability_host():
    """
    Retrieve information about hosts found in a vulnerability scan

        Returns:
            VulnerabilityHost: Returns an object with properties for a vulnerable host
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.vulnerability().host))

@api_bp.route("/vulnerability/host/checks_considered", methods=['GET'])
def socfaker_vulnerabilityhost_checks_considered():
    """
    A count of how many vulnerability checks were considered for a host

        Returns:
            int: Returns a randomly integer for checks considered during a vulnerability scan
        
    """
    if validate_request(request):
        return { 'value': socfaker.vulnerability().host.checks_considered }

@api_bp.route("/vulnerability/host/critical", methods=['GET'])
def socfaker_vulnerabilityhost_critical():
    """
    Returns a list of critical vulnerabilities based on counts provided when instantiating the class

        Returns:
            list: Returns a list of critical vulnerabilities
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.vulnerability().host.critical))

@api_bp.route("/vulnerability/host/data", methods=['GET'])
def socfaker_vulnerabilityhost_data():
    """
    Returns all vulnerability data

        Returns:
            json: Returns json of all vulnerability data
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.vulnerability().host.data))

@api_bp.route("/vulnerability/host/fqdn", methods=['GET'])
def socfaker_vulnerabilityhost_fqdn():
    """
    A host FQDN

        Returns:
            str: Returns a randomly generated DNS name
        
    """
    if validate_request(request):
        return { 'value': socfaker.vulnerability().host.fqdn }

@api_bp.route("/vulnerability/host/high", methods=['GET'])
def socfaker_vulnerabilityhost_high():
    """
    Returns a list of high vulnerabilities based on counts provided when instantiating the class

        Returns:
            list: Returns a list of high vulnerabilities
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.vulnerability().host.high))

@api_bp.route("/vulnerability/host/host", methods=['GET'])
def socfaker_vulnerabilityhost_host():
    """
    Retrieve information about hosts found in a vulnerability scan

        Returns:
            VulnerabilityHost: Returns an object with properties for a vulnerable host
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.vulnerability().host.host))

@api_bp.route("/vulnerability/host/host_id", methods=['GET'])
def socfaker_vulnerabilityhost_host_id():
    """
    Returns a random host ID

        Returns:
            int: Returns a random host ID
        
    """
    if validate_request(request):
        return { 'value': socfaker.vulnerability().host.host_id }

@api_bp.route("/vulnerability/host/informational", methods=['GET'])
def socfaker_vulnerabilityhost_informational():
    """
    Returns a list of informational vulnerabilities based on counts provided when instantiating the class

        Returns:
            list: Returns a list of informational vulnerabilities
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.vulnerability().host.informational))

@api_bp.route("/vulnerability/host/low", methods=['GET'])
def socfaker_vulnerabilityhost_low():
    """
    Returns a list of low vulnerabilities based on counts provided when instantiating the class

        Returns:
            list: Returns a list of low vulnerabilities
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.vulnerability().host.low))

@api_bp.route("/vulnerability/host/mac_address", methods=['GET'])
def socfaker_vulnerabilityhost_mac_address():
    """
    A host MAC Address

        Returns:
            str: Returns a randomly generated MAC Address
        
    """
    if validate_request(request):
        return {'value': socfaker.vulnerability().host.mac_address}

@api_bp.route("/vulnerability/host/medium", methods=['GET'])
def socfaker_vulnerabilityhost_medium():
    """
    Returns a list of medium vulnerabilities based on counts provided when instantiating the class

        Returns:
            list: Returns a list of medium vulnerabilities
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.vulnerability().host.medium))

@api_bp.route("/vulnerability/host/name", methods=['GET'])
def socfaker_vulnerabilityhost_name():
    """
    Returns a computer name

        Returns:
            str: Returns a randomly generated computer name
        
    """
    if validate_request(request):
        return { 'value': socfaker.vulnerability().host.name }

@api_bp.route("/vulnerability/host/percentage", methods=['GET'])
def socfaker_vulnerabilityhost_percentage():
    """
    Returns a percentage of vulnerabilities found on a host

        Returns:
            dict: Returns a percentage of vulnerabilities found on a host
        
    """
    if validate_request(request):
        return {'value': socfaker.vulnerability().host.percentage}

@api_bp.route("/vulnerability/host/scan", methods=['GET'])
def socfaker_vulnerabilityhost_scan():
    """
    A vulnerability scan

        Returns:
            VulnerabilityScan: Returns a vulnerability scan object with properties related a vulnerability scan
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.vulnerability().host.scan))

@api_bp.route("/vulnerability/host/total_score", methods=['GET'])
def socfaker_vulnerabilityhost_total_score():
    """
    The total score of a host during a vulnerability scan

        Returns:
            int: The total score for a host during a vulnerability scan
        
    """
    if validate_request(request):
        return { 'value': socfaker.vulnerability().host.total_score }

@api_bp.route("/vulnerability/scan", methods=['POST'])
def socfaker_vulnerability_scan(host_count=1, critical=1, high=1, medium=1, low=1, informational=1):
    if validate_request(request):
        return jsonify(str(socfaker.vulnerability(host_count=host_count, critical=critical, high=high, medium=medium, low=low, informational=informational).scan))

@api_bp.route("/vulnerability/scan/end_time", methods=['GET'])
def socfaker_vulnerabilityscan_end_time():
    """
    End time of a vulnerability scan

        Returns:
            str: The end time of a vulnerability scan in the future
        
    """
    if validate_request(request):
        return { 'value': socfaker.vulnerability().scan.end_time }

@api_bp.route("/vulnerability/scan/host_count", methods=['GET'])
def socfaker_vulnerabilityscan_host_count():
    """
    A vulnerability scan host count

        Returns:
            int: The provided vulnerability scan host count
        
    """
    if validate_request(request):
        return { 'value': socfaker.vulnerability().scan.host_count }

@api_bp.route("/vulnerability/scan/id", methods=['GET'])
def socfaker_vulnerabilityscan_id():
    """
    A vulnerability scan ID

        Returns:
            int: Returns a random vulnerability scan ID
        
    """
    if validate_request(request):
        return { 'value': socfaker.vulnerability().scan.id }

@api_bp.route("/vulnerability/scan/ip_list", methods=['GET'])
def socfaker_vulnerabilityscan_ip_list():
    """
    A list of host IPs during a Vulnerability scan

        Returns:
            list: A randomly generated list of host IPs during a vulnerability scan
        
    """
    if validate_request(request):
        return { 'value': socfaker.vulnerability().scan.ip_list }

@api_bp.route("/vulnerability/scan/name", methods=['GET'])
def socfaker_vulnerabilityscan_name():
    """
    A vulnerability scan name

        Returns:
            str: A randomly selected vulnerability scan name
        
    """
    if validate_request(request):
        return { 'value': socfaker.vulnerability().scan.name }

@api_bp.route("/vulnerability/scan/scan_uuid", methods=['GET'])
def socfaker_vulnerabilityscan_scan_uuid():
    """
    A vulnerability scan UUID

        Returns:
            str: A random UUID for a vulnerability scan
        
    """
    if validate_request(request):
        return { 'value': socfaker.vulnerability().scan.scan_uuid }

@api_bp.route("/vulnerability/scan/scanner_name", methods=['GET'])
def socfaker_vulnerabilityscan_scanner_name():
    """
    A vulnerability scaner name

        Returns:
            str: Returns a random vulnerability scanner name
        
    """
    if validate_request(request):
        return { 'value': socfaker.vulnerability().scan.scanner_name }

@api_bp.route("/vulnerability/scan/scanner_uuid", methods=['GET'])
def socfaker_vulnerabilityscan_scanner_uuid():
    """
    A vulnerability scanner UUID

        Returns:
            str: A random UUID for a scanner
        
    """
    if validate_request(request):
        return { 'value': socfaker.vulnerability().scan.scanner_uuid }

@api_bp.route("/vulnerability/scan/start_time", methods=['GET'])
def socfaker_vulnerabilityscan_start_time():
    """
    Start time of a vulnerability scan

        Returns:
            str: The start time of a vulnerability scan in the past
        
    """
    if validate_request(request):
        return { 'value': socfaker.vulnerability().scan.start_time }

@api_bp.route("/vulnerability/scan/status", methods=['GET'])
def socfaker_vulnerabilityscan_status():
    """
    Vulnerability scan status

        Returns:
            str: A randomly selected scan status
        
    """
    if validate_request(request):
        return { 'value': socfaker.vulnerability().scan.status }

@api_bp.route("/vulnerability/scan/type", methods=['GET'])
def socfaker_vulnerabilityscan_type():
    """
    The vulnerability scan type

        Returns:
            str: A randomly selected vulnerability scan type
        
    """
    if validate_request(request):
        return { 'value': socfaker.vulnerability().scan.type }

### VULNERABILITY ROUTES ###
### WORDS ROUTES ###

@api_bp.route("/words", methods=['GET'])
def socfaker_socfaker_words():
    """
    Used to create fake words or strings

        Returns:
            Words: Returns an object with methods to generate fake words and strings
        
    """
    if validate_request(request):
        return {'value': socfaker.words }

### WORDS ROUTES ###


### PRODUCT ROUTES ###

### PRODUCTS - AZURE - VM - DETAILS ###

@api_bp.route("/products/azure/details", methods=['GET'])
def socfaker_products_azure():
    """
    Azure class contains properties related to Azure products

        Returns:
            Azure: Microsoft Azure object containing properties and methods for generating data about Microsoft Azure products and services
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.products.azure.vm.details))

@api_bp.route("/products/azure/vm/details/location", methods=['GET'])
def socfaker_azureproperties_location():
    """
    A location based on Microsoft Azure available locations

        Returns:
            str: Returns a Azure location
        
    """
    if validate_request(request):
        return { 'value': socfaker.products.azure.vm.details.location }

@api_bp.route("/products/azure/vm/details/network_zone", methods=['GET'])
def socfaker_azureproperties_network_zone():
    """
    Network zone type in Microsoft Azure

        Returns:
            str: Returns a random type for a network zone in Azure
        
    """
    if validate_request(request):
        return { 'value': socfaker.products.azure.vm.details.network_zone }

@api_bp.route("/products/azure/vm/details/resource_group_id", methods=['GET'])
def socfaker_azureproperties_resource_group_id():
    """
    Resource Group ID

        Returns:
            str: Returns a random resource group ID (GUID)
        
    """
    if validate_request(request):
        return { 'value': socfaker.products.azure.vm.details.resource_group_id }

@api_bp.route("/products/azure/vm/details/resource_group_name", methods=['GET'])
def socfaker_azureproperties_resource_group_name():
    """
    Resource Group Name in Azure

        Returns:
            str: Returns a three-word Resource Group name for Microsoft Azure
        
    """
    if validate_request(request):
        return { 'value': socfaker.products.azure.vm.details.resource_group_name }

@api_bp.route("/products/azure/vm/details/score", methods=['GET'])
def socfaker_azureproperties_score():
    """
    None
    """
    if validate_request(request):
        return { 'value': socfaker.products.azure.vm.details.score }

@api_bp.route("/products/azure/vm/details/vm_name", methods=['GET'])
def socfaker_azureproperties_vm_name():
    """
    A Azure VM Name

        Returns:
            str: Returns a random Azure VM name
        
    """
    if validate_request(request):
        return { 'value': socfaker.products.azure.vm.details.vm_name }

### PRODUCTS - AZURE - VM - DETAILS ###
### PRODUCTS - AZURE - VM - METRICS ###

@api_bp.route("/products/azure/vm/metrics", methods=['POST'])
def socfaker_azurevmmetrics_generate():
    """
    Returns a list of dicts containing Azure VM Metrics

        Returns:
            list: A list of dicts containing metrics for an Azure VM
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.products.azure.vm.metrics.generate()))

@api_bp.route("/products/azure/vm/metrics/average", methods=['GET'])
def socfaker_azurevmmetrics_average():
    """
    None
    """
    if validate_request(request):
        return { 'value': socfaker.products.azure.vm.metrics.average }

@api_bp.route("/products/azure/vm/metrics/graphs", methods=['GET'])
def socfaker_azurevmmetrics_graphs():
    """
    None
    """
    if validate_request(request):
        return { 'value': socfaker.products.azure.vm.metrics.graphs }

### PRODUCTS - AZURE - VM - METRICS ###
### PRODUCTS - AZURE - VM - TOPOLOGY ###

@api_bp.route("/products/azure/vm/topology", methods=['GET'])
def socfaker_azurevmtopology_get():
    """
    None
    """
    if validate_request(request):
        return jsonify(str(socfaker.products.azure.vm.topology))

### PRODUCTS - AZURE - VM - TOPOLOGY ###
### PRODUCTS - ELASTIC ###

@api_bp.route("/products/elastic", methods=['GET'])
def socfaker_products_elastic():
    """
    Elastic class contains properties related to Elastic products

        Returns:
            Elastic: Elastic object containing properties and methods for generating data about Elastic products and services
        
    """
    if validate_request(request):
        return { 'value': socfaker.products.elastic }

@api_bp.route("/products/elastic/document", methods=['POST'])
def socfaker_elasticecs_get(count=1):
    """
    Generates one or more Elastic Common Schema documents

        Args:
            count (int, optional): The number of documents you want 
                                   generated. Defaults to 1.

        Returns:
            list: A list of ECS Document dictionaries
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.products.elastic.document.get(count=count)))

@api_bp.route("/products/elastic/document/fields", methods=['GET'])
def socfaker_elasticecs_fields():
    """
    None
    """
    if validate_request(request):
        return jsonify(str(socfaker.products.elastic.document.fields))

@api_bp.route("/products/elastic/document/fields/agent", methods=['GET'])
def socfaker_elasticecsfields_agent():
    """
    Returns an ECS agent dictionary

        Returns:
            dict: Returns a dictionary of agent
                  fields/properties
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.products.elastic.document.fields.agent))

@api_bp.route("/products/elastic/document/fields/base", methods=['GET'])
def socfaker_elasticecsfields_base():
    """
    Returns an ECS base fields dictionary

        Returns:
            dict: Returns a dictionary of ECS base
                  fields/properties
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.products.elastic.document.fields.base))

@api_bp.route("/products/elastic/document/fields/client", methods=['GET'])
def socfaker_elasticecsfields_client():
    """
    Returns an ECS Client dictionary

        Returns:
            dict: Returns a dictionary of ECS 
                  client fields/properties
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.products.elastic.document.fields.client))

@api_bp.route("/products/elastic/document/fields/cloud", methods=['GET'])
def socfaker_elasticecsfields_cloud():
    """
    Returns an ECS Cloud dictionary

        Returns:
            dict: Returns a dictionary of ECS 
                  Cloud fields/properties
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.products.elastic.document.fields.cloud))

@api_bp.route("/products/elastic/document/fields/code_signature", methods=['GET'])
def socfaker_elasticecsfields_code_signature():
    """
    Returns an ECS Code Signature dictionary

        Returns:
            dict: Returns a dictionary of ECS 
                  Code Signature fields/properties
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.products.elastic.document.fields.code_signature))

@api_bp.route("/products/elastic/document/fields/container", methods=['GET'])
def socfaker_elasticecsfields_container():
    """
    Returns an ECS container dictionary

        Returns:
            dict: Returns a dictionary of ECS 
                  container fields/properties
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.products.elastic.document.fields.container))

@api_bp.route("/products/elastic/document/fields/destination", methods=['GET'])
def socfaker_elasticecsfields_destination():
    """
    Returns an ECS destination dictionary

        Returns:
            dict: Returns a dictionary of ECS 
                  destination fields/properties
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.products.elastic.document.fields.destination))

@api_bp.route("/products/elastic/document/fields/dll", methods=['GET'])
def socfaker_elasticecsfields_dll():
    """
    Returns an ECS DLL dictionary

        Returns:
            dict: Returns a dictionary of ECS 
                  DLL fields/properties
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.products.elastic.document.fields.dll))

@api_bp.route("/products/elastic/document/fields/dns", methods=['GET'])
def socfaker_elasticecsfields_dns():
    """
    Returns an ECS DNS dictionary

        Returns:
            dict: Returns a dictionary of ECS 
                  DNS fields/properties
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.products.elastic.document.fields.dns))

@api_bp.route("/products/elastic/document/fields/event", methods=['GET'])
def socfaker_elasticecsfields_event():
    """
    Returns an ECS Event dictionary

        Returns:
            dict: Returns a dictionary of ECS 
                  Event fields/properties
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.products.elastic.document.fields.event))

@api_bp.route("/products/elastic/document/fields/file", methods=['GET'])
def socfaker_elasticecsfields_file():
    """
    Returns an ECS file dictionary

        Returns:
            dict: Returns a dictionary of ECS 
                  file fields/properties
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.products.elastic.document.fields.file))

@api_bp.route("/products/elastic/document/fields/host", methods=['GET'])
def socfaker_elasticecsfields_host():
    """
    Returns an ECS host dictionary

        Returns:
            dict: Returns a dictionary of ECS 
                  host fields/properties
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.products.elastic.document.fields.host))

@api_bp.route("/products/elastic/document/fields/http", methods=['GET'])
def socfaker_elasticecsfields_http():
    """
    Returns an ECS HTTP dictionary

        Returns:
            dict: Returns a dictionary of ECS 
                  HTTP fields/properties
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.products.elastic.document.fields.http))

@api_bp.route("/products/elastic/document/fields/network", methods=['GET'])
def socfaker_elasticecsfields_network():
    """
    Returns an ECS network dictionary

        Returns:
            dict: Returns a dictionary of ECS 
                  network fields/properties
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.products.elastic.document.fields.network))

@api_bp.route("/products/elastic/document/fields/organization", methods=['GET'])
def socfaker_elasticecsfields_organization():
    """
    Returns an ECS Organization dictionary

        Returns:
            dict: Returns a dictionary of ECS 
                  organization fields/properties
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.products.elastic.document.fields.organization))

@api_bp.route("/products/elastic/document/fields/package", methods=['GET'])
def socfaker_elasticecsfields_package():
    """
    Returns an ECS package dictionary

        Returns:
            dict: Returns a dictionary of ECS 
                  package fields/properties
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.products.elastic.document.fields.package))

@api_bp.route("/products/elastic/document/fields/registry", methods=['GET'])
def socfaker_elasticecsfields_registry():
    """
    Returns an ECS Windows Registry dictionary

        Returns:
            dict: Returns a dictionary of ECS 
                  Windows Registry fields/properties
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.products.elastic.document.fields.registry))

@api_bp.route("/products/elastic/document/fields/server", methods=['GET'])
def socfaker_elasticecsfields_server():
    """
    Returns an ECS server dictionary

        Returns:
            dict: Returns a dictionary of ECS 
                  server fields/properties
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.products.elastic.document.fields.server))

@api_bp.route("/products/elastic/document/fields/source", methods=['GET'])
def socfaker_elasticecsfields_source():
    """
    Returns an ECS source dictionary

        Returns:
            dict: Returns a dictionary of ECS 
                  source fields/properties
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.products.elastic.document.fields.source))

@api_bp.route("/products/elastic/hits", methods=['POST'])
def socfaker_elastic_hits(count=10):
    """
    Returns a provided count of generated / fake Elasticsearch query hits.  Default is 10.

        Args:
            count (int, optional): The number of Elasticsearch query hits returned in a list. Defaults to 10.

        Returns:
            list: A list of Elasticsearch query hits
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.products.elastic.hits(count=count)))

### PRODUCTS - ELASTIC ###
### PRODUCTS - QUALYSGUARD ###

@api_bp.route("/products/qualysguard/scan", methods=['POST'])
def socfaker_qualysguard_scan(count=1, host_count=1):
    """
    Retrieve 1 or more QualysGuard VM scans for 1 or more hosts

        Args:
            count (int, optional): The number of scans to return. Defaults to 1.
            host_count (int, optional): The number of hosts within a scan. Defaults to 1.

        Returns:
            list: Returns a list of scans based on the provided inputs
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.products.qualysguard.scan(count=count, host_count=host_count)))

### PRODUCTS - QUALYSGUARD ###
### PRODUCTS - SERVICENOW ###

@api_bp.route("/products/servicenow/search", methods=['POST'])
def socfaker_servicenow_search(random_keyword=None):
    """
    Generates a fake response from a ServiceNow Incident Search

        Args:
            random_keyword (str, optional): Adds a random keyword string you provide to fields within the generated response object. Defaults to None.

        Returns:
            dict: A ServiceNow Incident Search response object
        
    """
    if validate_request(request):
        return jsonify(str(socfaker.products.servicenow.search(random_keyword=random_keyword)))
