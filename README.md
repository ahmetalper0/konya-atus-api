# KONYA ATUS API ( Akıllı Toplu Ulaşım Sistemleri )

This API allows you to get real-time data from ATUS. Using the API you can request information about buses at a specific bus stop.

## Checking API Status

To check the status of the API itself, you can send a GET request to:

```http
GET https://ahmetalper-atus.hf.space/
```

## Retrieving Bus Information for a Specific Bus Stop

To retrieve information about buses related to a specific bus stop number, you need to replace `<bus_stop_no>` in the following endpoint with the actual bus stop number:

```http
GET https://ahmetalper-atus.hf.space/where-is-my-bus/<bus_stop_no>
```

For example, if the bus stop number is 26, the request URL would be:

```http
GET https://ahmetalper-atus.hf.space/where-is-my-bus/26
```
Example API Response:

```json
[
  {
    "route_no": "56-A",
    "name": "ŞEYH ŞAMİL",
    "direction": "KÜLTÜRPARK",
    "duration": 0
  },
  {
    "route_no": "17-A",
    "name": "TIRILIRMAK KAŞ",
    "direction": "ALAADDİN",
    "duration": 7
  },
  {
    "route_no": "84-C",
    "name": "GÖDENE TOKİ 2. ETAP",
    "direction": "ALAADDİN",
    "duration": 10
  },
  {
    "route_no": "4-A",
    "name": "MERAM YENİYOL ANASULTAN",
    "direction": "ALAADDİN",
    "duration": 13
  }
]
```

## Additional Notes

Make sure to replace `<bus_stop_no>` with the actual bus stop number in your API requests.

For more comprehensive bus stop information, you can refer to --> [https://atus.konya.bel.tr/atus/durak-bilgileri](https://atus.konya.bel.tr/atus/durak-bilgileri)

This URL likely contains detailed information about bus stops that can help you identify the correct `<bus_stop_no>` to use in your API requests.

***If you have any questions or suggestions regarding this API, feel free to reach out.***
