import ast
import pendulum
from flask import Blueprint, render_template, request, abort, jsonify, url_for, flash, redirect, session
from socfakerservice import status, HTMLRenderer, set_renderers, app
from socfakerservice.frontend.nav import nav
from socfaker import SocFaker


socfaker = SocFaker()

general_bp = Blueprint(
    'general',
    __name__
)

@general_bp.route("/agent", methods=['GET'])
def socfaker_socfaker_agent():
    """
    Access generated data related to an endpoint agent

        Returns:
            Agent: Returns an object with properties related to an endpoint agent
        
    """
    return ast.literal_eval(str(socfaker.agent))

@general_bp.route("/agent/ephermeral_id", methods=['GET'])
def socfaker_agent_ephermeral_id():
    """
    A unique and random ephermal ID that changes

        Returns:
            str: A unique 8 character length hex ID
        
    """
    return { 'value': socfaker.agent.ephermeral_id }

@general_bp.route("/agent/id", methods=['GET'])
def socfaker_agent_id():
    """
    A agent ID which is typically static across the lifetime of the 
           agent (per instance of this class)

        Returns:
            str: A static but unique 8 character length ID representing the agent ID
        
    """
    return { 'value': socfaker.agent.id }

@general_bp.route("/agent/name", methods=['GET'])
def socfaker_agent_name():
    """
    A custom name of the agent

        Returns:
            str: A custom name of the agent
        
    """
    return { 'value': socfaker.agent.name }

@general_bp.route("/agent/type", methods=['GET'])
def socfaker_agent_type():
    """
    The type of agent.

        Options are: 'filebeat', 'auditbeat', 'functionbeat', 
                     'heartbeat', 'winlogbeat', 'packetbeat'

        Returns:
            str: A agent type
        
    """
    return { 'value': socfaker.agent.type }

@general_bp.route("/agent/version", methods=['GET'])
def socfaker_agent_version():
    """
    The agent version

        Returns:
            str: Currently set to a static value of 7.8.0
        
    """
    return { 'value': socfaker.agent.version }

### AGENT ROUTES ###
### ALERT ROUTES ###

@general_bp.route("/alert", methods=['GET'])
def socfaker_socfaker_alert():
    """
    Alert or Detection properties

        Returns:
            Alert: Returns an object with properties about a alert or detection
        
    """
    return ast.literal_eval(str(socfaker.alert))

@general_bp.route("/alert/action", methods=['GET'])
def socfaker_alert_action():
    """
    An action taken based on the alert

        Returns:
            str: Returns a random action based on the alert
        
    """
    return { 'value': socfaker.alert.action }

@general_bp.route("/alert/direction", methods=['GET'])
def socfaker_alert_direction():
    """
    The direction of the alert (network based)

        Returns:
            str: Random direction of from or to
        
    """
    return { 'value': socfaker.alert.direction }

@general_bp.route("/alert/location", methods=['GET'])
def socfaker_alert_location():
    """
    The country the alert originated from

        Returns:
            str: A random country an alert was generated from
        
    """
    return { 'value': socfaker.alert.location }

@general_bp.route("/alert/signature_name", methods=['GET'])
def socfaker_alert_signature_name():
    """
    Returns the name of a signature that the Alert triggered upon

        Returns:
            Str: returns a random alert signature name
        
    """
    return { 'value': socfaker.alert.signature_name }

@general_bp.route("/alert/status", methods=['GET'])
def socfaker_alert_status():
    """
    The current alert status

        Returns:
            str: Returns whether the alert was successful 
                 or unsuccessful
        
    """
    return { 'value': socfaker.alert.status }

@general_bp.route("/alert/summary", methods=['GET'])
def socfaker_alert_summary():
    """
    Returns the summary of an alert

        Returns:
            str: Returns a string of this instance of an alert.  
                 Contains a status, action, type, direction, and location.
        
    """
    return { 'value': socfaker.alert.summary }

@general_bp.route("/alert/type", methods=['GET'])
def socfaker_alert_type():
    """
    Returns an alert type

        Returns:
            str: Returns a random alert type
        
    """
    return { 'value': socfaker.alert.type }

### ALERT ROUTES ###
### APPLICATION ROUTES ###

@general_bp.route("/application", methods=['GET'])
def socfaker_socfaker_application():
    """
    Generated data related to a application

        Returns:
            Application: Returns an object with properties about an application
        
    """
    return ast.literal_eval(str(socfaker.application))

@general_bp.route("/application/account_status", methods=['GET'])
def socfaker_application_account_status():
    """
    A random account status for the application

        Returns:
            str: Returns whether an account is enabled or 
                 disabled for an application
        
    """
    return { 'value': socfaker.application.account_status }

@general_bp.route("/application/logon_timestamp", methods=['GET'])
def socfaker_application_logon_timestamp():
    """
    Logon timestamp of a user/service for an applicaiton

        Returns:
            str: Returns an ISO 8601 timestamp in the past
        
    """
    return { 'value': socfaker.application.logon_timestamp }

@general_bp.route("/application/name", methods=['GET'])
def socfaker_application_name():
    """
    The name of an application

        Returns:
            str: Returns a random application name based on common 
                 applications used in enterprises
        
    """
    return { 'value': socfaker.application.name }

@general_bp.route("/application/status", methods=['GET'])
def socfaker_application_status():
    """
    Returns the application status

        Returns:
            str: Returns the application status of 
                 Active, Inactive, or Legacy
        
    """
    return { 'value': socfaker.application.status }

### APPLICATION ROUTES ###
### CLOUD ROUTES ###

@general_bp.route("/cloud", methods=['GET'])
def socfaker_socfaker_cloud():
    """
    Generated data related to cloud infrastructure

        Returns:
            Cloud: Returns an object with properties about cloud infrastructure
        
    """
    return ast.literal_eval(str(socfaker.cloud))

@general_bp.route("/cloud/id", methods=['GET'])
def socfaker_cloud_id():
    """
    A cloud instance ID

        Returns:
            str: A random GUID for a cloud instance ID
        
    """
    return { 'value': socfaker.cloud.id }

@general_bp.route("/cloud/instance_id", methods=['GET'])
def socfaker_cloud_instance_id():
    """
    A random hex instance ID

        Returns:
            str: A random HEX character instance ID
        
    """
    return { 'value': socfaker.cloud.instance_id }

@general_bp.route("/cloud/name", methods=['GET'])
def socfaker_cloud_name():
    """
    The name of a cloud VM/container instance

        Returns:
            str: A random generated name of a cloud VM or container instance
        
    """
    return { 'value': socfaker.cloud.name }

@general_bp.route("/cloud/provider", methods=['GET'])
def socfaker_cloud_provider():
    """
    The cloud provider

        Returns:
            str: A random cloud provider of either aws, azure, gcp, or digitalocean
        
    """
    return { 'value': socfaker.cloud.provider }

@general_bp.route("/cloud/region", methods=['GET'])
def socfaker_cloud_region():
    """
    The region of a cloud instance

        Returns:
            str: The region of a cloud instance
        
    """
    return { 'value': socfaker.cloud.region }

@general_bp.route("/cloud/size", methods=['GET'])
def socfaker_cloud_size():
    """
    The size of a instance (based on AWS naming convention)

        Returns:
            str: A random size of an instance based on AWS naming convention
        
    """
    return { 'value': socfaker.cloud.size }

