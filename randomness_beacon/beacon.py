import sys
import os
import urllib
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

BASE_URL = "https://beacon.nist.gov/rest/record/"

SAMPLE_DATA = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><record><version>Version 1.0</version><frequency>60</frequency><timeStamp>1380418860</timeStamp><seedValue>A6E5D599A128A1000EBD71B20EA441E22CC1005058F9656A976380C0FCD88518B7B827015AAF18730109A089C9EFF05A5DF7A74C392B78D561FD271B895EFC81</seedValue><previousOutputValue>D5C3D61EB3C08A3B17AB340F8FFABEAD76A3322AC5F90259EDFBF9A40351CC356AE1D0C9B3888CB8D8FD3C3934B4FF903BD0A1406A06DAB4770DFCD0FDF8A8DE</previousOutputValue><signatureValue>AF6A76BCE8592020E2DCB2CDF1EB6B2966C82FB1F5FCD1F08EC572BBA704CA04260D06037574B6AED4AFF6749965FF3B684EE392553A14702A9EC98FB7F6AC8E93A83B167130AE0D3D199C9DAD92A0F46ECB9DC56D28101068ABD4FF36CC9629681073C9EC0DC3948EE32D89CE7E2EB04A27704C29216F2FD79A9C120B6186DA9A1CC4A2323995F2E3AA7B1AD8BF794C4C4AAEA89BE53F3B5B29F787765ECBB0FA94E1195027C4E1C62331E4B585F2DDDBF244321FB3C27A82E1C98A0B92167DDEB7F49ACF9E7B8DD296CB1597FC7A0726597783A1808B0C158C08B6F25AEE21E7ACF967F476F49F13D2DE81348B4FDE59629A30B8BEE35F30F0A86156E99F9A</signatureValue><outputValue>9481F1348C9A313E5BB387BCAB6290B224F476BACC509511A3D36D1D1089470B7846EC947A63EF71F6A36ED4304252F51BB233ADDB9489C718D9BA9FAD03C463</outputValue><statusCode>0</statusCode></record>'

class BeaconError(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)

class Beacon(object):

    def __init__(self):
        self.last_timestamp = None

    def current_record(self, timestamp=None):
        if not timestamp:
            timestamp = self.last_timestamp

        if not timestamp:
            raise BeaconError("No timestamp specified")

        url = BASE_URL + timestamp
        return self._call(url)


    def previous_record(self, timestamp=None):
        if not timestamp:
            timestamp = self.last_timestamp

        if not timestamp:
            raise BeaconError("No timestamp specified")

        url = BASE_URL + "previous/" + timestamp
        return self._call(url)

    def next_record(self, timestamp=None):
        if not timestamp:
            timestamp = self.last_timestamp

        if not timestamp:
            raise BeaconError("No timestamp specified")

        url = BASE_URL + "next/" + timestamp
        return self._call(url)

    def last_record(self):
        url = BASE_URL + "last"
        return self._call(url)

    def start_chain_record(self, timestamp=None):
        url = BASE_URL + "start-chain/" + timestamp

    def _call(self, url):
        u = urllib.urlopen(url)
        result = u.read()
        #result = SAMPLE_DATA
        data = {}
        record = ET.fromstring(result)
        for child in record:
            data[child.tag] = child.text

        self.last_timestamp = data.get('timeStamp', None)

        return data


if __name__ == '__main__':
    b = Beacon()
    print b.current_record('1380418860')
