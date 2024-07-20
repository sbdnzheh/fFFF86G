import re
from pyrogram import Client, filters, enums
from pyrogram.types import Message
from utils import http

# Api key used in weather.com's mobile app.
weather_apikey = "8de2d8b3a93542c9a2d8b3a935a2c909"

get_coords = "https://api.weather.com/v3/location/search"
url = "https://api.weather.com/v3/aggcommon/v3-wx-observations-current"

headers = {"User-Agent": "curl/7.72.0"}

async def weather(c: Client, m: Message):
    m.text = re.sub("ه", "ة", m.text)
    r = await http.get(get_coords, headers=headers,
                       params=dict(apiKey=weather_apikey,
                                   format="json",
                                   language="ar-SA",
                                   query=m.text.split(maxsplit=1)[1]))
    loc_json = r.json()
    if not loc_json.get("location"):
        await m.reply_text("الموقع غير موجود.")
    else:
        pos = f"{loc_json['location']['latitude'][0]},{loc_json['location']['longitude'][0]}"
        r = await http.get(url, headers=headers,
                           params=dict(apiKey=weather_apikey,
                                       format="json",
                                       language="ar-SA",
                                       geocode=pos,
                                       units="m"))
        res_json = r.json()

        obs_dict = res_json["v3-wx-observations-current"]

        res = f"""
**{loc_json['location']['address'][0]}**

الحراره: `{obs_dict['temperature']} °C`
درجة الحرارة يشبه: `{obs_dict['temperatureFeelsLike']} °C`
رطوبة الهواء: `{obs_dict['relativeHumidity']}٪`
سرعة الرياح: `{obs_dict['windSpeed']} كم/ساعه`
- __{obs_dict['wxPhraseLong']}__
        """
        await m.reply_text(res, parse_mode=enums.ParseMode.MARKDOWN)