@general_bp.route("/cloud/zone", methods=['GET'])
def socfaker_cloud_zone():
    """
    A random generated availability zone in common cloud platforms like AWS & Azure

        Returns:
            str: A string representing a cloud availability zone
        
    """
    return { 'value': socfaker.cloud.zone }

### CLOUD ROUTES ###
### COMPUTER ROUTES ###

@general_bp.route("/computer", methods=['GET'])
def socfaker_socfaker_computer():
    """
    Generated data about a computer system

        Returns:
            Computer: Returns an object with properties about a computer system
        
    """
    return ast.literal_eval(str(socfaker.computer))

@general_bp.route("/computer/architecture", methods=['GET'])
def socfaker_computer_architecture():
    """
    Architecture of a computer instance

        Returns:
            str: Architecture of computer system of either x86_64 or x86
        
    """
    return { 'value': socfaker.computer.architecture }

@general_bp.route("/computer/disk", methods=['GET'])
def socfaker_computer_disk():
    """
    The disk size of a computer instance

        Returns:
            list: Returns a list of B,KB,MB,GB, and TB size of a computers disk
        
    """
    return { 'value': socfaker.computer.disk }

@general_bp.route("/computer/ipv4", methods=['GET'])
def socfaker_computer_ipv4():
    """
    The operating system ipv4 address

        Returns:
            str: A random operating system ipv4 address
        
    """
    return { 'value': socfaker.computer.ipv4 }

@general_bp.route("/computer/mac_address", methods=['GET'])
def socfaker_computer_mac_address():
    """
    A generated MAC address for a computer instance

        Returns:
            str: A random MAC Address
        
    """
    return { 'value': socfaker.computer.mac_address }

@general_bp.route("/computer/memory", methods=['GET'])
def socfaker_computer_memory():
    """
    The memory size of a computer instance

        Returns:
            list: Returns a list of B,KB,MB,GB, and TB size of a computers memory size
        
    """
    return { 'value': socfaker.computer.memory }

@general_bp.route("/computer/name", methods=['GET'])
def socfaker_computer_name():
    """
    The name of a comptuer

        Returns:
            str: A random name of a computer 
        
    """
    return { 'value': socfaker.computer.name }

@general_bp.route("/computer/os", methods=['GET'])
def socfaker_computer_os():
    """
    The operating system full name of the computer instance

        Returns:
            str: A random operating system version
        
    """
    return { 'value': socfaker.computer.os }

@general_bp.route("/computer/platform", methods=['GET'])
def socfaker_computer_platform():
    """
    A random name of the computers platform

        Returns:
            str: Random name of a computers platform (e.g. worksation, server, etc.)
        
    """
    return { 'value': socfaker.computer.platform }

### COMPUTER ROUTES ###
### CONTAINER ROUTES ###

@general_bp.route("/container", methods=['GET'])
def socfaker_socfaker_container():
    """
    Generated data about a container

        Returns:
            Container: Returns an object with properties about a container
        
    """
    return ast.literal_eval(str(socfaker.container))

@general_bp.route("/container/id", methods=['GET'])
def socfaker_container_id():
    """
    A container ID

        Returns:
            str: A hex container ID
        
    """
    return { 'value': socfaker.container.id }

@general_bp.route("/container/name", methods=['GET'])
def socfaker_container_name():
    """
    A random generated container name

        Returns:
            str: A randomly generated container name
        
    """
    return { 'value': socfaker.container.name }

@general_bp.route("/container/runtime", methods=['GET'])
def socfaker_container_runtime():
    """
    A container runtime

        Returns:
            str: Returns either docker or kubernetes
        
    """
    return { 'value': socfaker.container.runtime }

@general_bp.route("/container/tags", methods=['GET'])
def socfaker_container_tags():
    """
    Container tags

        Returns:
            list: A random list of container tags
        
    """
    return { 'value': socfaker.container.tags }

### CONTAINER ROUTES ###
### DNS ROUTES ###

@general_bp.route("/dns", methods=['GET'])
def socfaker_socfaker_dns():
    """
    DNS Information

        Returns:
            DNS: Returns an object with properties about DNS request, response, etc.
        
    """
    return ast.literal_eval(str(socfaker.dns))

@general_bp.route("/dns/answers", methods=['GET'])
def socfaker_dns_answers():
    """
    A list of DNS answers during a DNS request

        Returns:
            list: A random list (count) of random DNS answers during a DNS request
        
    """
    return socfaker.dns.answers

@general_bp.route("/dns/direction", methods=['GET'])
def socfaker_dns_direction():
    """
    The direction of a DNS request

        Returns:
            str: Returns a direction for a DNS request or response
        
    """
    return { 'value': socfaker.dns.direction }

@general_bp.route("/dns/header_flags", methods=['GET'])
def socfaker_dns_header_flags():
    """
    DNS Header flags

        Returns:
            str: A randomly selected DNS Header Flag
        
    """
    return { 'value': socfaker.dns.header_flags }

@general_bp.route("/dns/id", methods=['GET'])
def socfaker_dns_id():
    """
    A random DNS ID value from 10000,100000

        Returns:
            int: A random DNS ID value
        
    """
    return { 'value': socfaker.dns.id }

@general_bp.route("/dns/name", methods=['GET'])
def socfaker_dns_name():
    """
    Returns a randomly generated DNS name

        Returns:
            str: A random DNS Name
        
    """
    return { 'value': socfaker.dns.name }

@general_bp.route("/dns/op_code", methods=['GET'])
def socfaker_dns_op_code():
    """
    A DNS OP COde

        Returns:
            str: A random DNS OP Code for a DNS request
        
    """
    return { 'value': socfaker.dns.op_code }

@general_bp.route("/dns/question", methods=['GET'])
def socfaker_dns_question():
    """
    A DNS question during a DNS request

        Returns:
            dict: A random DNS question during a DNS request
        
    """
    return socfaker.dns.question

@general_bp.route("/dns/record", methods=['GET'])
def socfaker_dns_record():
    """
    A randomly selected record type

        Returns:
            str: A random DNS record (e.g. A, CNAME, PTR, etc.)
        
    """
    return { 'value': socfaker.dns.record }

@general_bp.route("/dns/response_code", methods=['GET'])
def socfaker_dns_response_code():
    """
    A DNS Response Code

        Returns:
            str: A DNS response code as part of a response made during a DNS request
        
    """
    return { 'value': socfaker.dns.response_code }


### DNS ROUTES ###
### EMPLOYEE ROUTES ###

@general_bp.route("/employee", methods=['GET'])
def socfaker_socfaker_employee():
    """
    An employee object

        Returns:
            Employee: Returns an object with properties about a fake employee
        
    """
    return ast.literal_eval(str(socfaker.employee))

@general_bp.route("/employee/account_status", methods=['GET'])
def socfaker_employee_account_status():
    """
    Account status of an employee

        Returns:
            str: Returns an employee's account status.  This is weighted towards enabled.
        
    """
    return { 'value': socfaker.employee.account_status }

@general_bp.route("/employee/department", methods=['GET'])
def socfaker_employee_department():
    """
    Employee department

        Returns:
            str: Returns a random employee department
        
    """
    return { 'value': socfaker.employee.department }

@general_bp.route("/employee/dob", methods=['GET'])
def socfaker_employee_dob():
    """
    Date of Birth of an employee

        Returns:
            str: Returns the date of birth (DOB) of an employee
        
    """
    return { 'value': socfaker.employee.dob }

