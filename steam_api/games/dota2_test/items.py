# =============================================================================
# >> IMPORTS
# =============================================================================
# API Imports
from steam_api.api_base import SteamWebAPI


# =============================================================================
# >> CLASSES
# =============================================================================
class IEconDOTA2_205790(SteamWebAPI):
    def __init__(self):
        self.interface = 'IEconDOTA2_205790'
        super(IEconDOTA2_205790, self).__init__()

    def GetHeroes(self, itemizedonly, language=''):
        params = {
            'language': language,
            'itemizedonly': bool(itemizedonly),
            }
        return self.generate_api_url(self.interface, 'GetHeroes', 1,
            params, key=True)

    def GetRarities(self, language=''):
        params = {
            'language': language,
            }
        return self.generate_api_url(self.interface, 'GetRarities', 1,
            params, key=True)

    def GetTicketSaleStatus(self):
        params = {}
        return self.generate_api_url(self.interface, 'GetTicketSaleStatus', 1,
            params, key=True)


class ITFPromos_205790(SteamWebAPI):
    def __init__(self):
        self.interface = 'ITFPromos_205790'
        super(ITFPromos_205790, self).__init__()

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


class IEconItems_205790(SteamWebAPI):
    def __init__(self):
        self.interface = 'IEconItems_205790'
        super(IEconItems_205790, self).__init__()

    def GetPlayerItems(self, steamid):
        params = {
            'steamid': steamid,
            }
        return self.generate_api_url(self.interface, 'GetPlayerItems', 1,
            params, key=True)

    def GetSchema(self, language=''):
        params = {
            'language': language,
            }
        return self.generate_api_url(self.interface, 'GetSchema', 1,
            params, key=True)

    def GetSchemaURL(self):
        params = {}
        return self.generate_api_url(self.interface, 'GetSchemaURL', 1,
            params, key=True)

    def GetStoreMetaData(self, language=''):
        params = {
            'language': language,
            }
        return self.generate_api_url(self.interface, 'GetStoreMetaData', 1,
            params, key=True)

    def GetStoreStatus(self):
        params = {}
        return self.generate_api_url(self.interface, 'GetStoreStatus', 1,
            params, key=True)
