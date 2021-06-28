from helpers.utils import properties_helper


class Base:

    def __init__(self):
        props = properties_helper.read_properties()
        self.url = props.get('environment', 'url')
        print('Testcases will be run against - ' + self.url)