@general_bp.route("/employee/email", methods=['GET'])
def socfaker_employee_email():
    """
    Email of an employee

        Returns:
            str: Returns the email address of an employee
        
    """
    return { 'value': socfaker.employee.email }

@general_bp.route("/employee/first_name", methods=['GET'])
def socfaker_employee_first_name():
    """
    First name of an employee

        Returns:
            str: Returns the first name of an employee
        
    """
    return { 'value': socfaker.employee.first_name }

@general_bp.route("/employee/gender", methods=['GET'])
def socfaker_employee_gender():
    """
    Gender of an employee

        Returns:
            str: Returns the gender of an employee
        
    """
    return { 'value': socfaker.employee.gender }

@general_bp.route("/employee/language", methods=['GET'])
def socfaker_employee_language():
    """
    The preferred employee language

        Returns:
            str: Returns a random language of an employee
        
    """
    return { 'value': socfaker.employee.language }

@general_bp.route("/employee/last_name", methods=['GET'])
def socfaker_employee_last_name():
    """
    Last name of an employee

        Returns:
            str: Returns the last name of an employee
        
    """
    return { 'value': socfaker.employee.last_name }

@general_bp.route("/employee/logon_timestamp", methods=['GET'])
def socfaker_employee_logon_timestamp():
    """
    Last logon timestamp of an employee

        Returns:
            str: Returns a random ISO 8601 timestamp of an employee in the past
        
    """
    return { 'value': socfaker.employee.logon_timestamp }

@general_bp.route("/employee/name", methods=['GET'])
def socfaker_employee_name():
    """
    Returns First and Last name of an employee

        Returns:
            str: Returns a random First and Last name of an employee
        
    """
    return { 'value': socfaker.employee.name }

@general_bp.route("/employee/phone_number", methods=['GET'])
def socfaker_employee_phone_number():
    """
    Phone number of an employee

        Returns:
            str: Returns a random phone number of an employee
        
    """
    return { 'value': socfaker.employee.phone_number }

@set_renderers(HTMLRenderer)
@general_bp.route("/employee/photo", methods=['GET'])
def socfaker_employee_photo():
    """
    Photo URL of an employee

        Returns:
            str: Returns a URL of a random photo for the employee
        
    """
    return f'<html><body><h1><img src="{socfaker.employee.photo}</h1></body></html>'

@general_bp.route("/employee/ssn", methods=['GET'])
def socfaker_employee_ssn():
    """
    SSN of an employee

        Returns:
            str: Returns the SSN of an employee
        
    """
    return { 'value': socfaker.employee.ssn }

@general_bp.route("/employee/title", methods=['GET'])
def socfaker_employee_title():
    """
    Employee title

        Returns:
            str: Returns a random employee title
        
    """
    return { 'value': socfaker.employee.title }

@general_bp.route("/employee/user_id", methods=['GET'])
def socfaker_employee_user_id():
    """
    User ID of an employee

        Returns:
            str: Returns a random user ID of an employee
        
    """
    return { 'value': socfaker.employee.user_id }

@general_bp.route("/employee/username", methods=['GET'])
def socfaker_employee_username():
    """
    Username of an employee

        Returns:
            str: Returns the username of an employee
        
    """
    return { 'value': socfaker.employee.username }

### EMPLOYEE ROUTES ###
### FILE ROUTES ###

@general_bp.route("/file", methods=['GET'])
def socfaker_socfaker_file():
    """
    A file object

        Returns:
            File: Returns an object with properties about a fake file object
        
    """
    return ast.literal_eval(str(socfaker.file))

@general_bp.route("/file/accessed_timestamp", methods=['GET'])
def socfaker_file_accessed_timestamp():
    """
    The last accessed timestamp of a file in the past

        Returns:
            str: A randomly generated accessed timestamp is ISO 8601 format
        
    """
    return { 'value': socfaker.file.accessed_timestamp }

@general_bp.route("/file/attributes", methods=['GET'])
def socfaker_file_attributes():
    """
    Attributes of the file 

        Returns:
            list: A randomly selected list of file attributes
        
    """
    return socfaker.file.attributes

@general_bp.route("/file/build_version", methods=['GET'])
def socfaker_file_build_version():
    """
    A build version of a file

        Returns:
            str: Returns the last digit in the version string
        
    """
    return { 'value': socfaker.file.build_version }

@general_bp.route("/file/checksum", methods=['GET'])
def socfaker_file_checksum():
    """
    A MD5 checksum of a file

        Returns:
            str: Returns a MD5 of the file
        
    """
    return { 'value': socfaker.file.checksum }

@general_bp.route("/file/directory", methods=['GET'])
def socfaker_file_directory():
    """
    The directory of a file

        Returns:
            str: The directory of a file
        
    """
    return { 'value': socfaker.file.directory }

@general_bp.route("/file/drive_letter", methods=['GET'])
def socfaker_file_drive_letter():
    """
    The drive letter of a file

        Returns:
            str: A randomly selected drive letter of a file
        
    """
    return { 'value': socfaker.file.drive_letter }

@general_bp.route("/file/extension", methods=['GET'])
def socfaker_file_extension():
    """
    The extension of a file

        Returns:
            str: The extension of a file
        
    """
    return { 'value': socfaker.file.extension }

@general_bp.route("/file/full_path", methods=['GET'])
def socfaker_file_full_path():
    """
    The full path of a file

        Returns:
            str: A randomly selected file name path
        
    """
    return { 'value': socfaker.file.full_path }

@general_bp.route("/file/gid", methods=['GET'])
def socfaker_file_gid():
    """
    The GID of a file

        Returns:
            str: A randomly generated GID of a file
        
    """
    return { 'value': socfaker.file.gid }

@general_bp.route("/file/hashes", methods=['GET'])
def socfaker_file_hashes():
    """
    A dict containing MD5, SHA1, and SHA256 hashes

        Returns:
            str: A randomly generated dict containing MD5, SHA1, and SHA256 hashes
        
    """
    return { 'value': socfaker.file.hashes }

@general_bp.route("/file/install_scope", methods=['GET'])
def socfaker_file_install_scope():
    """
    The install scope of a file

        Returns:
            str: Returns a random install scope of user-local or global for a file
        
    """
    return { 'value': socfaker.file.install_scope }

@general_bp.route("/file/md5", methods=['GET'])
def socfaker_file_md5():
    """
    A random generated MD5 hash

        Returns:
            str: A randomly generated MD5 file hash
        
    """
    return { 'value': socfaker.file.md5 }

@general_bp.route("/file/mime_type", methods=['GET'])
def socfaker_file_mime_type():
    """
    The mime type of a file

        Returns:
            str: A randomly selected file mime type
        
    """
    return { 'value': socfaker.file.mime_type }

@general_bp.route("/file/name", methods=['GET'])
def socfaker_file_name():
    """
    The name of a file

        Returns:
            str: A randomly selected file name
        
    """
    return { 'value': socfaker.file.name }

@general_bp.route("/file/sha1", methods=['GET'])
def socfaker_file_sha1():
    """
    A random generated SHA1 hash

        Returns:
            str: A randomly generated SHA1 file hash
        
    """
    return { 'value': socfaker.file.sha1 }

@general_bp.route("/file/sha256", methods=['GET'])
def socfaker_file_sha256():
    """
    A random generated SHA256 hash

        Returns:
            str: A randomly generated SHA256 file hash
        
    """
    return { 'value': socfaker.file.sha256 }

