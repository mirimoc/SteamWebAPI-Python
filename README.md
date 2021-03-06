SteamWebAPI-Python
==================

A class-based wrapper for the Steam Community Web API. Each class is the "interface" provided by the Steam Web API which contains the methods within the interface.

**NOTE**:

    The dev branch is undergoing rapid development.
    Please be aware that we have not finalized any classes, methods, or functions outside
    of the interfaces/methods that Valve provides.

    Until there is a release or tagged version of this package, all contents may be
    unstable. We certainly welcome your feedback during this time, and encourage you to
    not only follow the project, but report issues and submit feedback.

settings.py:
------------
* STEAM_API_KEY

  Your Steam API Key as requested from https://steamcommunity.com/login/home/?goto=%2Fdev%2Fapikey

* DEFAULT_LANGUAGE

  If no language argument is provided to a method requesting one, this language will automatically be provided.

core.py:
------------
Contains the class APIQuery, which is a utility class for returning data in either raw JSON, XML, or VDF format as queried from urllib2.urlopen(API_URL) via any interface method. Example usage:

    from steam_api.user import ISteamUser

    # Create an instance of ISteamUser
    iSteamUser = ISteamUser()

    # Using the APIQuery methods
    return_xml = iSteamUser.GetFriendList(steamid).as_xml()
    return_json = iSteamUser.GetFriendList(steamid).as_json()
    return_vdf = iSteamUser.GetFriendList(steamid).as_vdf()

    # Using the APIQuery properties
    return_xml = iSteamUser.GetFriendList(steamid).xml
    return_json = iSteamUser.GetFriendList(steamid).json
    return_vdf = iSteamUser.GetFriendList(steamid).vdf

    # Print the URL for the base API Query
    iSteamUser.GetFriendList(steamid).url

    # Print the URL for the XML API Query
    iSteamUser.GetFriendList(steamid).as_xml().url

### ../games/710/items.py:
Contains game-specific interfaces for Valve's Development Version of Counter-Strike: Global Offensive:
```python
# Getting and granting promo items using interface ITFPromos_710
ITFPromos = ITFPromos_710()
ITFPromos.GetItemID(steamid, promoid)
ITFPromos.GrantItem(steamid, promoid)

# Getting economy items and schema using interface IEconItems_710
iEconItems = IEconItems_710()
iEconItems.GetPlayerItems(steamid)
iEconItems.GetSchema(language='')
```

### ../games/csgo/items.py:
Contains game-specific interfaces for Counter-Strike: Global Offensive:
```python
# Getting and granting promo items using interface ITFPromos_730
ITFPromos = ITFPromos_730()
ITFPromos.GetItemID(steamid, promoid)
ITFPromos.GrantItem(steamid, promoid)

# Getting economy items and schema using interface IEconItems_730
iEconItems = IEconItems_730()
iEconItems.GetPlayerItems(steamid)
iEconItems.GetSchema(language='')
```

### ../games/css_beta/items.py:
Contains game-specific interfaces for Counter-Strike: Source Beta:
```python
# Getting and granting promo items using interface ITFPromos_260
ITFPromos = ITFPromos_260()
ITFPromos.GetItemID(steamid, promoid)
ITFPromos.GrantItem(steamid, promoid)

# Getting economy items and schema using interface IEconItems_260
iEconItems = IEconItems_260()
iEconItems.GetPlayerItems(steamid)
iEconItems.GetSchema(language='')
```

### ../games/dota2/gameclient.py
```python
# Getting game client information using interface IGCVersion_570
IGCVersion = IGCVersion_570()
IGCVersion.GetClientVersion()
IGCVersion.GetClusterVersion()
IGCVersion.GetServerVersion()
```

### ../games/dota2/items.py
```python
# Getting economy information using the interface IEconDOTA2_570
iEconDota2 = IEconDOTA2_570()
iEconDota2.GetHeroes(itemizedonly, language='')
iEconDota2.GetRarities(language='')
iEconDota2.GetStoreSections(language='')
iEconDota2.GetTicketSaleStatus()

# Getting and granting promo items using interface ITFPromos_570
ITFPromos = ITFPromos_570()
ITFPromos.GetItemID(steamid, promoid)
ITFPromos.GrantItem(steamid, promoid)

# Getting economy information using the interface IEconItems_570
iEconItems = IEconItems_570()
iEconItems.GetPlayerItems(steamid)
iEconItems.GetSchema(language='')
iEconItems.GetStoreStatus()
```

### ../games/dota2/match.py
```python
# Getting match information using the interface IDOTA2Match_570
iDota2Match = IDOTA2Match_570()
iDota2Match.GetMatchDetails(match_id)
iDota2Match.GetMatchHistory(player_name=None, hero_id=None, game_mode=None,skill=None,
                            date_min=None, date_max=None, min_players=None,
                            account_id=None, league_id=None, start_at_match_id=None,
                            matches_requested=None, tournament_games_only=None)
```

../games/< game name | id >/*.*
-----------------------------
* ../games/dota2_test/gameclient.py
* ../games/dota2_test/items.py
* ../games/dota2_test/match.py
* ../games/portal2/items.py
* ../games/portal2/leaderboards.py
* ../games/tf2/gameclient.py
* ../games/tf2/items.py
* ../games/tf2_beta/gameclient.py
* ../games/tf2_beta/items.py
