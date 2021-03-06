from adapters.base_adapter import Adapter
import urllib.parse

class OnOffSwitchAdapter(Adapter):

    def __init__(self):
        Adapter.__init__(self)

    def handleMqttMessage(self, device, data, action, domoticz_port):
        if data == '1':
            command = 'On'
        else:
            command = 'Off'

        params = {
            'param': self.getParamType(),
            'idx': device['idx'],
            'switchcmd': command
        }
        Adapter.callDomoticzApi(self, domoticz_port, urllib.parse.urlencode(params))

    def getBridgeType(self, device):
        if ('TypeImg' in device and (device['TypeImg'] == 'lightbulb' or device['TypeImg'] == 'dimmer')) \
                and 'Image' in device and device['Image'] == 'Light':
            # Light
            return 1
        # Switch
        return 3

    def getParamType(self):
        return 'switchlight'

    def getTraits(self):
        return [1]