@general_bp.route("/file/signature", methods=['GET'])
def socfaker_file_signature():
    """
    The file signature

        Returns:
            str: Returns the signature name of Microsoft Windows
        
    """
    return { 'value': socfaker.file.signature }

@general_bp.route("/file/signature_status", methods=['GET'])
def socfaker_file_signature_status():
    """
    The signature status of a file

        Returns:
            str: A randomly selected signature status of Verified, Unknown, or Counterfit
        
    """
    return { 'value': socfaker.file.signature_status }

@general_bp.route("/file/signed", methods=['GET'])
def socfaker_file_signed():
    """
    Whether the file is signed or not

        Returns:
            str: Returns whether a file is signed or not
        
    """
    return { 'value': socfaker.file.signed }

@general_bp.route("/file/size", methods=['GET'])
def socfaker_file_size():
    """
    The file size

        Returns:
            str: A randomly generated file size
        
    """
    return { 'value': socfaker.file.size }

@general_bp.route("/file/timestamp", methods=['GET'])
def socfaker_file_timestamp():
    """
    The timestamp of a file in the past

        Returns:
            str: A randomly generated file timestamp is ISO 8601 format
        
    """
    return { 'value': socfaker.file.timestamp }

@general_bp.route("/file/type", methods=['GET'])
def socfaker_file_type():
    """
    The type of a file

        Returns:
            str: A randomly selected file type
        
    """
    return { 'value': socfaker.file.type }

@general_bp.route("/file/version", methods=['GET'])
def socfaker_file_version():
    """
    A random generated file version string

        Returns:
            str: A randomly generated file version string
        
    """
    return { 'value': socfaker.file.version }

### FILE ROUTES ###

@general_bp.route("/http", methods=['GET'])
def socfaker_socfaker_http():
    """
    Data related to HTTP requests and responses

        Returns:
            HTTP: Returns an object with properties about HTTP requests and responses
        
    """
    return ast.literal_eval(str(socfaker.http))

@general_bp.route("/http/bytes", methods=['GET'])
def socfaker_http_bytes():
    """
    Random bytes for an HTTP request

        Returns:
            int: Random bytes for an HTTP request
        
    """
    return { 'value': socfaker.http.bytes }

@general_bp.route("/http/method", methods=['GET'])
def socfaker_http_method():
    """
    A randomly selected method for an HTTP request or response

        Returns:
            str: A randomly selected method for an HTTP request or response
        
    """
    return { 'value': socfaker.http.method }

@general_bp.route("/http/request", methods=['GET'])
def socfaker_http_request():
    """
    A randomly generated request dictionary based on Elastic ECS format

        Returns:
            dict: A random request dictionary containing body, bytes, method and referrer information 
        
    """
    return { 'value': socfaker.http.request }

@general_bp.route("/http/response", methods=['GET'])
def socfaker_http_response():
    """
    A randomly generated response dictionary based on Elastic ECS format

        Returns:
            dict: A random response dictionary containing body, bytes, and status code information 
        
    """
    return { 'value': socfaker.http.response }

@general_bp.route("/http/status_code", methods=['GET'])
def socfaker_http_status_code():
    """
    A randomly selected status_code for an HTTP request or response

        Returns:
            str: A randomly selected status code for an HTTP request or response
        
    """
    return { 'value': socfaker.http.status_code }

### FILE ROUTES ###
### LOCATION ROUTES ###

@general_bp.route("/location", methods=['GET'])
def socfaker_socfaker_location():
    """
    Fake location data

        Returns:
            Location: Returns an object with properties containing location information
        
    """
    return ast.literal_eval(str(socfaker.location))

@general_bp.route("/location/city", methods=['GET'])
def socfaker_location_city():
    """
    A random city

        Returns:
            str: Returns a random city name
        
    """
    return { 'value': socfaker.location.city }

@general_bp.route("/location/continent", methods=['GET'])
def socfaker_location_continent():
    """
    A random continent

        Returns:
            str: Returns a random continent
        
    """
    return { 'value': socfaker.location.continent }

@general_bp.route("/location/country", methods=['GET'])
def socfaker_location_country():
    """
    A random country

        Returns:
            str: Returns a random country
        
    """
    return { 'value': socfaker.location.country }

@general_bp.route("/location/country_code", methods=['GET'])
def socfaker_location_country_code():
    """
    A random country code

        Returns:
            str: Returns a random country code
        
    """
    return { 'value': socfaker.location.country_code }

@general_bp.route("/location/latitude", methods=['GET'])
def socfaker_location_latitude():
    """
    Random Latitude coordinates

        Returns:
            str: Returns a random latitude coordinates
        
    """
    return { 'value': socfaker.location.latitude }

@general_bp.route("/location/longitude", methods=['GET'])
def socfaker_location_longitude():
    """
    Random Longitude coordinates

        Returns:
            str: Returns a random longitude coordinates
        
    """
    return { 'value': socfaker.location.longitude }

### LOCATION ROUTES ###
### LOGS ROUTES ###

@general_bp.route("/logs/syslog", methods=['POST'])
def socfaker_logs_syslog(type='ransomware', count=1):
    """
    The syslog method generates random syslog messages based on the type and count requested

        Args:
            type (str, optional): Generates random syslog files with ransomware traffic added randomly. Defaults to 'ransomware'.
            count (int, optional): The number of logs to generate. Defaults to 10.

        Returns:
            list: Returns a list of generated syslogs
        
    """
    return socfaker.logs.syslog(type=type, count=count)

@general_bp.route("/logs/windows/eventlog", methods=['POST'])
def socfaker_windows_eventlog(count=1, computer_name=None, os_version='Windows', json=False):
    """
    Generate fake event logs based on the provided inputs

        Args:
            count (int, optional): The number of logs to generate. Defaults to 1.
            computer_name (str, optional): A computer name to use when generating logs. Defaults to None.
            os_version (str, optional): The Operating System version to use when generating logs. Defaults to 'Windows'.
            json (bool, optional): Whether or not to convert to json:
        return data as JSON or XML. Defaults to False.

        Returns:
            list: Returns a list of generated Windows Event Logs
        
    """
    return socfaker.logs.windows.eventlog(count=count, computer_name=computer_name, os_version=os_version, json=json)

@general_bp.route("/logs/windows/sysmon", methods=['POST'])
def socfaker_sysmon_get(count=1):
    """
    Returns a list of generated sysmon logs

        Args:
            count (int, optional): The number of sysmon logs to return. Defaults to 21.

        Returns:
            list: A list of generated sysmon logs
        
    """
    return socfaker.logs.windows.sysmon(count=count)

### LOGS ROUTES ###
### NETWORK ROUTES ###

@general_bp.route("/network", methods=['GET'])
def socfaker_socfaker_network():
    """
    Access common generated network information

        Returns:
            Network: Returns an object with properties containing general
            or common network information
        
    """
    return ast.literal_eval(str(socfaker.network))

@general_bp.route("/network/get_cidr_range", methods=['POST'])
def socfaker_network_get_cidr_range(cidr):
    """
    Returns an IPv4 range

        Returns:
            str: Returns CIDR range for an IPv4 address.
        
    """
    return socfaker.network.get_cidr_range(cidr=cidr)

@general_bp.route("/network/ipv4", methods=['GET'])
def socfaker_network_ipv4():
    """
    Returns an IPv4 IP Address

        Returns:
            str: Returns an IPv4 Address.  If private the address will be 10.x.x.x or 172.x.x.x or 192.168.x.x.
        
    """
    return { 'value': socfaker.network.ipv4 }

