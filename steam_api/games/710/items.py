

class ITFPromos_710(SteamWebAPI):
    def __init__(self):
        self.interface = 'ITFPromos_710'
        super(ITFPromos_710, self).__init__()

    def GetItemID(self, steamid, promoid):
        params = {
            'steamid': steamid,
            'PromoID': promoid,
            }
        return self.generate_api_url(self.interface, 'GetItemID', 1,
            params, key=True)

    def GrantItem(self, steamid, promoid):
        params = {
            'steamid': steamid,
            'PromoID': promoid,
            }
        return self.generate_api_url(self.interface, 'GrantItem', 1,
            params, key=True)


class IEconItems_710(SteamWebAPI):
    def __init__(self):
        self.interface = 'IEconItems_710'
        super(IEconItems_710, self).__init__()

    def GetPlayerItems(self, steamid):
        params = {
            'steamid': steamid,
            }
        return self.generate_api_url(self.interface, 'GetPlayerItems', 1,
            params, key=True)

    def GetSchema(self, language='en'):
        params = {
            'language': language,
            }
        return self.generate_api_url(self.interface, 'GetSchema', 1,
            params, key=True)
