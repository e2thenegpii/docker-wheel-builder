def os_release_parser():
    with open('/etc/os-release', 'r') as fs:
        return {k.lower(): v.strip().strip('"') for k, v in (line.split('=', 1) for line in fs)}
            
class os_release:
    '''Parses the /etc/os-release file'''
    
    def __init__(self):
        self._name = None
        self._version = None
        self._id = None
        self._id_like = None
        self._version_codename = None
        self._version_id = None
        self._pretty_name = None
        self._ansi_color = None
        self._cpe_name = None
        self._home_url = None
        self._documentation_url = None
        self._support_url = None
        self._bug_report_url = None
        self._privacy_policy_url = None
        self._build_id = None
        self._variant = None
        self._variant_id = None
        self._logo = None
        self._vendor_extra = {}

        for option, value in os_release_parser():
            if hasattr(self, option):
                setattr(self, '_' + option, value)
            else:
                self._vendor_extra[option] = value
        
    @property
    def name(self):
        return self._name

    @property
    def version(self):
        return self._version

    @property
    def id(self):
        return self._id

    @property
    def id_like(self):
        return self._id_like

    @property
    def version_codename(self):
        return self._version_codename

    @property
    def version_id(self):
        return self._version_id

    @property
    def pretty_name(self):
        return self._pretty_name

    @property
    def ansi_color(self):
        return self._ansi_color

    @property
    def cpe_name(self):
        return self._cpe_name

    @property
    def home_url(self):
        return self._home_url

    @property
    def documentation_url(self):
        return self._documentation_url

    @property
    def support_url(self):
        return self._support_url

    @property
    def bug_report_url(self):
        return self._bug_report_url
    
    @property
    def privacy_policy_url(self):
        return self._privacy_policy_url

    @property
    def build_id(self):
        return self._build_id

    @property
    def variant(self):
        return self._variant

    @property
    def variant_id(self):
        return self._variant_id

    @property
    def logo(self):
        return self._logo

    @property
    def vendor_extra(self):
        '''Get a dictionary of vendor specific strings'''
        return self._vendor_extra