@general_bp.route("/network/ipv6", methods=['GET'])
def socfaker_network_ipv6():
    """
    Returns an IPv6 IP Address

        Returns:
            dict: Returns a compressed and exploded IPv6 Address.
        
    """
    return { 'value': socfaker.network.ipv6 }

@general_bp.route("/network/netbios", methods=['GET'])
def socfaker_network_netbios():
    """
    Returns a netbios name

        Returns:
            str: Returns a random netbios name
        
    """
    return { 'value': socfaker.network.netbios }

@general_bp.route("/network/port", methods=['GET'])
def socfaker_network_port():
    """
    Returns a dictionary map of a port and it's common name

        Returns:
            dict: A random port and it's common name
        
    """
    return socfaker.network.port

@general_bp.route("/network/protocol", methods=['GET'])
def socfaker_network_protocol():
    """
    Random network protocol

        Returns:
            dict: Returns a random network protocol and protocol number
        
    """
    return socfaker.network.protocol

### NETWORK ROUTES ###
### OPERATING_SYSTEM ROUTES ###

@general_bp.route("/operating_system", methods=['GET'])
def socfaker_socfaker_operating_system():
    """
    Fake operating system information

        Returns:
            OperatingSystem: Returns an object with properties containing
            Operating System information
        
    """
    return ast.literal_eval(str(socfaker.operating_system))

@general_bp.route("/operating_system/family", methods=['GET'])
def socfaker_operatingsystem_family():
    """
    The operating system family

        Returns:
            str: Returns a random operating system family
        
    """
    return { 'value': socfaker.operating_system.family }

@general_bp.route("/operating_system/fullname", methods=['GET'])
def socfaker_operatingsystem_fullname():
    """
    The operating system full name

        Returns:
            str: Returns a random operating system full name including name, type and version
        
    """
    return { 'value': socfaker.operating_system.fullname }

@general_bp.route("/operating_system/name", methods=['GET'])
def socfaker_operatingsystem_name():
    """
    The operating system name

        Returns:
            str: Returns a random operating system name
        
    """
    return { 'value': socfaker.operating_system.name }

@general_bp.route("/operating_system/version", methods=['GET'])
def socfaker_operatingsystem_version():
    """
    The operating system version

        Returns:
            str: Returns a random operating system version
        
    """
    return { 'value': socfaker.operating_system.version }

### OPERATING_SYSTEM ROUTES ###
### ORGANIZATION ROUTES ###

@general_bp.route("/organization", methods=['GET'])
def socfaker_socfaker_organization():
    """
    Fake organization information

        Returns:
            Organization: Returns an object with properties containing common
            organization information
        
    """
    return ast.literal_eval(str(socfaker.organization))

@general_bp.route("/organization/division", methods=['GET'])
def socfaker_organization_division():
    """
    Returns a division within an organization

        Returns:
            str: Returns a division within an organization
        
    """
    return { 'value': socfaker.organization.division }

@general_bp.route("/organization/domain", methods=['GET'])
def socfaker_organization_domain():
    """
    Returns a domain name based on the organization name

        Returns:
            str: Returns a domain name based on the organizational name
        
    """
    return { 'value': socfaker.organization.domain }

@general_bp.route("/organization/name", methods=['GET'])
def socfaker_organization_name():
    """
    A randomly generated organization name

        Returns:
            str: A randomly generated organization name
        
    """
    return { 'value': socfaker.organization.name }

@general_bp.route("/organization/title", methods=['GET'])
def socfaker_organization_title():
    """
    Returns a title within an organization

        Returns:
            str: Returns a title within an organization
        
    """
    return { 'value': socfaker.organization.title }

### ORGANIZATION ROUTES ###
### PCAP ROUTES ###

@general_bp.route("/pcap", methods=['POST'])
def socfaker_pcap_generate(count=1, port=9600):
    """
    None
    """
    return socfaker.pcap(count=count)

### PCAP ROUTES ###
### REGISTRY ROUTES ###

@general_bp.route("/registry", methods=['GET'])
def socfaker_socfaker_registry():
    """
    Fake registry information

        Returns:
            Registry: Returns an object with properties containing
            common Windows registry information
        
    """
    return ast.literal_eval(str(socfaker.registry))

@general_bp.route("/registry/hive", methods=['GET'])
def socfaker_registry_hive():
    """
    A random registry hive

        Returns:
            str: Returns a random registry hive
        
    """
    return { 'value': socfaker.registry.hive }

@general_bp.route("/registry/key", methods=['GET'])
def socfaker_registry_key():
    """
    A random registry key

        Returns:
            str: Returns a random registry key
        
    """
    return { 'value': socfaker.registry.key }

@general_bp.route("/registry/path", methods=['GET'])
def socfaker_registry_path():
    """
    A full registry path
        
        Returns:
            str: Returns a random full registry path
        
    """
    return { 'value': socfaker.registry.path }

@general_bp.route("/registry/root", methods=['GET'])
def socfaker_registry_root():
    """
    A random registry root path string

        Returns:
            str: Returns a random registry root path string
        
    """
    return { 'value': socfaker.registry.root }

@general_bp.route("/registry/type", methods=['GET'])
def socfaker_registry_type():
    """
    A random registry key type

        Returns:
            str: A random registry key type
        
    """
    return { 'value': socfaker.registry.type }

@general_bp.route("/registry/value", methods=['GET'])
def socfaker_registry_value():
    """
    A random registry key value

        Returns:
            str: A random registry key value
        
    """
    return { 'value': socfaker.registry.value }

### REGISTRY ROUTES ###
### TIMESTAMP ROUTES ###

@general_bp.route("/timestamp", methods=['GET'])
def socfaker_socfaker_timestamp():
    """
    Fake timestamp information

        Returns:
            Timestamp: Returns an object with methods to generate fake
            timestamps
        
    """
    return ast.literal_eval(str(socfaker.timestamp))

@general_bp.route("/timestamp/date_string", methods=['POST'])
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
    return {'value': socfaker.timestamp.date_string(years=years, months=months, days=days) }

@general_bp.route("/timestamp/in_the_future", methods=['POST'])
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
    return {'value': socfaker.timestamp.in_the_future(years=years, months=months, days=days, hours=hours, minutes=minutes, seconds=seconds) }

@general_bp.route("/timestamp/in_the_past", methods=['POST'])
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
    return {'value': socfaker.timestamp.in_the_past(years=years, months=months, days=days, hours=hours, minutes=minutes, seconds=seconds) }

@general_bp.route("/timestamp/current", methods=['GET'])
def socfaker_timestamp_current():
    """
    The current timestamp

        Returns:
            str: Returns the current timestamp in ISO 8601 format
        
    """
    return { 'value': socfaker.timestamp.current }


### TIMESTAMP ROUTES ###
### USER_AGENT ROUTES ###

@general_bp.route("/user_agent", methods=['GET'])
def socfaker_socfaker_user_agent():
    """
    Fake user agent information

        Returns:
            UserAgent: Returns an object with methods to generate fake
            user agent strings
        
    """
    return {'value': socfaker.user_agent }

### USER_AGENT ROUTES ###
### VULNERABILITY ROUTES ###


@general_bp.route("/vulnerability/critical", methods=['GET'])
def socfaker_vulnerability_critical():
    """
    Returns a list of critical vulnerabilities based on counts provided when instantiating the class

        Returns:
            list: Returns a list of critical vulnerabilities
        
    """
    return socfaker.vulnerability().critical

