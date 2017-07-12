import pycaching
from geotogpx import createGPX

def main():
    url = input("URL: ")
    cacheurl = url
    cachegccode = url.split("/")[4].split("_")[0]

    geocaching = pycaching.login("USERNAME", "PASSWORD")
    cache = geocaching.get_cache(cachegccode)
    cachecreator = cache.author

    lat = str(cache.lat)
    lon = str(cache.lon)
    cachename = str(cache.name)
    cacheid = str(cache.id)
    cachetype = str(str(cache.type).split(".")[1].title())
    cachedifficulty = str(cache.difficulty)
    if cachedifficulty.split(".")[1] == "0":
        cachedifficulty = cachedifficulty.split(".")[0]
    cachecontainer = str(str(cache.size).split(".")[1].title())
    cacheterrain = str(cache.terrain)
    if cacheterrain.split(".")[1] == "0":
        cacheterrain = cacheterrain.split(".")[0]
    country = str(cache.country)
    state = str(cache.stateprovince)
    longdesc = str(cache.description)
    shortdesc = str(cache.summary)
    hints = str(cache.hint)

    createGPX(cachecreator, "", "", "", lat, lon, cachegccode, cachename, cacheid, cachetype, cachedifficulty, cachecontainer, cacheterrain, country, state, longdesc, shortdesc, hints, cacheurl)

    resp = input("Another? (Y/N): ")

    resp = resp.lower()
    if "y" in resp:
        main()
    else:
        exit(0)

main()
