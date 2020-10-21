from datetime import datetime

from fs_utils import get_document_filter
from mongo_utils import create_one_mongo


data = get_document_filter(
    "fc_belgingur", "forecastDate", "2020-10-15T03:00:00+00:00")
data_post = {}

for data_create in data:
    data_post = {
        "hourly": {
            "hour": [datetime.strptime(data_date, '%Y-%m-%dT%H:%M:%S+00:00') for data_date in data_create['time']],
            "pc": data_create['data']['lwe_precipitation_rate'],
            "pc_sm": data_create['data']['lwe_precipitation_smooth_rate'],
            "rh": data_create['data']['relative_humidity_at_2m_agl'],
            "tp": data_create['data']['air_temperature_at_2m_agl'],
            "tc": data_create['data']['cloud_area_fraction'],
            "rd": data_create['data']['downward_shortwave_flux'],
            "wswd": data_create['data']['wind_speed_at_10m_agl'],
            "wdLbl": data_create['data']['wind_from_direction_at_10m_agl']
        },
        "forecastDate": datetime.strptime(data_create['forecastDate'], '%Y-%m-%dT%H:%M:%S+00:00'),
        "coordinates":  data_create['info_station']['coordinates'],
        "info": {"foracast": data_create['forecast']},
        "createdAt": datetime.utcnow(),
        "updatedAt": datetime.utcnow()
    }
    create_one_mongo(data_post, f'{data_create["forecastTypes"]}Forecast')