@general_bp.route("/vulnerability/data", methods=['GET'])
def socfaker_vulnerability_data():
    """
    Returns all vulnerability data

        Returns:
            json: Returns json of all vulnerability data
        
    """
    return socfaker.vulnerability().data

@general_bp.route("/vulnerability/high", methods=['GET'])
def socfaker_vulnerability_high():
    """
    Returns a list of high vulnerabilities based on counts provided when instantiating the class

        Returns:
            list: Returns a list of high vulnerabilities
        
    """
    return socfaker.vulnerability().high


@general_bp.route("/vulnerability/informational", methods=['GET'])
def socfaker_vulnerability_informational():
    """
    Returns a list of informational vulnerabilities based on counts provided when instantiating the class

        Returns:
            list: Returns a list of informational vulnerabilities
        
    """
    return socfaker.vulnerability().informational

@general_bp.route("/vulnerability/low", methods=['GET'])
def socfaker_vulnerability_low():
    """
    Returns a list of low vulnerabilities based on counts provided when instantiating the class

        Returns:
            list: Returns a list of low vulnerabilities
        
    """
    return socfaker.vulnerability().low

@general_bp.route("/vulnerability/medium", methods=['GET'])
def socfaker_vulnerability_medium():
    """
    Returns a list of medium vulnerabilities based on counts provided when instantiating the class

        Returns:
            list: Returns a list of medium vulnerabilities
        
    """
    return socfaker.vulnerability().medium

@general_bp.route("/vulnerability/host", methods=['GET'])
def socfaker_vulnerability_host():
    """
    Retrieve information about hosts found in a vulnerability scan

        Returns:
            VulnerabilityHost: Returns an object with properties for a vulnerable host
        
    """
    return socfaker.vulnerability().host

@general_bp.route("/vulnerability/host/checks_considered", methods=['GET'])
def socfaker_vulnerabilityhost_checks_considered():
    """
    A count of how many vulnerability checks were considered for a host

        Returns:
            int: Returns a randomly integer for checks considered during a vulnerability scan
        
    """
    return { 'value': socfaker.vulnerability().host.checks_considered }

@general_bp.route("/vulnerability/host/critical", methods=['GET'])
def socfaker_vulnerabilityhost_critical():
    """
    Returns a list of critical vulnerabilities based on counts provided when instantiating the class

        Returns:
            list: Returns a list of critical vulnerabilities
        
    """
    return socfaker.vulnerability().host.critical

@general_bp.route("/vulnerability/host/data", methods=['GET'])
def socfaker_vulnerabilityhost_data():
    """
    Returns all vulnerability data

        Returns:
            json: Returns json of all vulnerability data
        
    """
    return socfaker.vulnerability().host.data

@general_bp.route("/vulnerability/host/fqdn", methods=['GET'])
def socfaker_vulnerabilityhost_fqdn():
    """
    A host FQDN

        Returns:
            str: Returns a randomly generated DNS name
        
    """
    return { 'value': socfaker.vulnerability().host.fqdn }

@general_bp.route("/vulnerability/host/high", methods=['GET'])
def socfaker_vulnerabilityhost_high():
    """
    Returns a list of high vulnerabilities based on counts provided when instantiating the class

        Returns:
            list: Returns a list of high vulnerabilities
        
    """
    return socfaker.vulnerability().host.high

@general_bp.route("/vulnerability/host/host", methods=['GET'])
def socfaker_vulnerabilityhost_host():
    """
    Retrieve information about hosts found in a vulnerability scan

        Returns:
            VulnerabilityHost: Returns an object with properties for a vulnerable host
        
    """
    return socfaker.vulnerability().host.host

@general_bp.route("/vulnerability/host/host_id", methods=['GET'])
def socfaker_vulnerabilityhost_host_id():
    """
    Returns a random host ID

        Returns:
            int: Returns a random host ID
        
    """
    return { 'value': socfaker.vulnerability().host.host_id }

@general_bp.route("/vulnerability/host/informational", methods=['GET'])
def socfaker_vulnerabilityhost_informational():
    """
    Returns a list of informational vulnerabilities based on counts provided when instantiating the class

        Returns:
            list: Returns a list of informational vulnerabilities
        
    """
    return socfaker.vulnerability().host.informational

@general_bp.route("/vulnerability/host/low", methods=['GET'])
def socfaker_vulnerabilityhost_low():
    """
    Returns a list of low vulnerabilities based on counts provided when instantiating the class

        Returns:
            list: Returns a list of low vulnerabilities
        
    """
    return socfaker.vulnerability().host.low

@general_bp.route("/vulnerability/host/mac_address", methods=['GET'])
def socfaker_vulnerabilityhost_mac_address():
    """
    A host MAC Address

        Returns:
            str: Returns a randomly generated MAC Address
        
    """
    return { 'value': socfaker.vulnerability().host.mac_address }

@general_bp.route("/vulnerability/host/medium", methods=['GET'])
def socfaker_vulnerabilityhost_medium():
    """
    Returns a list of medium vulnerabilities based on counts provided when instantiating the class

        Returns:
            list: Returns a list of medium vulnerabilities
        
    """
    return socfaker.vulnerability().host.medium

@general_bp.route("/vulnerability/host/name", methods=['GET'])
def socfaker_vulnerabilityhost_name():
    """
    Returns a computer name

        Returns:
            str: Returns a randomly generated computer name
        
    """
    return { 'value': socfaker.vulnerability().host.name }

@general_bp.route("/vulnerability/host/percentage", methods=['GET'])
def socfaker_vulnerabilityhost_percentage():
    """
    Returns a percentage of vulnerabilities found on a host

        Returns:
            dict: Returns a percentage of vulnerabilities found on a host
        
    """
    return {'value': socfaker.vulnerability().host.percentage }

@general_bp.route("/vulnerability/host/scan", methods=['GET'])
def socfaker_vulnerabilityhost_scan():
    """
    A vulnerability scan

        Returns:
            VulnerabilityScan: Returns a vulnerability scan object with properties related a vulnerability scan
        
    """
    return socfaker.vulnerability().host.scan

@general_bp.route("/vulnerability/host/total_score", methods=['GET'])
def socfaker_vulnerabilityhost_total_score():
    """
    The total score of a host during a vulnerability scan

        Returns:
            int: The total score for a host during a vulnerability scan
        
    """
    return { 'value': socfaker.vulnerability().host.total_score }

@general_bp.route("/vulnerability/scan", methods=['POST'])
def socfaker_vulnerability_scan(host_count=1, critical=1, high=1, medium=1, low=1, informational=1):
    return socfaker.vulnerability(host_count=host_count, critical=critical, high=high, medium=medium, low=low, informational=informational).scan

@general_bp.route("/vulnerability/scan/end_time", methods=['GET'])
def socfaker_vulnerabilityscan_end_time():
    """
    End time of a vulnerability scan

        Returns:
            str: The end time of a vulnerability scan in the future
        
    """
    return { 'value': socfaker.vulnerability().scan.end_time }

@general_bp.route("/vulnerability/scan/host_count", methods=['GET'])
def socfaker_vulnerabilityscan_host_count():
    """
    A vulnerability scan host count

        Returns:
            int: The provided vulnerability scan host count
        
    """
    return { 'value': socfaker.vulnerability().scan.host_count }

@general_bp.route("/vulnerability/scan/id", methods=['GET'])
def socfaker_vulnerabilityscan_id():
    """
    A vulnerability scan ID

        Returns:
            int: Returns a random vulnerability scan ID
        
    """
    return { 'value': socfaker.vulnerability().scan.id }

@general_bp.route("/vulnerability/scan/ip_list", methods=['GET'])
def socfaker_vulnerabilityscan_ip_list():
    """
    A list of host IPs during a Vulnerability scan

        Returns:
            list: A randomly generated list of host IPs during a vulnerability scan
        
    """
    return { 'value': socfaker.vulnerability().scan.ip_list }

@general_bp.route("/vulnerability/scan/name", methods=['GET'])
def socfaker_vulnerabilityscan_name():
    """
    A vulnerability scan name

        Returns:
            str: A randomly selected vulnerability scan name
        
    """
    return { 'value': socfaker.vulnerability().scan.name }

@general_bp.route("/vulnerability/scan/scan_uuid", methods=['GET'])
def socfaker_vulnerabilityscan_scan_uuid():
    """
    A vulnerability scan UUID

        Returns:
            str: A random UUID for a vulnerability scan
        
    """
    return { 'value': socfaker.vulnerability().scan.scan_uuid }

@general_bp.route("/vulnerability/scan/scanner_name", methods=['GET'])
def socfaker_vulnerabilityscan_scanner_name():
    """
    A vulnerability scaner name

        Returns:
            str: Returns a random vulnerability scanner name
        
    """
    return { 'value': socfaker.vulnerability().scan.scanner_name }

@general_bp.route("/vulnerability/scan/scanner_uuid", methods=['GET'])
def socfaker_vulnerabilityscan_scanner_uuid():
    """
    A vulnerability scanner UUID

        Returns:
            str: A random UUID for a scanner
        
    """
    return { 'value': socfaker.vulnerability().scan.scanner_uuid }

@general_bp.route("/vulnerability/scan/start_time", methods=['GET'])
def socfaker_vulnerabilityscan_start_time():
    """
    Start time of a vulnerability scan

        Returns:
            str: The start time of a vulnerability scan in the past
        
    """
    return { 'value': socfaker.vulnerability().scan.start_time }

@general_bp.route("/vulnerability/scan/status", methods=['GET'])
def socfaker_vulnerabilityscan_status():
    """
    Vulnerability scan status

        Returns:
            str: A randomly selected scan status
        
    """
    return { 'value': socfaker.vulnerability().scan.status }

@general_bp.route("/vulnerability/scan/type", methods=['GET'])
def socfaker_vulnerabilityscan_type():
    """
    The vulnerability scan type

        Returns:
            str: A randomly selected vulnerability scan type
        
    """
    return { 'value': socfaker.vulnerability().scan.type }

### VULNERABILITY ROUTES ###
### WORDS ROUTES ###

@general_bp.route("/words", methods=['GET'])
def socfaker_socfaker_words():
    """
    Used to create fake words or strings

        Returns:
            Words: Returns an object with methods to generate fake words and strings
        
    """
    return {'value': socfaker.words}

### WORDS ROUTES ###


### PRODUCT ROUTES ###

### PRODUCTS - AZURE - VM - DETAILS ###

@general_bp.route("/products/azure/details", methods=['GET'])
def socfaker_products_azure():
    """
    Azure class contains properties related to Azure products

        Returns:
            Azure: Microsoft Azure object containing properties and methods for generating data about Microsoft Azure products and services
        
    """
    return socfaker.products.azure.vm.details

@general_bp.route("/products/azure/vm/details/location", methods=['GET'])
def socfaker_azureproperties_location():
    """
    A location based on Microsoft Azure available locations

        Returns:
            str: Returns a Azure location
        
    """
    return { 'value': socfaker.products.azure.vm.details.location }

@general_bp.route("/products/azure/vm/details/network_zone", methods=['GET'])
def socfaker_azureproperties_network_zone():
    """
    Network zone type in Microsoft Azure

        Returns:
            str: Returns a random type for a network zone in Azure
        
    """
    return { 'value': socfaker.products.azure.vm.details.network_zone }

@general_bp.route("/products/azure/vm/details/resource_group_id", methods=['GET'])
def socfaker_azureproperties_resource_group_id():
    """
    Resource Group ID

        Returns:
            str: Returns a random resource group ID (GUID)
        
    """
    return { 'value': socfaker.products.azure.vm.details.resource_group_id }

@general_bp.route("/products/azure/vm/details/resource_group_name", methods=['GET'])
def socfaker_azureproperties_resource_group_name():
    """
    Resource Group Name in Azure

        Returns:
            str: Returns a three-word Resource Group name for Microsoft Azure
        
    """
    return { 'value': socfaker.products.azure.vm.details.resource_group_name }

@general_bp.route("/products/azure/vm/details/score", methods=['GET'])
def socfaker_azureproperties_score():
    """
    None
    """
    return { 'value': socfaker.products.azure.vm.details.score }

@general_bp.route("/products/azure/vm/details/vm_name", methods=['GET'])
def socfaker_azureproperties_vm_name():
    """
    A Azure VM Name

        Returns:
            str: Returns a random Azure VM name
        
    """
    return { 'value': socfaker.products.azure.vm.details.vm_name }

### PRODUCTS - AZURE - VM - DETAILS ###
### PRODUCTS - AZURE - VM - METRICS ###

@general_bp.route("/products/azure/vm/metrics", methods=['POST'])
def socfaker_azurevmmetrics_generate():
    """
    Returns a list of dicts containing Azure VM Metrics

        Returns:
            list: A list of dicts containing metrics for an Azure VM
        
    """
    return socfaker.products.azure.vm.metrics.generate()

@general_bp.route("/products/azure/vm/metrics/average", methods=['GET'])
def socfaker_azurevmmetrics_average():
    """
    None
    """
    return { 'value': socfaker.products.azure.vm.metrics.average }

@general_bp.route("/products/azure/vm/metrics/graphs", methods=['GET'])
def socfaker_azurevmmetrics_graphs():
    """
    None
    """
    return { 'value': socfaker.products.azure.vm.metrics.graphs }

### PRODUCTS - AZURE - VM - METRICS ###
### PRODUCTS - AZURE - VM - TOPOLOGY ###

@general_bp.route("/products/azure/vm/topology", methods=['GET'])
def socfaker_azurevmtopology_get():
    """
    None
    """
    return socfaker.products.azure.vm.topology

### PRODUCTS - AZURE - VM - TOPOLOGY ###
### PRODUCTS - ELASTIC ###

@general_bp.route("/products/elastic", methods=['GET'])
def socfaker_products_elastic():
    """
    Elastic class contains properties related to Elastic products

        Returns:
            Elastic: Elastic object containing properties and methods for generating data about Elastic products and services
        
    """
    return { 'value': socfaker.products.elastic }

@general_bp.route("/products/elastic/document", methods=['POST'])
def socfaker_elasticecs_get(count=1):
    """
    Generates one or more Elastic Common Schema documents

        Args:
            count (int, optional): The number of documents you want 
                                   generated. Defaults to 1.

        Returns:
            list: A list of ECS Document dictionaries
        
    """
    return socfaker.products.elastic.document.get(count=count)

@general_bp.route("/products/elastic/document/fields/agent", methods=['GET'])
def socfaker_elasticecsfields_agent():
    """
    Returns an ECS agent dictionary

        Returns:
            dict: Returns a dictionary of agent
                  fields/properties
        
    """
    return socfaker.products.elastic.document.fields.agent

@general_bp.route("/products/elastic/document/fields/base", methods=['GET'])
def socfaker_elasticecsfields_base():
    """
    Returns an ECS base fields dictionary

        Returns:
            dict: Returns a dictionary of ECS base
                  fields/properties
        
    """
    return socfaker.products.elastic.document.fields.base

@general_bp.route("/products/elastic/document/fields/client", methods=['GET'])
def socfaker_elasticecsfields_client():
    """
    Returns an ECS Client dictionary

        Returns:
            dict: Returns a dictionary of ECS 
                  client fields/properties
        
    """
    return socfaker.products.elastic.document.fields.client

@general_bp.route("/products/elastic/document/fields/cloud", methods=['GET'])
def socfaker_elasticecsfields_cloud():
    """
    Returns an ECS Cloud dictionary

        Returns:
            dict: Returns a dictionary of ECS 
                  Cloud fields/properties
        
    """
    return socfaker.products.elastic.document.fields.cloud

@general_bp.route("/products/elastic/document/fields/code_signature", methods=['GET'])
def socfaker_elasticecsfields_code_signature():
    """
    Returns an ECS Code Signature dictionary

        Returns:
            dict: Returns a dictionary of ECS 
                  Code Signature fields/properties
        
    """
    return socfaker.products.elastic.document.fields.code_signature

@general_bp.route("/products/elastic/document/fields/container", methods=['GET'])
def socfaker_elasticecsfields_container():
    """
    Returns an ECS container dictionary

        Returns:
            dict: Returns a dictionary of ECS 
                  container fields/properties
        
    """
    return socfaker.products.elastic.document.fields.container

@general_bp.route("/products/elastic/document/fields/destination", methods=['GET'])
def socfaker_elasticecsfields_destination():
    """
    Returns an ECS destination dictionary

        Returns:
            dict: Returns a dictionary of ECS 
                  destination fields/properties
        
    """
    return socfaker.products.elastic.document.fields.destination

@general_bp.route("/products/elastic/document/fields/dll", methods=['GET'])
def socfaker_elasticecsfields_dll():
    """
    Returns an ECS DLL dictionary

        Returns:
            dict: Returns a dictionary of ECS 
                  DLL fields/properties
        
    """
    return socfaker.products.elastic.document.fields.dll

@general_bp.route("/products/elastic/document/fields/dns", methods=['GET'])
def socfaker_elasticecsfields_dns():
    """
    Returns an ECS DNS dictionary

        Returns:
            dict: Returns a dictionary of ECS 
                  DNS fields/properties
        
    """
    return socfaker.products.elastic.document.fields.dns

@general_bp.route("/products/elastic/document/fields/event", methods=['GET'])
def socfaker_elasticecsfields_event():
    """
    Returns an ECS Event dictionary

        Returns:
            dict: Returns a dictionary of ECS 
                  Event fields/properties
        
    """
    return socfaker.products.elastic.document.fields.event

@general_bp.route("/products/elastic/document/fields/file", methods=['GET'])
def socfaker_elasticecsfields_file():
    """
    Returns an ECS file dictionary

        Returns:
            dict: Returns a dictionary of ECS 
                  file fields/properties
        
    """
    return socfaker.products.elastic.document.fields.file

@general_bp.route("/products/elastic/document/fields/host", methods=['GET'])
def socfaker_elasticecsfields_host():
    """
    Returns an ECS host dictionary

        Returns:
            dict: Returns a dictionary of ECS 
                  host fields/properties
        
    """
    return socfaker.products.elastic.document.fields.host

@general_bp.route("/products/elastic/document/fields/http", methods=['GET'])
def socfaker_elasticecsfields_http():
    """
    Returns an ECS HTTP dictionary

        Returns:
            dict: Returns a dictionary of ECS 
                  HTTP fields/properties
        
    """
    return socfaker.products.elastic.document.fields.http

@general_bp.route("/products/elastic/document/fields/network", methods=['GET'])
def socfaker_elasticecsfields_network():
    """
    Returns an ECS network dictionary

        Returns:
            dict: Returns a dictionary of ECS 
                  network fields/properties
        
    """
    return socfaker.products.elastic.document.fields.network

@general_bp.route("/products/elastic/document/fields/organization", methods=['GET'])
def socfaker_elasticecsfields_organization():
    """
    Returns an ECS Organization dictionary

        Returns:
            dict: Returns a dictionary of ECS 
                  organization fields/properties
        
    """
    return socfaker.products.elastic.document.fields.organization

@general_bp.route("/products/elastic/document/fields/package", methods=['GET'])
def socfaker_elasticecsfields_package():
    """
    Returns an ECS package dictionary

        Returns:
            dict: Returns a dictionary of ECS 
                  package fields/properties
        
    """
    return socfaker.products.elastic.document.fields.package

@general_bp.route("/products/elastic/document/fields/registry", methods=['GET'])
def socfaker_elasticecsfields_registry():
    """
    Returns an ECS Windows Registry dictionary

        Returns:
            dict: Returns a dictionary of ECS 
                  Windows Registry fields/properties
        
    """
    return socfaker.products.elastic.document.fields.registry

@general_bp.route("/products/elastic/document/fields/server", methods=['GET'])
def socfaker_elasticecsfields_server():
    """
    Returns an ECS server dictionary

        Returns:
            dict: Returns a dictionary of ECS 
                  server fields/properties
        
    """
    return socfaker.products.elastic.document.fields.server

@general_bp.route("/products/elastic/document/fields/source", methods=['GET'])
def socfaker_elasticecsfields_source():
    """
    Returns an ECS source dictionary

        Returns:
            dict: Returns a dictionary of ECS 
                  source fields/properties
        
    """
    return socfaker.products.elastic.document.fields.source

@general_bp.route("/products/elastic/hits", methods=['POST'])
def socfaker_elastic_hits(count=10):
    """
    Returns a provided count of generated / fake Elasticsearch query hits.  Default is 10.

        Args:
            count (int, optional): The number of Elasticsearch query hits returned in a list. Defaults to 10.

        Returns:
            list: A list of Elasticsearch query hits
        
    """
    return socfaker.products.elastic.hits(count=count)

### PRODUCTS - ELASTIC ###
### PRODUCTS - QUALYSGUARD ###

@general_bp.route("/products/qualysguard/scan", methods=['POST'])
def socfaker_qualysguard_scan(count=1, host_count=1):
    """
    Retrieve 1 or more QualysGuard VM scans for 1 or more hosts

        Args:
            count (int, optional): The number of scans to return. Defaults to 1.
            host_count (int, optional): The number of hosts within a scan. Defaults to 1.

        Returns:
            list: Returns a list of scans based on the provided inputs
        
    """
    return socfaker.products.qualysguard.scan(count=count, host_count=host_count)

### PRODUCTS - QUALYSGUARD ###
### PRODUCTS - SERVICENOW ###

@general_bp.route("/products/servicenow/search", methods=['POST'])
def socfaker_servicenow_search(random_keyword=None):
    """
    Generates a fake response from a ServiceNow Incident Search

        Args:
            random_keyword (str, optional): Adds a random keyword string you provide to fields within the generated response object. Defaults to None.

        Returns:
            dict: A ServiceNow Incident Search response object
        
    """
    return socfaker.products.servicenow.search(random_keyword=random_keyword)
