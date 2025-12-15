## TomTom Traffic API (docs snapshot)

This document is a **generated** aggregation of the TomTom Developer Portal Traffic API documentation pages
(TomTom Maps + TomTom Orbis Maps variants). It is intended to provide a single place that lists **all endpoints**,
**all parameters**, and **response formats/examples**.

- **Base URL**: `https://api.tomtom.com`
- **Authentication**: API key in query string (`key=...`)
- **OpenAPI (downloaded)**: `docs/spec/tomtom-traffic-api.yml` (source: `https://developer.tomtom.com/documentation-assets/traffic_22072021_1.yml`)
- **Official product entry points**:
  - `https://developer.tomtom.com/traffic-api`
  - `https://developer.tomtom.com/traffic-api/api-explorer`

### Coverage

#### TomTom Maps

- `https://developer.tomtom.com/traffic-api/documentation/tomtom-maps/traffic-incidents/incident-details`
- `https://developer.tomtom.com/traffic-api/documentation/tomtom-maps/traffic-incidents/incident-details-deprecated`
- `https://developer.tomtom.com/traffic-api/documentation/tomtom-maps/traffic-incidents/incident-viewport`
- `https://developer.tomtom.com/traffic-api/documentation/tomtom-maps/traffic-incidents/raster-incident-tiles`
- `https://developer.tomtom.com/traffic-api/documentation/tomtom-maps/traffic-incidents/vector-incident-tiles`
- `https://developer.tomtom.com/traffic-api/documentation/tomtom-maps/traffic-flow/flow-segment-data`
- `https://developer.tomtom.com/traffic-api/documentation/tomtom-maps/traffic-flow/raster-flow-tiles`
- `https://developer.tomtom.com/traffic-api/documentation/tomtom-maps/traffic-flow/vector-flow-tiles`

#### TomTom Orbis Maps

- `https://developer.tomtom.com/traffic-api/documentation/tomtom-orbis-maps/traffic-incidents/incident-details`
- `https://developer.tomtom.com/traffic-api/documentation/tomtom-orbis-maps/traffic-incidents/incident-details-v2`
- `https://developer.tomtom.com/traffic-api/documentation/tomtom-orbis-maps/traffic-incidents/raster-incident-tiles`
- `https://developer.tomtom.com/traffic-api/documentation/tomtom-orbis-maps/traffic-incidents/raster-incident-tiles-v2`
- `https://developer.tomtom.com/traffic-api/documentation/tomtom-orbis-maps/traffic-incidents/vector-incident-tiles`
- `https://developer.tomtom.com/traffic-api/documentation/tomtom-orbis-maps/traffic-incidents/vector-incident-tiles-v2`
- `https://developer.tomtom.com/traffic-api/documentation/tomtom-orbis-maps/extended/traffic-incidents-extended-tiles`
- `https://developer.tomtom.com/traffic-api/documentation/tomtom-orbis-maps/traffic-flow/raster-flow-tiles`
- `https://developer.tomtom.com/traffic-api/documentation/tomtom-orbis-maps/traffic-flow/raster-flow-tiles-v2`
- `https://developer.tomtom.com/traffic-api/documentation/tomtom-orbis-maps/traffic-flow/vector-flow-tiles`
- `https://developer.tomtom.com/traffic-api/documentation/tomtom-orbis-maps/traffic-flow/vector-flow-tiles-v2`
- `https://developer.tomtom.com/traffic-api/documentation/tomtom-orbis-maps/extended/traffic-flow-extended-tiles`

## TomTom Maps endpoints

### Incident Details

- **Source**: `https://developer.tomtom.com/traffic-api/documentation/tomtom-maps/traffic-incidents/incident-details`

#### Tables

**Request parameters**

| Required parameters | Description |
| --- | --- |
| baseURL string | The base URL for calling the API. Values: api.tomtom.com : The default global API endpoint. kr-api.tomtom.com : The region-specific endpoint for
South Korea. See the region-specific content documentation . |
| versionNumber string | The service version number. Value: The current value is 5 . |
| bbox float,float,float,float | The corners of the area to report on, expressed in the EPSG:4326 projection. These are two longitude-latitude pairs describing the
corners of the bounding box. The first pair is for the lower-left corner
and the second pair for the upper-right corner. All values should be
separated by a comma. The maximum area of a bounding box is 10,000 km 2 . This parameter is mutually exclusive with the  ids
parameter. This parameter is available only for  GET  requests. Values: minLon,minLat,maxLon,maxLat |
| ids string | Comma separated list of incidents IDs. The maximum number of incidents
IDs is 5 for GET requests. This parameter is mutually exclusive with the  bbox
parameter. This parameter is available only for  GET  requests. Note: Incidents IDs are available from the result of a previous query with the 'bbox' parameter. Values: comma separated string |
| key string | The authorization key for access to the API. Value: Your valid API Key. |

**Request parameters**

| Optional parameters | Description |
| --- | --- |
| fields string | The fields to be included in the response, nested as in the response
schema. In order to obtain all data, it is necessary to place the whole
object in the query. get Default value {
  incidents
    {
      type,
      geometry{
        type,coordinates
      },
      properties{
        iconCategory
      }
    }
} 1 { 2 incidents 3 { 4 type, 5 geometry{ 6 type,coordinates 7 }, 8 properties{ 9 iconCategory 10 } 11 } 12 } get Value with all available fields {
  incidents{
    type,
    geometry{
      type,
      coordinates
    },
    properties{
      id,
      iconCategory,
      magnitudeOfDelay,
      events{
        description,
        code,
        iconCategory
      },
      startTime,
      endTime,
      from,
      to,
      length,
      delay,
      roadNumbers,
      timeValidity,
      probabilityOfOccurrence,
      numberOfReports,
      lastReportTime
      tmc{
        countryCode,
        tableNumber,
        tableVersion,
        direction,
        points{
          location,
          offset
        }
      }
    }
  }
} 1 { 2 incidents{ 3 type, 4 geometry{ 5 type, 6 coordinates 7 }, 8 properties{ 9 id, 10 iconCategory, 11 magnitudeOfDelay, 12 events{ 13 description, 14 code, 15 iconCategory 16 }, 17 startTime, 18 endTime, 19 from, 20 to, 21 length, 22 delay, 23 roadNumbers, 24 timeValidity, 25 probabilityOfOccurrence, 26 numberOfReports, 27 lastReportTime 28 tmc{ 29 countryCode, 30 tableNumber, 31 tableVersion, 32 direction, 33 points{ 34 location, 35 offset 36 } 37 } 38 } 39 } 40 } |
| language string | The language code for the output language. Affects the description fields in the response. When an incident
description does not have a translation, an English description is
returned. Default value: en-GB Allowed values: ar ca-ES cs-CZ da-DK de-DE el-GR en-GB en-US es-ES et-EE fi-FI fr-FR he-IL hu-HU id-ID it-IT ko-KR lt-LT lv-LV nb-NO nl-NL pl-PL pt-PT ro-RO ru-RU sk-SK sv-SE th-TH tr-TR zh-TW |
| t string | The Traffic Model ID is the reference value for the state of traffic at
a particular time. It is updated every minute, and is valid for two
minutes before it times out. See the HTTP response headers section and Traffic Model ID page for more
information. Default value: current Traffic Model ID Allowed value: Traffic_Model_ID |
| categoryFilter string | This filter allows the choice of types of incidents and future incidents
to be included in the response. Filtering takes into account the main
icon category of the incident. Both value types can be used: numeric and
descriptive strings. Multiple values are supported and should be
separated by a comma. Default values: 0,1,2,3,4,5,6,7,8,9,10,11,14 Allowed values: 0 : Unknown 1 : Accident 2 : Fog 3 : DangerousConditions 4 : Rain 5 : Ice 6 : Jam 7 : LaneClosed 8 : RoadClosed 9 : RoadWorks 10 : Wind 11 : Flooding 14 : BrokenDownVehicle |
| timeValidityFilter string | This filter allows the choice of incidents based on their occurrence in
time. Multiple values are supported and they should be separated by a
comma. Default value:  present Allowed values: present future |

**Request headers**

| Optional headers | Description |
| --- | --- |
| Accept-Encoding | Contains the content encoding (usually a compression algorithm), that
the client is able to understand. It is strongly recommended using this header in order to limit
bandwidth usage. Value: gzip |
| Tracking-ID | Specifies an identifier for the request. It can be used to trace a call.
The value must match the regular expression '^[a-zA-Z0-9-]{1,100}$' . An example of the format
that matches this regular expression is a UUID (e.g., 9ac68072-c7a4-11e8-a8d5-f2801f1b9fd1 ). For details check RFC 4122 . If specified, it is replicated in the Tracking-ID response header. It
is only meant to be used for support and does not involve tracking of
you or your users in any form. Value: <string> |

**Response data**

| Field | Description |
| --- | --- |
| incidents object | Incidents which belong or intersect with the given bounding box. |

**Response data**

| Field | Description |
| --- | --- |
| type string | The value is set as Feature ( GeoJSON feature object). |
| geometry object | A GeoJSON feature of type Point or Linestring (depending
on the incident). It always contains the type and coordinates fields. |
| properties object | The properties of a particular incident. |

**Response data**

| Field | Description |
| --- | --- |
| id string | The ID of the traffic incident, common among Traffic Incident API
services where it is available. |
| iconCategory integer | The main icon category associated with this incident. This is an icon
category associated with the first event in the events list
describing the incident. The values meaning: 0 : Unknown 1 : Accident 2 : Fog 3 : Dangerous Conditions 4 : Rain 5 : Ice 6 : Jam 7 : Lane Closed 8 : Road Closed 9 : Road Works 10 : Wind 11 : Flooding 14 : Broken Down Vehicle |
| magnitudeOfDelay integer | The magnitude of delay associated with an incident. The values meaning: 0 : Unknown 1 : Minor 2 : Moderate 3 : Major 4 : Undefined (used for road closures and other
indefinite delays) |
| events object | The list of events describing the details of the incident in the
language requested. Traffic incident can be described with more than one Event object. |
| startTime string | Start time of the incident, if available. The date is described in the ISO8601 format. |
| endTime string | End time of the incident, if available. The date is described in the ISO8601 format. |
| from string | The name of the location where the traffic due to the incident starts. |
| to string | The name of the location where the traffic due to the incident ends. |
| length float | The length of the incident in meters. |
| delay integer | The delay in seconds caused by the incident (except road closures). It
is calculated against free-flow travel time (the travel time when the
traffic is minimal, e.g., night traffic). |
| roadNumbers array of strings | The road number(s) affected by the incident. |
| timeValidity string | Enumeration string describing if the incident occurrence is now or in
the future. |
| tmc object | TMC (Traffic Message Channel) data of the traffic incident, needed to
determine its location. |
| probabilityOfOccurrence string | Enumeration string specifying the likelihood of the occurring incident. Allowed values: certain probable risk_of improbable |
| numberOfReports integer | The number of reports given by actual end-users. |
| lastReportTime string | The date in ISO8601 format, when the last time the incident was reported. Gives the user
confidence that the incident is fresh. |
| aci object | The Community Attributes (ACI). |

**Response data**

| Field | Description |
| --- | --- |
| description string | The description of the event (being part of incident) in the requested
language. |
| code integer | The predefined alert code, describing the event (part of incident). |
| iconCategory integer | The icon category associated with the event. The icon category from the
first event in the list is replicated in the iconCategory field in the IncidentProperties object. |

**Response data**

| Field | Description |
| --- | --- |
| probabilityOfOccurrence string | Enumeration string specifying the likelihood of the occurring incident. Allowed values: certain probable risk_of improbable |
| numberOfReports integer | The number of reports given by actual end-users. |
| lastReportTime string | The date in ISO8601 format, when the last time the incident was reported. Gives the user
confidence that the incident is fresh. |

**Response data**

| Field | Description |
| --- | --- |
| detailedError object | Main object of the error response. |
| code string | One of a server-defined set of error codes. |
| message string | A human-readable description of the error code. |

**Response data**

| Code | Meaning & possible causes |
| --- | --- |
| 200 | OK |
| 400 | Bad request , usually due to a malformed syntax or incorrect
format of the Traffic Model ID. |
| 403 | Forbidden : The supplied API Key is not valid for this request. |
| 405 | Method Not Allowed : The provided HTTP request method is known by
the server, but is not supported by the target resource. |
| 429 | Too Many Requests : Too many requests were sent in a given amount
of time for the supplied API Key. |
| 500 | Internal Server Error |

**Response data**

| Header | Description |
| --- | --- |
| Access-Control-Allow-Origin | Indicates that cross-origin resource sharing (CORS) is allowed. Value: * |
| Allow | Lists the set of supported HTTP methods. The header is sent in case a 405 HTTP response code is returned. Value: GET , POST , HEAD |
| Content-Encoding | Indicates which encodings were applied to the response body. Value: gzip |
| Content-Length | Contains information about the size of the response body. Value: <decimal number> |
| Content-Type | Indicates the media type of the resource returned. Value: <application/json; charset=utf-8> |
| Date | Contains the date and time when the message was originated. Value: <http-date> |
| TrafficModelID | Contains the reference value for the state of traffic at a particular
time. If the request contains a valid Traffic Model ID, its value is
replicated here. If the request does not contain a Traffic Model ID, or
it contains outdated data, then the most recent one is returned. Value: <numeric> |
| Tracking-ID | An identifier for the request. If the Tracking-ID header was specified
in the request, it is replicated in the response. Otherwise, it is
generated automatically by the service. For details check RFC 4122 . It is only meant to be used for support and does not involve tracking
of you or your users in any form. Value: <string> |

**Successful response**

| Field | Description |
| --- | --- |
| incidents object | Incidents which belong or intersect with the given bounding box. |

**Successful response**

| Field | Description |
| --- | --- |
| type string | The value is set as Feature ( GeoJSON feature object). |
| geometry object | A GeoJSON feature of type Point or Linestring (depending
on the incident). It always contains the type and coordinates fields. |
| properties object | The properties of a particular incident. |

**Successful response**

| Field | Description |
| --- | --- |
| id string | The ID of the traffic incident, common among Traffic Incident API
services where it is available. |
| iconCategory integer | The main icon category associated with this incident. This is an icon
category associated with the first event in the events list
describing the incident. The values meaning: 0 : Unknown 1 : Accident 2 : Fog 3 : Dangerous Conditions 4 : Rain 5 : Ice 6 : Jam 7 : Lane Closed 8 : Road Closed 9 : Road Works 10 : Wind 11 : Flooding 14 : Broken Down Vehicle |
| magnitudeOfDelay integer | The magnitude of delay associated with an incident. The values meaning: 0 : Unknown 1 : Minor 2 : Moderate 3 : Major 4 : Undefined (used for road closures and other
indefinite delays) |
| events object | The list of events describing the details of the incident in the
language requested. Traffic incident can be described with more than one Event object. |
| startTime string | Start time of the incident, if available. The date is described in the ISO8601 format. |
| endTime string | End time of the incident, if available. The date is described in the ISO8601 format. |
| from string | The name of the location where the traffic due to the incident starts. |
| to string | The name of the location where the traffic due to the incident ends. |
| length float | The length of the incident in meters. |
| delay integer | The delay in seconds caused by the incident (except road closures). It
is calculated against free-flow travel time (the travel time when the
traffic is minimal, e.g., night traffic). |
| roadNumbers array of strings | The road number(s) affected by the incident. |
| timeValidity string | Enumeration string describing if the incident occurrence is now or in
the future. |
| tmc object | TMC (Traffic Message Channel) data of the traffic incident, needed to
determine its location. |
| probabilityOfOccurrence string | Enumeration string specifying the likelihood of the occurring incident. Allowed values: certain probable risk_of improbable |
| numberOfReports integer | The number of reports given by actual end-users. |
| lastReportTime string | The date in ISO8601 format, when the last time the incident was reported. Gives the user
confidence that the incident is fresh. |
| aci object | The Community Attributes (ACI). |

**Successful response**

| Field | Description |
| --- | --- |
| description string | The description of the event (being part of incident) in the requested
language. |
| code integer | The predefined alert code, describing the event (part of incident). |
| iconCategory integer | The icon category associated with the event. The icon category from the
first event in the list is replicated in the iconCategory field in the IncidentProperties object. |

**Successful response**

| Field | Description |
| --- | --- |
| probabilityOfOccurrence string | Enumeration string specifying the likelihood of the occurring incident. Allowed values: certain probable risk_of improbable |
| numberOfReports integer | The number of reports given by actual end-users. |
| lastReportTime string | The date in ISO8601 format, when the last time the incident was reported. Gives the user
confidence that the incident is fresh. |

**Error response**

| Field | Description |
| --- | --- |
| detailedError object | Main object of the error response. |
| code string | One of a server-defined set of error codes. |
| message string | A human-readable description of the error code. |

#### Examples & payloads

**GET Request URL with bounding box**

```text
https://{baseURL}/traffic/services/{versionNumber}/incidentDetails?key={Your_Api_Key}&bbox={bbox}&fields={fields}&language={language}&t={t}&categoryFilter={categoryFilter}&timeValidityFilter={timeValidityFilter}
```

**GET Request URL with IDs**

```text
https://{baseURL}/traffic/services/{versionNumber}/incidentDetails?key={Your_Api_Key}&ids={ids}&fields={fields}&language={language}&t={t}&categoryFilter={categoryFilter}&timeValidityFilter={timeValidityFilter}
```

**GET Example with bounding box**

```text
https://api.tomtom.com/traffic/services/5/incidentDetails?key={Your_Api_Key}&bbox=4.8854592519716675,52.36934334773164,4.897883244144765,52.37496348620152&fields={incidents{type,geometry{type,coordinates},properties{iconCategory}}}&language=en-GB&t=1111&timeValidityFilter=present
```

**GET Example with IDs**

```text
https://api.tomtom.com/traffic/services/5/incidentDetails?key={Your_Api_Key}&ids=4819f7d0a15db3d9b0c3cd9203be7ba5&fields={incidents{type,geometry{type,coordinates},properties{iconCategory}}}&language=en-GB&t=1111&timeValidityFilter=present
```

**GET curl command format**

```text
curl 'https://api.tomtom.com/traffic/services/5/incidentDetails?key={Your_Api_Key}&bbox=4.8854592519716675,52.36934334773164,4.897883244144765,52.37496348620152&fields={incidents{type,geometry{type,coordinates},properties{iconCategory}}}&language=en-GB&t=1111&timeValidityFilter=present'
```

**GET curl command format**

```text
curl 'https://api.tomtom.com/traffic/services/5/incidentDetails?key={Your_Api_Key}&ids=4819f7d0a15db3d9b0c3cd9203be7ba5&fields={incidents{type,geometry{type,coordinates},properties{iconCategory}}}&language=en-GB&t=1111&timeValidityFilter=present'
```

**GET category filter**

```text
https://api.tomtom.com/traffic/services/5/incidentDetails?key={Your_Api_Key}&bbox=4.8854592519716675,52.36934334773164,4.897883244144765,52.37496348620152&fields={incidents{type,geometry{type,coordinates},properties{iconCategory}}}&language=en-GB&t=1111&categoryFilter=Accident&timeValidityFilter=present
```

**GET curl command with category filter**

```text
curl 'https://api.tomtom.com/traffic/services/5/incidentDetails?key={Your_Api_Key}&bbox=4.8854592519716675,52.36934334773164,4.897883244144765,52.37496348620152&fields={incidents{type,geometry{type,coordinates},properties{iconCategory}}}&language=en-GB&t=1111&categoryFilter=Accident&timeValidityFilter=present'
```

**POST Request URL with IDs**

```text
https://{baseURL}/traffic/services/{versionNumber}/incidentDetails?key={Your_Api_Key}&fields={fields}&language={language}&t={t}&categoryFilter={categoryFilter}&timeValidityFilter={timeValidityFilter}
```

**POST Example with IDs**

```text
https://api.tomtom.com/traffic/services/5/incidentDetails?key={Your_Api_Key}&fields={incidents{type,geometry{type,coordinates},properties{iconCategory}}}&language=en-GB&t=1111&timeValidityFilter=present
```

**POST curl command format**

```text
curl -X POST 'https://api.tomtom.com/traffic/services/5/incidentDetails?key={Your_Api_Key}&fields={incidents{type,geometry{type,coordinates},properties{iconCategory}}}&language=en-GB&t=1111&timeValidityFilter=present -d '{
    "ids": [
        "4819f7d0a15db3d9b0c3cd9203be7ba5"
    ]
}'
```

**GET Default value**

```json
{
  incidents
    {
      type,
      geometry{
        type,coordinates
      },
      properties{
        iconCategory
      }
    }
}
```

**GET Value with all available fields**

```json
{
  incidents{
    type,
    geometry{
      type,
      coordinates
    },
    properties{
      id,
      iconCategory,
      magnitudeOfDelay,
      events{
        description,
        code,
        iconCategory
      },
      startTime,
      endTime,
      from,
      to,
      length,
      delay,
      roadNumbers,
      timeValidity,
      probabilityOfOccurrence,
      numberOfReports,
      lastReportTime
      tmc{
        countryCode,
        tableNumber,
        tableVersion,
        direction,
        points{
          location,
          offset
        }
      }
    }
  }
}
```

**Request body**

```json
{
    ids: [String!]!
}
```

**type Query**

```text
type Query {
  incidents : [Incident!]!
}
```

**type Query**

```text
type Query {
  incidents : [Incident]!
}
```

**type Incident**

```text
type Incident {
    type: GeojsonFeatureType!
    geometry : GeojsonGeometry!
    properties: IncidentProperties!
}
```

**type IncidentProperties, Event, GeojsonGeometry, GeojsonLinestring, Aci**

```text
type IncidentProperties {
    id : String!
    iconCategory  : Int!
    magnitudeOfDelay : Int!
    events : [Event!]!
    startTime : String
    endTime : String
    from : String
    to : String
    length : Float!
    delay : Int
    roadNumbers : [String!]!
    timeValidity : TimeValidity!
    probabilityOfOccurrence : ProbabilityOfOccurrence!
    numberOfReports : Int
    lastReportTime : String
    tmc : Tmc
    aci : Aci
}

type Event {
    description : String!
    code : Int!
    iconCategory : Int!
}

union GeojsonGeometry = GeojsonPoint | GeojsonLinestring

type GeojsonPoint {
    type : GeojsonPointType!
    coordinates : [Float!]!
}

type GeojsonLinestring {
    type : GeojsonLinestringType!
    coordinates : [[Float!]!]!
}

enum GeojsonLinestringType {
    LineString
}

enum GeojsonPointType {
    Point
}

enum GeojsonFeatureType {
    Feature
}

type Aci {
    probabilityOfOccurrence : ProbabilityOfOccurrence!
    numberOfReports : Int!
    lastReportTime : String!
}

enum ProbabilityOfOccurrence {
    certain
    probable
    risk_of
    improbable
}

type Tmc {
    countryCode: String!
    tableNumber: String!
    tableVersion: String!
    direction: Direction!
    points [TmcPoint!]!
}

enum Direction {
    positive
    negative
}

type TmcPoint {
    location : Int!
    offset: Int
}

enum TimeValidity {
    present
    future
}
```

**Response example - JSON**

```json
{
  "incidents": [
    {
      "type": "Feature",
      "properties": {
        "iconCategory": 8
      },
      "geometry": {
        "type": "LineString",
        "coordinates": [
          [4.8905266414, 52.3725919469],
          [4.8905306647, 52.372535656],
          [4.8905360291, 52.3724806443],
          [4.8905387113, 52.3724028603],
          [4.8905440757, 52.3723505607],
          [4.8905467579, 52.3722754886],
          [4.8905574868, 52.3721722195],
          [4.8905762622, 52.3719066767],
          [4.8905963788, 52.371663905],
          [4.8905936966, 52.371524454],
          [4.8905749211, 52.3714278871],
          [4.8905440757, 52.3713393544],
          [4.8905065248, 52.3712669418],
          [4.8904555628, 52.3711703743],
          [4.8904166708, 52.3711100387],
          [4.8903268168, 52.3709759593],
          [4.8901725898, 52.370765372],
          [4.8900062928, 52.370581651],
          [4.8899472842, 52.3705320104]
        ]
      }
    }
  ]
}
```

**Response example with available fields - JSON**

```json
{
  "incidents" : [
    {
      "type" : "Feature",
      "properties" : {
        "id":"4819f7d0a15db3d9b0c3cd9203be7ba5",
        "iconCategory" : 8,
        "magnitudeOfDelay" : 4,
        "startTime" : "2021-02-02T15:37:00Z",
        "endTime" : "2021-04-30T22:00:00Z",
        "from" : "Paleisstraat",
        "to" : "Rosmarijnsteeg",
        "length" : 238.553,
        "delay" : 0,
        "roadNumbers" : [],
        "timeValidity" : "present",
        "events" : [
          {
            "code" : 401,
            "description" : "Closed",
            "iconCategory" : 8
          }
        ],
        "aci" : null,
        "tmc" : null
	"probabilityOfOccurrence" : "certain",
	"numberOfReports" : "null",
	"lastReportTime" : "null
      },
      "geometry" : {
        "type" : "LineString",
        "coordinates" : [[4.8905266414,52.3725919469],[4.8905306647,52.3725356560],[4.8905360291,52.3724806443],[4.8905387113,52.3724028603],[4.8905440757,52.3723505607],[4.8905467579,52.3722754886],[4.8905574868,52.3721722195],[4.8905762622,52.3719066767],[4.8905963788,52.3716639050],[4.8905936966,52.3715244540],[4.8905749211,52.3714278871],[4.8905440757,52.3713393544],[4.8905065248,52.3712669418],[4.8904555628,52.3711703743],[4.8904166708,52.3711100387],[4.8903268168,52.3709759593],[4.8901725898,52.3707653720],[4.8900062928,52.3705816510],[4.8899472842,52.3705320104]]
      }
    }
  ]
}
```

**Error response example - JSON**

```json
{
  "detailedError ": {
    "code": "INVALID_REQUEST",
    "message": "Unknown field in fields=incidents.properties.last"
  }
}
```

### Incident Details (Deprecated)

- **Source**: `https://developer.tomtom.com/traffic-api/documentation/tomtom-maps/traffic-incidents/incident-details-deprecated`

#### Tables

**Request parameters**

| Required parameters | Description |
| --- | --- |
| baseURL string | The base URL for calling the API. Values: api.tomtom.com : The default global API endpoint. kr-api.tomtom.com : The region-specific endpoint for South Korea. See the region-specific content documentation . |
| versionNumber string | The service version number. Value: The current value is 4 . |
| style string | The style used with Raster Incident Tiles and Vector Incident Tiles. This has an effect on the coordinates and encoded geometry of traffic incidents in the response. Values: s0 s0-dark s1 s2 s3 night |
| boundingBox float | The corners of the area to report on, expressed in the projection specified. These are two latitude-longitude pairs describing corners of the bounding box. The first pair is for the lower-left corner and the second pair for the upper-right corner. All values should be separated by commas. If the width or height exceeds maximum size, it is trimmed to the maximum allowed size. See th Maximum bounding box section for details. Values: minY,minX,maxY,maxX , or minLat,minLon,maxLat,maxLon . |
| zoom integer | This is the zoom level. This will affect traffic incident coordinates and determine which incidents are included in clusters rather than reported separately. Value: 0..22 |
| trafficModelID string | The Traffic Model ID is the reference value for the state of traffic at a particular time. It can be obtained from the Viewport API. It is updated every minute, and is valid for two minutes before it times out. An invalid value of the Traffic Model ID or a value equal to -1 always invokes the most recent traffic model. See the Response headers section for more information. Values: Traffic model ID or -1 . |
| format string | The content type of the response structure. If the content type is jsonp , a callback method must be specified at the end of the service call. Values: xml json jsonp |
| key string | The authorization key for access to the API. Value: Your valid API Key . |

**Request parameters**

| Optional parameters | Description |
| --- | --- |
| language string | The ISO 639-1 code for the output language. Affects the <c> (cause) and <d> (description) fields in the response. When an invalid language code is provided the response is returned in English. When an incident cause or description does not have a translation, an English description is returned. Languages marked with * (an asterisk) are deprecated. Default value: en Other values: ar, ca, cs, da, de, el, en, en-GB, en-US, es, et, fi, fr, he, hu, id, in*, it, iw*, lt, lv, nb, nl, no, pl, pt, ro, ru, sk, sv, th, tr, zh |
| projection string | The projection used to specify the coordinates in the request and response. Default value: EPSG900913 Other value: EPSG4326 |
| geometries string | The type of vector geometry added to incidents (returned in the <v> element of the response). original places incidents precisely on the road. shifted moves the incident slightly (depending on the zoom level) to indicate specific road lanes. If this parameter is not used , the response will not contain a <v> element. Values: original and shifted |
| expandCluster boolean | This separately lists all traffic incidents in a cluster. Default Value: false Other value: true |
| originalPosition boolean | This returns the original position of the incident ( <op> ) as well as the one shifted to the beginning of the traffic tube ( <p> ). Default Value: false Other value: true |
| jsonp string | Specifies the callback method. Only used where the contentType is jsonp . Value: An asynchronous or synchronous function. |

**Request headers**

| Optional headers | Description |
| --- | --- |
| Accept-Encoding | Contains the content encoding (usually a compression algorithm), that the client is able to understand. Value: gzip |
| Tracking-ID | Specifies an identifier for the request. It can be used to trace a call. The value must match the regular expression '^[a-zA-Z0-9-]{1,100}$' . An example of the format that matches this regular expression is a UUID (e.g., 9ac68072-c7a4-11e8-a8d5-f2801f1b9fd1 ). For details check RFC 4122 . If specified, it is replicated in the Tracking-ID response header. It is only meant to be used for support and does not involve tracking of you or your users in any form. Value: <string> |

**Response data**

| Field | Description |
| --- | --- |
| <tm> object | The main response element. The attribute id is the current traffic model. It may be different than the one in the request, since the model refreshes every two minutes. |
| <poi> array | A single traffic incident, or a cluster of traffic incidents. |
| <cpoi> array | A single incident, only within an expanded cluster. |
| <id> string | The ID of the traffic incident, common among Traffic Incident API services where it is available. |
| <p> object | The point where an icon of the cluster or raw incident should be drawn, expressed in the requested projection. In the case of a cluster, this is its center. In the case of an incident which has a shape/length, this is its starting point. The point is also affected by: Traffic style Zoom level Road type |
| <op> object | The point representing the actual position of the incident, expressed in the required projection . In the case of a cluster, this is its center. In the case of an incident which has a shape/length, this is its starting point. This is only returned if the originalPosition value is a boolean true . |
| <ic> integer | The icon category associated with this incident. Values are numbers in the range 0-14, with the following meanings: 0 : Unknown 1 : Accident 2 : Fog 3 : Dangerous Conditions 4 : Rain 5 : Ice 6 : Jam 7 : Lane Closed 8 : Road Closed 9 : Road Works 10 : Wind 11 : Flooding 13 : Cluster: Returned if a cluster contains incidents with different icon categories. 14 : Broken Down Vehicle |
| <ty> integer | The magnitude of delay associated with an incident. Values can be: 0 : Unknown 1 : Minor 2 : Moderate 3 : Major 4 : Undefined (used for road closures and other indefinite delays) |
| <cbl> object | Bottom-left coordinate of the cluster in the projection of the request. |
| <ctr> object | Top-right coordinate of the cluster in the projection of the request. |
| <cs> integer | Cluster size: The number of incidents in the cluster. |
| <d> string | Description of the incident in the language requested. |
| <sd> string | Start date of the incident, if available. The date is described in the ISO8601 format . |
| <ed> string | Estimated end date of the incident, if available. The date is described in the ISO8601 format . |
| <c> string | Cause of the incident, if available, in the language requested. |
| <f> string | From: The name of the intersection or location where the traffic due to the incident starts. |
| <t> string | To: The name of the intersection or location where the traffic due to the incident ends. |
| <l> integer | Length of the incident in meters. |
| <dl> integer | Delay caused by the incident in seconds (except in road closures). It is calculated against free-flow travel time (the travel time when the traffic is minimal, e.g., night traffic). |
| <r> string | The road number(s) affected by the incident. Multiple road numbers will delimited by slashes. |
| <v> string | A vector representing the geometry of the incident. Not available for clusters and incidents that do not have a shape/length. Only returned if a valid geometries value is included in the request. The vector is encoded with the Google Encoded Polyline Algorithm . |

**Response data**

| Field | Description |
| --- | --- |
| detailedError object | Main object of the error response. |
| code string | One of a server-defined set of error codes. |
| message string | A human-readable description of the error code. |

**Response data**

| Code | Meaning & possible causes |
| --- | --- |
| 200 | OK |
| 400 | Bad request , usually due to a malformed syntax. |
| 403 | Forbidden : The supplied API Key is not valid for this request. |
| 405 | Method Not Allowed : The provided HTTP request method is known by the server, but is not supported by the target resource. |
| 429 | Too Many Requests : Too many requests were sent in a given amount of time for the supplied API Key. |
| 500 | Internal Server Error |

**Response data**

| Header | Description |
| --- | --- |
| Access-Control-Allow-Origin | Indicates that cross-origin resource sharing (CORS) is allowed. Value : * |
| Allow | Lists the set of supported HTTP methods. The header is sent in case a 405 HTTP response code is returned. Value : GET, HEAD |
| Content-Encoding | Indicates which encodings were applied to the response body. Value : gzip |
| Cache-Control | Contains directives for a caching mechanism. Values : <private, no-cache, no-store, max-age=0, must-revalidate> |
| Content-Length | Contains information about the size of the response body. Value : <decimal number> |
| Content-Type | Indicates the media type of the resource returned. Value : <application/json; charset=utf-8> <application/javascript; charset=utf-8> <text/xml; charset=utf-8> |
| Content-Language | Indicates the language of the response body. Value : <en> |
| Date | Contains the date and time when the message was originated. Value : <http-date> |
| Expires | Contains the date after which the response is considered outdated. Value : <http-date> |
| TrafficModelID | Contains the reference value for the state of traffic at a particular time. If the request contains a valid Traffic Model ID and is not equal to -1 , its value is replicated here. If the request contains an invalid Traffic Model ID or is equal to -1 , the most recent one is returned. Value : <numeric> |
| Tracking-ID | An identifier for the request. If the Tracking-ID header was specified in the request, it is replicated in the response. Otherwise, it is generated automatically by the service. For details check RFC 4122 . It is only meant to be used for support and does not involve tracking of you or your users in any form. Value : <string> |

**Response field structure**

| Field | Description |
| --- | --- |
| <tm> object | The main response element. The attribute id is the current traffic model. It may be different than the one in the request, since the model refreshes every two minutes. |
| <poi> array | A single traffic incident, or a cluster of traffic incidents. |
| <cpoi> array | A single incident, only within an expanded cluster. |
| <id> string | The ID of the traffic incident, common among Traffic Incident API services where it is available. |
| <p> object | The point where an icon of the cluster or raw incident should be drawn, expressed in the requested projection. In the case of a cluster, this is its center. In the case of an incident which has a shape/length, this is its starting point. The point is also affected by: Traffic style Zoom level Road type |
| <op> object | The point representing the actual position of the incident, expressed in the required projection . In the case of a cluster, this is its center. In the case of an incident which has a shape/length, this is its starting point. This is only returned if the originalPosition value is a boolean true . |
| <ic> integer | The icon category associated with this incident. Values are numbers in the range 0-14, with the following meanings: 0 : Unknown 1 : Accident 2 : Fog 3 : Dangerous Conditions 4 : Rain 5 : Ice 6 : Jam 7 : Lane Closed 8 : Road Closed 9 : Road Works 10 : Wind 11 : Flooding 13 : Cluster: Returned if a cluster contains incidents with different icon categories. 14 : Broken Down Vehicle |
| <ty> integer | The magnitude of delay associated with an incident. Values can be: 0 : Unknown 1 : Minor 2 : Moderate 3 : Major 4 : Undefined (used for road closures and other indefinite delays) |
| <cbl> object | Bottom-left coordinate of the cluster in the projection of the request. |
| <ctr> object | Top-right coordinate of the cluster in the projection of the request. |
| <cs> integer | Cluster size: The number of incidents in the cluster. |
| <d> string | Description of the incident in the language requested. |
| <sd> string | Start date of the incident, if available. The date is described in the ISO8601 format . |
| <ed> string | Estimated end date of the incident, if available. The date is described in the ISO8601 format . |
| <c> string | Cause of the incident, if available, in the language requested. |
| <f> string | From: The name of the intersection or location where the traffic due to the incident starts. |
| <t> string | To: The name of the intersection or location where the traffic due to the incident ends. |
| <l> integer | Length of the incident in meters. |
| <dl> integer | Delay caused by the incident in seconds (except in road closures). It is calculated against free-flow travel time (the travel time when the traffic is minimal, e.g., night traffic). |
| <r> string | The road number(s) affected by the incident. Multiple road numbers will delimited by slashes. |
| <v> string | A vector representing the geometry of the incident. Not available for clusters and incidents that do not have a shape/length. Only returned if a valid geometries value is included in the request. The vector is encoded with the Google Encoded Polyline Algorithm . |

**Successful response**

| Field | Description |
| --- | --- |
| <tm> object | The main response element. The attribute id is the current traffic model. It may be different than the one in the request, since the model refreshes every two minutes. |
| <poi> array | A single traffic incident, or a cluster of traffic incidents. |
| <cpoi> array | A single incident, only within an expanded cluster. |
| <id> string | The ID of the traffic incident, common among Traffic Incident API services where it is available. |
| <p> object | The point where an icon of the cluster or raw incident should be drawn, expressed in the requested projection. In the case of a cluster, this is its center. In the case of an incident which has a shape/length, this is its starting point. The point is also affected by: Traffic style Zoom level Road type |
| <op> object | The point representing the actual position of the incident, expressed in the required projection . In the case of a cluster, this is its center. In the case of an incident which has a shape/length, this is its starting point. This is only returned if the originalPosition value is a boolean true . |
| <ic> integer | The icon category associated with this incident. Values are numbers in the range 0-14, with the following meanings: 0 : Unknown 1 : Accident 2 : Fog 3 : Dangerous Conditions 4 : Rain 5 : Ice 6 : Jam 7 : Lane Closed 8 : Road Closed 9 : Road Works 10 : Wind 11 : Flooding 13 : Cluster: Returned if a cluster contains incidents with different icon categories. 14 : Broken Down Vehicle |
| <ty> integer | The magnitude of delay associated with an incident. Values can be: 0 : Unknown 1 : Minor 2 : Moderate 3 : Major 4 : Undefined (used for road closures and other indefinite delays) |
| <cbl> object | Bottom-left coordinate of the cluster in the projection of the request. |
| <ctr> object | Top-right coordinate of the cluster in the projection of the request. |
| <cs> integer | Cluster size: The number of incidents in the cluster. |
| <d> string | Description of the incident in the language requested. |
| <sd> string | Start date of the incident, if available. The date is described in the ISO8601 format . |
| <ed> string | Estimated end date of the incident, if available. The date is described in the ISO8601 format . |
| <c> string | Cause of the incident, if available, in the language requested. |
| <f> string | From: The name of the intersection or location where the traffic due to the incident starts. |
| <t> string | To: The name of the intersection or location where the traffic due to the incident ends. |
| <l> integer | Length of the incident in meters. |
| <dl> integer | Delay caused by the incident in seconds (except in road closures). It is calculated against free-flow travel time (the travel time when the traffic is minimal, e.g., night traffic). |
| <r> string | The road number(s) affected by the incident. Multiple road numbers will delimited by slashes. |
| <v> string | A vector representing the geometry of the incident. Not available for clusters and incidents that do not have a shape/length. Only returned if a valid geometries value is included in the request. The vector is encoded with the Google Encoded Polyline Algorithm . |

**Error response**

| Field | Description |
| --- | --- |
| detailedError object | Main object of the error response. |
| code string | One of a server-defined set of error codes. |
| message string | A human-readable description of the error code. |

#### Examples & payloads

**GET Request URL**

```text
https://{baseURL}/traffic/services/{versionNumber}/incidentDetails/{style}/{boundingBox}/{zoom}/{trafficModelID}/{format}?key={Your_Api_Key}&language={language}&projection={projection}&geometries={geometries}&expandCluster={expandCluster}&originalPosition={originalPosition}&jsonp={jsonp}
```

**GET Request URL example**

```text
https://api.tomtom.com/traffic/services/4/incidentDetails/s3/6841263.950712,511972.674418,6886056.049288,582676.925582/11/1335294634919/xml?key={Your_Api_Key}
```

**GET Request curl command**

```text
curl 'https://{baseURL}/traffic/services/{versionNumber}/incidentDetails/{style}/{boundingBox}/{zoom}/{trafficModelID}/{format}?key={Your_Api_Key}&language={language}&projection={projection}&geometries={geometries}&expandCluster={expandCluster}&originalPosition={originalPosition}&jsonp={jsonp}'
```

**GET Query**

```text
https://api.tomtom.com/traffic/services/4/incidentDetails/s3/6841263.950712,511972.674418,6886056.049288,582676.925582/11/1335294634919/xml?key={Your_Api_Key}
```

**GET XML cluster**

```xml
<tm id="1400168040337">
  <poi>
    <id>CLUSTER_581</id>
    <p>
      <x>294962.2</x>
      <y>6535338.8</y>
    </p>
    <ic>13</ic>
    <ty>1</ty>
    <cbl>
      <x>294223.5</x>
      <y>6535005.4</y>
    </cbl>
    <ctr>
      <x>295700.9</x>
      <y>6535672.3</y>
    </ctr>
    <cs>2</cs>
    <l>7430</l>
  </poi>
  <poi>
    <id>CLUSTER_325</id>
    <p>
      <x>314807.6</x>
      <y>6538765.0</y>
    </p>
    <ic>13</ic>
    <ty>1</ty>
    <cbl>
      <x>313078.2</x>
      <y>6538198.4</y>
    </cbl>
    <ctr>
      <x>316536.9</x>
      <y>6539331.6</y>
    </ctr>
    <cs>3</cs>
    <l>2850</l>
  </poi>
  [...]
</tm>
```

**GET Query**

```text
https://api.tomtom.com/traffic/services/4/incidentDetails/s3/6841263.950712,511972.674418,6886056.049288,582676.925582/11/1335294634919/xml?key={Your_Api_Key}&language=en&expandCluster=true
```

**GET Expanded XML cluster**

```xml
<tm id="1400168682560">
  <poi>
    <id>TTR826194</id>
    <p>
      <x>581415.6</x>
      <y>6535660.9</y>
    </p>
    <ic>6</ic>
    <ty>3</ty>
    <cs>0</cs>
    <d>stationary traffic</d>
    <f>Rue Joseph Wauters</f>
    <t>Rue du Pont</t>
    <l>1100</l>
    <dl>558</dl>
    <r>N90</r>
  </poi>
  <poi>
    <id>CLUSTER_244</id>
    <p>
      <x>543483.8</x>
      <y>6537828.8</y>
    </p>
    <ic>13</ic>
    <ty>1</ty>
    <cbl>
      <x>543112.0</x>
      <y>6537745.5</y>
    </cbl>
    <ctr>
      <x>543855.5</x>
      <y>6537912.2</y>
    </ctr>
    <cs>2</cs>
    <cpoi>
      <id>TTR775657</id>
      <p>
        <x>543855.5</x>
        <y>6537912.2</y>
      </p>
      <ic>9</ic>
      <ty>1</ty>
      <cs>0</cs>
      <d>roadworks</d>
      <f>Daussoulx - A4 - E411 (A15)</f>
      <t>Fleurus - N29 (A15)</t>
      <l>460</l>
      <dl>12</dl>
      <r>A15/E42</r>
    </cpoi>
    [...]
    <l>11840</l>
  </poi>
  [...]
</tm>
```

**GET Query with geometries and original positions**

```text
https://api.tomtom.com/traffic/services/4/incidentDetails/s3/6841263.950712,511972.674418,6886056.049288,582676.925582/10/1335294634919/xml?key={Your_Api_Key}&language=en&originalPosition=true&geometries=original
```

**GET XML**

```xml
<tm id="1400168426640">
  <poi>
    <id>TTL826194</id>
    <p>
      <x>581415.6</x>
      <y>6535660.9</y>
    </p>
    <op>
      <x>581687.8</x>
      <y>6536208.0</y>
    </op>
    <ic>6</ic>
    <ty>3</ty>
    <cs>0</cs>
    <d>stationary traffic</d>
    <f>Rue Joseph Wauters</f>
    <t>Rue du Pont</t>
    <l>1100</l>
    <dl>558</dl>
    <r>N90</r>
    <v>obob@_`}mKcy@zAe_@kc@</v>
  </poi>
  <poi>
  <id>CLUSTER_489</id>
  <p>
    <x>545350.3</x>
    <y>6538010.8</y>
  </p>
  <ic>6</ic>
  <ty>1</ty>
  <cbl>
    <x>543311.4</x>
    <y>6537799.6</y>
  </cbl>
  <ctr>
    <x>547389.1</x>
    <y>6538221.9</y>
  </ctr>
  <cs>2</cs>
  <l>13450</l>
  </poi>
  [...]
</tm>
```

**Error response example - JSON**

```json
{
  "errorResponse" : {
    "@errorCode" : 400,
    "@description" : "Invalid style."
  },
  "detailedError" : {
    "code" : "INVALID_REQUEST",
    "message" : "Invalid style."
  }
}
```

**Error response example - XML**

```xml
<errorResponse description="Invalid style." errorCode="400">
  <detailedError>
    <code>INVALID_REQUEST</code>
    <message>Invalid style.</message>
  </detailedError>
</errorResponse>
```

### Incident Viewport

- **Source**: `https://developer.tomtom.com/traffic-api/documentation/tomtom-maps/traffic-incidents/incident-viewport`

#### Tables

**Request parameters**

| Required parameters | Description |
| --- | --- |
| baseURL string | The base URL for calling TomTom services. Values: api.tomtom.com : The default global API endpoint. kr-api.tomtom.com : The region-specific endpoint for
South Korea. See the region-specific content documentation . |
| versionNumber string | Version of the service to call. Value: The current value is 4 . |
| boundingBox float | Bounding box of the map viewport in an EPSG:900913 projection. The maximum size of the bounding box that can be passed is
dependent on the requested zoom level. The width and height cannot
exceed the square of a side of 16 tiles for a given zoom level. See the Maximum bounding box section for
details. Value: minY,minX,maxY,maxX . See below for boxes
crossing the 180° meridian. |
| boundingZoom integer | The zoom level of the map viewport. Used to determine whether the view
can be zoomed in. Value: 0..22 |
| overviewBox float | Bounding box of the overview map in EPSG:900913 projection. Used in case
the overview box/mini map has different copyright data than the main
map. If there is no mini map, use the same coordinates as in the
preceding boundingBox parameter. Value: minY,minX,maxY,maxX . See below for boxes
crossing the 180° meridian. |
| overviewZoom integer | Zoom level of the overview map. If there is no mini map, use the same
zoom level as in the preceding boundingZoom parameter. Value: 0..22 |
| copyright boolean | Determines what copyright information to return. When true the copyright text is returned. When false only the
copyright index is returned. Default value: true Other value: false |
| contentType string | The content type of the response structure. If the content type is
jsonp, a callback method must be specified at the end of the service
call. Values: xml json jsonp |
| apiKey string | The Authorization key for access to the API. Value: Your valid API Key . |

**Request parameters**

| Optional parameters | Description |
| --- | --- |
| jsonp string | Specifies the callback method. It is only used where the contentType parameter value is jsonp . Value: jsonp |

**Request headers**

| Optional headers | Description |
| --- | --- |
| Tracking-ID | Specifies an identifier for the request. It can be used to trace a call.
The value must match the regular expression '^[a-zA-Z0-9-]{1,100}$' . An example of the format
that matches this regular expression is a UUID (e.g., 9ac68072-c7a4-11e8-a8d5-f2801f1b9fd1 ). For details check RFC 4122 . If specified, it is replicated in the Tracking-ID response header. It is
only meant to be used for support and does not involve tracking of you
or your users in any form. Value: <string> |

**Response data**

| Field | Description |
| --- | --- |
| <viewpResp> string | The main response element. The key attributes are: maps : Indicates the TomTom internal names for the map
data used in the viewport version : Indicates the software version that generated
the response. |
| <trafficState> string/integer | Traffic information. trafficModelId : The unique ID called Traffic Model ID is used in calls
to Traffic Incident services. trafficAge : The elapsed time (in seconds) from the
Traffic Model ID creation. |
| <copyrightIDs> string | Copyright information for the map viewport. When the copyright parameter value is true , this
contains the full text of the copyright information that must be
displayed with the tiles in the viewport. When it is false ,
it indicates which copyright holders must be cited but does not list
them. |

**Response data**

| Error response field structure |  |
| --- | --- |
| Field | Description |
| detailedError{} object | Main object of the error response. |
| code string | One of a server-defined set of error codes. |
| message string | A human-readable description of the error code. |

**Response data**

| Code | Meaning & possible causes |
| --- | --- |
| 200 | OK |
| 400 | Bad request |
| 403 | Forbidden : The supplied API Key is not valid for this request. |
| 404 | Not Found : The requested resource cannot be found. |
| 405 | Method Not Allowed : The provided HTTP request method is known by
the server, but is not supported by the target resource. |
| 429 | Too Many Requests : Too many requests were sent in a given amount
of time for the supplied API Key. |
| 500 | Internal Server Error |
| 503 | Service currently unavailable : The service is currently
unavailable. |
| 596 | Service Not Found : Unknown version of the service. |

**Response data**

| Header | Description |
| --- | --- |
| Access-Control-Allow-Origin | Indicates that cross-origin resource sharing (CORS) is allowed. Value: * |
| Allow | Lists the set of supported HTTP methods. The header is sent in case a 405 HTTP response code is returned. Value: GET , HEAD |
| Cache-Control | Contains directives for a caching mechanism. Values: <private, no-cache, no-store, max-age=0, must-revalidate> |
| Content-Length | Contains information about the size of the response body. Value: <decimal number> |
| Content-Type | Indicates the media type of the resource returned. Value: <application/json; charset=utf-8> <application/javascript; charset=utf-8> <text/xml; charset=utf-8> |
| Date | Contains the date and time when the message was originated. Value: <http-date> |
| Tracking-ID | An identifier for the request. If the Tracking-ID header was specified in
the request, it is replicated in the response. Otherwise, it is
generated automatically by the service. For details check RFC 4122 . It is only meant to be used for support and does not involve tracking
of you or your users in any form. Value: <string> |

**Response field structure**

| Field | Description |
| --- | --- |
| <viewpResp> string | The main response element. The key attributes are: maps : Indicates the TomTom internal names for the map
data used in the viewport version : Indicates the software version that generated
the response. |
| <trafficState> string/integer | Traffic information. trafficModelId : The unique ID called Traffic Model ID is used in calls
to Traffic Incident services. trafficAge : The elapsed time (in seconds) from the
Traffic Model ID creation. |
| <copyrightIDs> string | Copyright information for the map viewport. When the copyright parameter value is true , this
contains the full text of the copyright information that must be
displayed with the tiles in the viewport. When it is false ,
it indicates which copyright holders must be cited but does not list
them. |

**Successful response**

| Field | Description |
| --- | --- |
| <viewpResp> string | The main response element. The key attributes are: maps : Indicates the TomTom internal names for the map
data used in the viewport version : Indicates the software version that generated
the response. |
| <trafficState> string/integer | Traffic information. trafficModelId : The unique ID called Traffic Model ID is used in calls
to Traffic Incident services. trafficAge : The elapsed time (in seconds) from the
Traffic Model ID creation. |
| <copyrightIDs> string | Copyright information for the map viewport. When the copyright parameter value is true , this
contains the full text of the copyright information that must be
displayed with the tiles in the viewport. When it is false ,
it indicates which copyright holders must be cited but does not list
them. |

**Error response**

| Error response field structure |  |
| --- | --- |
| Field | Description |
| detailedError{} object | Main object of the error response. |
| code string | One of a server-defined set of error codes. |
| message string | A human-readable description of the error code. |

#### Examples & payloads

**GET Request URL**

```text
https://{baseURL}/traffic/services/{versionNumber}/incidentViewport/{boundingBox}/{boundingZoom}/{overviewBox}/{overviewZoom}/{copyright}/{contentType}?key={Your_API_Key}&jsonp={jsonp}
```

**GET Request example**

```text
https://api.tomtom.com/traffic/services/4/incidentViewport/-939584.4813015489,-23954526.723651607,14675583.153020501,25043442.895825107/2/-939584.4813015489,-23954526.723651607,14675583.153020501,25043442.895825107/2/true/xml?key={Your_API_Key}
```

**GET Request curl command**

```text
curl 'https://api.tomtom.com/traffic/services/4/incidentViewport/-939584.4813015489,-23954526.723651607,14675583.153020501,25043442.895825107/2/-939584.4813015489,-23954526.723651607,14675583.153020501,25043442.895825107/2/true/xml?key={Your_API_Key}'
```

**XML response body**

```xml
<viewpResp xmlns="http://lbs.tomtom.com/services" maps="world" version="traffic-service 2.0.004">
  <trafficState trafficModelId="1400143970784" trafficAge="28320"/>
  <copyrightIds>
    https://www.tomtom.com/en_gb/thirdpartyproductterms/
  </copyrightIds>
</viewpResp>
```

**JSON response body**

```json
{
  "viewpResp": {
    "trafficState": {
      "@trafficAge": 28320,
      "@trafficModelId": "1400143970784"
    },
    "copyrightIds": "https://www.tomtom.com/en_gb/thirdpartyproductterms/",
    "@version": "traffic-service 2.0.004",
    "@maps": "world"
  }
}
```

**Error response example - JSON**

```json
{
  "errorResponse": {
    "@errorCode": 400,
    "@description": "Error validating overviewBbox: ",
    "@version": "traffic-service 4.0.010"
  },
  "detailedError": {
    "code": "INVALID_REQUEST",
    "message": "Error validating overviewBbox: "
  }
}
```

**Error response example - XML**

```xml
<errorResponse description="Error validating overviewBbox: "errorCode"="400" version="traffic-service 4.0.010">
  <detailedError>
    <code>INVALID_REQUEST</code>
    <message>Error validating overviewBbox: </message>
  </detailedError>
</errorResponse>
```

### Raster Incident Tiles

- **Source**: `https://developer.tomtom.com/traffic-api/documentation/tomtom-maps/traffic-incidents/raster-incident-tiles`

#### Tables

**Request parameters**

| Required parameters | Description |
| --- | --- |
| baseURL string | The base URL for calling TomTom services. Values: api.tomtom.com : The default global API endpoint. kr-api.tomtom.com : The region-specific endpoint for
South Korea. See the region-specific content documentation . |
| versionNumber string | The version of the service to call. Value: The current value is 4 . |
| style string | The style to be used to render the tile. s0 and s0-dark create traffic lines with
different color intensities and colored chevrons indicating the
severity. s1 creates traffic lines with colored chevrons
indicating the severity. s2 and s3 create plain lines with
different degrees of glow. night does not group incidents into clusters. Styles s0 and s0-dark are recommended to
use. Values: s0 s0-dark s1 s2 s3 night |
| zoom integer | The zoom level of the tile to be rendered. Value: 0..22 |
| x integer | The x coordinate of the tile on the zoom grid. Value: 0..2 zoom -1 |
| y integer | The y coordinate of the tile on the zoom grid. Value: 0..2 zoom -1 |
| key string | An API Key valid for the requested service. Value: Your valid API Key . |
| format string | The format of the response. Value: png gif |

**Request parameters**

| Optional parameters | Description |
| --- | --- |
| t string | The Traffic Model ID is the reference value for the state of traffic at a particular time.
Use -1 to get the most recent traffic information. Default value: -1 |
| tileSize integer | The tile size dimension in pixels. Values: 256 , and 512 Default value: 256 |

**Request headers**

| Optional headers | Description |
| --- | --- |
| Tracking-ID | Specifies an identifier for the request. It can be used to trace a call.
The value must match the regular expression '^[a-zA-Z0-9-]{1,100}$' . An example of the format
that matches this regular expression is a UUID (e.g., 9ac68072-c7a4-11e8-a8d5-f2801f1b9fd1 ). For details check RFC 4122 . If specified, it is replicated in the Tracking-ID response header. It is
only meant to be used for support and does not involve tracking of you
or your users in any form. Value: <string> |
| Accept | Advertises which content types, expressed as MIME types, the client is
able to understand. In this service, the header is used to specify a
preferred Bad Request response format. Format: Accept: type/subtype Accept: type/subtype, type/subtype - for multiple types Value type/subtype is one of: image/gif - in case of the 200 OK image/png - in case of the 200 OK application/json - in case of the 400 Bad Request text/xml - in case of the 400 Bad Request Examples: Accept: application/json Accept: image/png, application/json |

**Response data**

| Field | Description |
| --- | --- |
| detailedError object | Main object of the error response. |
| code string | One of a server-defined set of error codes. |
| message string | A human-readable description of the error code. |

**Response data**

| Code | Meaning & possible causes |
| --- | --- |
| 200 | OK |
| 400 | Bad request , usually due to a malformed syntax. Zoom n is out of range [0,22]: The requested zoom level is
out of the possible range. x n is out of range [0,2 zoom -1]: The requested x coordinate is out of the possible range. y n is out of range [0,2 zoom -1]: The requested y coordinate is out of the possible range. Unknown Content Type: nnn : The requested content type is not supported. |
| 403 | Forbidden : The supplied API Key is not valid for this request. |
| 405 | Method Not Allowed : The provided HTTP request method is known by
the server, but is not supported by the target resource. |
| 429 | Too Many Requests : Too many requests were sent in a given amount
of time for the supplied API Key. |
| 500 | Internal Server Error |
| 503 | Service currently unavailable |
| 596 | Service Not Found : Unknown version of the service |

**Response data**

| Header | Description |
| --- | --- |
| Access-Control-Allow-Origin | Indicates that cross-origin resource sharing (CORS) is allowed. Value: * |
| Allow | Lists the set of supported HTTP methods. The header is sent in case a 405 HTTP response Ccde is returned. Value: GET , HEAD |
| Cache-Control | Contains directives for a caching mechanism. Value: private , no-cache , no-store , max-age=0 , must-revalidate |
| Content-Length | Contains information about the size of the response body. Value: <decimal number> |
| Content-Type | Indicates the media type of the resource returned. Value: image/gif image/png application/json; charset=utf-8 - in case of the 400 Bad Request text/xml; charset=utf-8 - in case of the 400 Bad Request In case of the 200 OK the response content should be
interpreted according to the type of the format request
parameter. |
| Date | Contains the date and time when the message was originated. Value: <http-date> |
| Tracking-ID | An identifier for the request. If the Tracking-ID header was specified in
the request, it is replicated in the response. Otherwise, it is
generated automatically by the service. For details check RFC 4122 . It is only meant to be used for support and does not involve tracking
of you or your users in any form. Value: <string> |
| TrafficModelID | Contains the reference value for the state of traffic at a particular
time. If the request contains a valid Traffic Model ID and is not equal
to -1 , its value is replicated here. If the request does
not contain a Traffic Model ID or it is equal to -1 , the
most recent one is returned. Value: <numeric> |

**Error response**

| Field | Description |
| --- | --- |
| detailedError object | Main object of the error response. |
| code string | One of a server-defined set of error codes. |
| message string | A human-readable description of the error code. |

#### Examples & payloads

**GET Request URL format**

```text
https://{baseURL}/traffic/map/{versionNumber}/tile/incidents/{style}/{zoom}/{x}/{y}.{format}?key={Your_API_Key}&t={t}
```

**GET Request URL example**

```text
https://api.tomtom.com/traffic/map/4/tile/incidents/s3/12/2044/1360.png?key={Your_API_Key}
```

**GET Request curl command**

```text
curl 'https://api.tomtom.com/traffic/map/4/tile/incidents/s3/12/2044/1360.png?key={Your_API_Key}'
```

**Error response example - XML**

```xml
<errorResponse errorCode="400" description="z out of range 0 <= z <= 22" version="traffic-rasterizer 2.0.009">
  <detailedError>
    <code>INVALID_REQUEST</code>
    <message>z out of range 0 <= z <= 22</message>
  </detailedError>
</errorResponse>
```

**Error response example - JSON**

```json
{
  "detailedError": {
    "code": "INVALID_REQUEST",
    "message": "z out of range 0 <= z <= 22"
  }
}
```

### Vector Incident Tiles

- **Source**: `https://developer.tomtom.com/traffic-api/documentation/tomtom-maps/traffic-incidents/vector-incident-tiles`

#### Tables

**Request parameters**

| Required parameters | Description |
| --- | --- |
| baseURL string | The base URL for calling TomTom services. Values: api.tomtom.com : The default global API endpoint. [a\|b\|c\|d].api.tomtom.com : The default global API
endpoint (see the Host name cycling section for details on aliases). kr-api.tomtom.com : The region-specific endpoint for
South Korea. See the region-specific content documentation . |
| versionNumber string | The version of the service to call. Value: The current value is 4 . |
| zoom integer | The zoom level of the tile to be rendered. Value: 0..22 |
| x integer | The x coordinate of the tile on the zoom grid. Value: 0..2 zoom -1 |
| y integer | The y coordinate of the tile on the zoom grid. Value: 0..2 zoom -1 |
| format string | The format of the response. Value: pbf (Protocolbuffer Binary Format) |
| key string | An API Key valid for the requested service. Value: Your valid API Key . |

**Request parameters**

| Optional parameters | Description |
| --- | --- |
| t string | The Traffic Model ID is the reference
value for the state of traffic at a particular time. Use -1 to get the most recent traffic information.See the Response Headers section and Traffic Model ID page for more
information. Default value: -1 |
| tags array | The list of the values representing the available tags in the tile: icon_category (enables both icon_category and icon_category_[idx] description (enables both description and description_[idx] delay road_type left_hand_traffic magnitude traffic_road_coverage clustered probability_of_occurrence number_of_reports last_report_time end_date id road_category road_subcategory By default, only the default tags are attached to the tile geometry. See Vector format for details. The list of the values must be enclosed in square brackets [ ] , and each value must be separated by a comma. The parameter behaves as a filter, narrowing down the list of tags
enclosed in each tile, which allows a decrease in the size of the
tile. Only tags that are used in both of the two protobuf layers can be
used as a parameter value. If the array of parameters is empty, only the tags unique for the
particular layer are sent. Value: Square brackets enclosed list. |
| language string | The language code for the output language. Affects the description fields in the response. When an incident
description does not have a translation, an English description is
returned. Default value: en-GB Allowed values: ar ca-ES cs-CZ da-DK de-DE el-GR en-GB en-US es-ES et-EE fi-FI fr-FR he-IL hu-HU id-ID it-IT ko-KR lt-LT lv-LV nb-NO nl-NL pl-PL pt-PT ro-RO ru-RU sk-SK sv-SE th-TH tr-TR zh-TW |

**Request headers**

| Optional headers | Description |
| --- | --- |
| Accept-Encoding | Contains the content encoding (usually a compression algorithm), that
the client is able to understand. Value: gzip |
| If-None-Match | Contains an identifier for a specific version of resource. The server
will send back the requested resource, with a 200 HTTP status code, only
if it doesn't have an ETag matching the given one. Value: <string> |
| Tracking-ID | Specifies an identifier for the request. It can be used to trace a call. The value must match the regular expression '^[a-zA-Z0-9-]{1,100}$' . An example of the format that matches this regular expression is a
UUID (e.g., 9ac68072-c7a4-11e8-a8d5-f2801f1b9fd1 ). For
details check RFC 4122 . If specified, it is replicated in the Tracking-ID response header. It is only meant to be used for support and does not involve
tracking of you or your users in any form. Value: <string> |

**Response data**

| Field | Description |
| --- | --- |
| detailedError{} object | Main object of the error response. |
| code string | One of a server-defined set of error codes. |
| message string | A human-readable description of the error code. |

**Response data**

| Code | Meaning & possible causes |
| --- | --- |
| 200 | OK |
| 304 | Not modified |
| 400 | Bad request : The combination of parameters is not supported. zoom n is out of range [0,22]: the requested zoom level is
out of the possible range x n is out of range [0,2 zoom -1]: The requested x
coordinate is out of the possible range. y n is out of range [0,2 zoom -1]: The requested y
coordinate is out of the possible range. Invalid or outdated Traffic Model ID. |
| 403 | Forbidden : The supplied API Key is not valid for this request. |
| 405 | Method Not Allowed : The provided HTTP request method is known by
the server, but is not supported by the target resource. |
| 429 | Too Many Requests : Too many requests were sent in a given amount
of time for the supplied API Key. |
| 500 | Internal Server Error : There is a problem with the TomTom Maps
Vector Tile service. |
| 503 | Service currently unavailable : The service is currently
unavailable. |
| 596 | Service not found : Unknown version of the service. |

**Response data**

| Header | Description |
| --- | --- |
| Access-Control-Allow-Origin | Indicates that cross-origin resource sharing (CORS) is allowed. Value: * |
| Allow | Lists the set of supported HTTP methods. The header is sent in case a 405 HTTP Response Code is returned. Value: GET , HEAD |
| Content-Encoding | Indicates which encodings were applied to the response body. Value: <gzip> |
| Content-Length | Contains information about the size of the response body. Value: <decimal number> |
| Content-Type | Indicates the media type of the resource returned. Value: <image/pbf> |
| Date | Contains the date and time when the message was originated. Value: <http-date> |
| ETag | Contains an identifier for a specific version of resource. Value: W/"2fdbd61f30456" |
| Expires | Contains the date after which the response is considered outdated. Value: <http-date> |
| TrafficModelID | Contains the reference value for the state of traffic at a particular
time. If the request contains a valid Traffic Model ID and is not equal
to -1 , its value is replicated here. If the request does
not contain a Traffic Model ID or it is equal to -1 , the
most recent one is returned. Value: <numeric> |
| Tracking-ID | An identifier for the request. If the Tracking-ID header was specified in
the request, it is replicated in the response. Otherwise, it is
generated automatically by the service. For details check RFC 4122 . It is only meant to be used for support and does not involve tracking
of you or your users in any form. Value: <string> |

**Error response**

| Field | Description |
| --- | --- |
| detailedError{} object | Main object of the error response. |
| code string | One of a server-defined set of error codes. |
| message string | A human-readable description of the error code. |

#### Examples & payloads

**GET Request URL**

```text
https://{baseURL}/traffic/map/{versionNumber}/tile/incidents/{zoom}/{x}/{y}.{format}?key={Your_API_Key}&t={t}
```

**GET Request example**

```text
https://api.tomtom.com/traffic/map/4/tile/incidents/5/4/8.pbf?key={Your_API_Key}
```

**GET Request curl command**

```text
curl 'https://api.tomtom.com/traffic/map/4/tile/incidents/5/4/8.pbf?key={Your_API_Key}'
```

**GET Request URL using a.api.tomtom.com**

```text
https://a.api.tomtom.com/traffic/map/4/tile/incidents/1/0/0.pbf?key=Your_API_Key
```

**GET Request URL using b.api.tomtom.com**

```text
https://b.api.tomtom.com/traffic/map/4/tile/incidents/1/0/0.pbf?key=Your_API_Key
```

**Error response example - JSON**

```json
{
  "error": "Invalid zoom value. Allowed values are <0,22>.",
  "httpStatusCode": 400,
  "detailedError": {
    "code": "INVALID_REQUEST",
    "message": "Invalid zoom value. Allowed values are <0,22>."
  }
}
```

### Flow Segment Data

- **Source**: `https://developer.tomtom.com/traffic-api/documentation/tomtom-maps/traffic-flow/flow-segment-data`

#### Tables

**Request parameters**

| Required parameters | Description |
| --- | --- |
| baseURL string | The base URL for calling TomTom services. Values: api.tomtom.com : The default global API endpoint. kr-api.tomtom.com : The region-specific endpoint for
South Korea. See the region-specific content documentation . |
| versionNumber string | The version of the service to call. Value: The current value is 4 . |
| style string | The style used with Raster Flow Tiles and Vector Flow Tiles. This has an
effect on the coordinates in the response. Values: absolute relative relative0 relative0-dark relative-delay reduced-sensitivity |
| zoom integer | The zoom level. This has an effect on the following items: Traffic flow coordinates: There may be a slight deviation between
the provided coordinates on different zoom levels. Visibility of the particular road: Roads of lower importance are
only visible on zoom levels with a higher value. When Flow Segment data is used together with the Traffic Flow service,
the zoom should be the same in both calls. Values: 0..22 |
| format string | The content type of the response structure. If the content type is jsonp , a callback method can be specified at the end of the
service call. Values: xml json jsonp |
| key string | The authorization key for access to the API. Value: Your valid API Key . |
| point float | The coordinates of the point close to the road segment. They must be comma-separated and calculated using EPSG:4326 projection (also known as WGS84 ). Value: latitude,longitude |

**Request parameters**

| Optional parameters | Description |
| --- | --- |
| unit string | The unit of speed. Default value: kmph (kilometers per hour) Other value: mph (miles per hour) |
| thickness integer | The segment width multiplier. Default value: 10 Other values: 1..20 |
| openLr boolean | Specifies if the response should include OpenLR code. Default value: false Other value: true |
| jsonp string | Specifies the callback method. jsonp must be a valid JSONP callback name. Only used where the contentType parameter value is jsonp . Value: jsonp |

**Request headers**

| Optional headers | Description |
| --- | --- |
| Accept-Encoding | Contains the content encoding (usually a compression algorithm), that
the client is able to understand. Value: gzip |
| Tracking-ID | Specifies an identifier for the request. It can be used to trace a call.
The value must match the regular expression '^[a-zA-Z0-9-]{1,100}$' . An example of the format
that matches this regular expression is a UUID (e.g., 9ac68072-c7a4-11e8-a8d5-f2801f1b9fd1 ). For details check RFC 4122 . If specified, it is replicated in the Tracking-ID response header. It
is only meant to be used for support and does not involve tracking of
you or your users in any form. Value: <string> |

**Response data**

| Field | Description |
| --- | --- |
| <flowSegmentData> object | Main response element. The version attribute indicates the software version that
generated the response. |
| <frc> string | F unctional R oad C lass. This indicates the road
type: FRC0 : Motorway, freeway or other major road FRC1 : Major road, less important than a motorway FRC2 : Other major road FRC3 : Secondary road FRC4 : Local connecting road FRC5 : Local road of high importance FRC6 : Local road |
| <currentSpeed> integer | The current average speed at the selected point , in the unit requested. This is calculated from the currentTravelTime and the length of the selected segment. |
| <freeFlowSpeed> integer | The free flow speed expected under ideal conditions, expressed in the unit requested. This is related to the freeFlowTravelTime . |
| <currentTravelTime> integer | Current travel time in seconds based on fused real-time measurements
between the defined locations in the specified direction. |
| <freeFlowTravelTime> integer | The travel time in seconds which would be expected under ideal free flow
conditions. |
| <confidence> float | The confidence is a measure of the quality of the provided travel time
and speed. A value ranges between 0 and 1 where 1 means full confidence, meaning that the response
contains the highest quality data. Lower values indicate the degree that
the response may vary from the actual conditions on the road. |
| <coordinates> object | This includes the coordinates describing the shape of the segment.
Coordinates are shifted from the road depending on the zoom level to support high quality visualization in every scale. |
| <openlr> string | The OpenLR code for segment. |
| <roadClosure> boolean | This indicates if the road is closed to traffic or not. |

**Response data**

| Field | Description |
| --- | --- |
| detailedError object | Main object of the error response. |
| code string | One of a server-defined set of error codes. |
| message string | A human-readable description of the error code. |

**Response data**

| Code | Meaning & possible causes |
| --- | --- |
| 200 | OK |
| 400 | Bad request |
| 403 | Forbidden : The supplied API Key is not valid for this request. |
| 405 | Method Not Allowed : The provided HTTP request method is known by
the server, but is not supported by the target resource. |
| 429 | Too Many Requests : Too many requests were sent in a given amount
of time for the supplied API Key. |
| 500 | Internal Server Error |
| 503 | Service currently unavailable : The service is currently
unavailable. |
| 596 | Service Not Found : Unknown version of the service. |

**Response data**

| Header | Description |
| --- | --- |
| Access-Control-Allow-Origin | Indicates that cross-origin resource sharing (CORS) is allowed. Value: * |
| Allow | Lists the set of supported HTTP methods. The header is sent in case a 405 HTTP response code is returned. Value: GET , HEAD |
| Content-Encoding | Indicates which encodings were applied to the response body. Value: gzip |
| Cache-Control | Contains directives for a caching mechanism. Value: <public, max-age=0> |
| Content-Length | Contains information about the size of the response body. Value: <decimal number> |
| Content-Type | Indicates the media type of the resource returned. Values: <application/json; charset=utf-8> <application/javascript; charset=utf-8> <text/xml; charset=utf-8> |
| Date | Contains the date and time when the message was originated. Value: <http-date> |
| Tracking-ID | An identifier for the request. If the Tracking-ID header was specified
in the request, it is replicated in the response. Otherwise, it is
generated automatically by the service. For details check RFC 4122 . It is only meant to be used for support and does not involve tracking
of you or your users in any form. Value: <string> |

**Successful response**

| Field | Description |
| --- | --- |
| <flowSegmentData> object | Main response element. The version attribute indicates the software version that
generated the response. |
| <frc> string | F unctional R oad C lass. This indicates the road
type: FRC0 : Motorway, freeway or other major road FRC1 : Major road, less important than a motorway FRC2 : Other major road FRC3 : Secondary road FRC4 : Local connecting road FRC5 : Local road of high importance FRC6 : Local road |
| <currentSpeed> integer | The current average speed at the selected point , in the unit requested. This is calculated from the currentTravelTime and the length of the selected segment. |
| <freeFlowSpeed> integer | The free flow speed expected under ideal conditions, expressed in the unit requested. This is related to the freeFlowTravelTime . |
| <currentTravelTime> integer | Current travel time in seconds based on fused real-time measurements
between the defined locations in the specified direction. |
| <freeFlowTravelTime> integer | The travel time in seconds which would be expected under ideal free flow
conditions. |
| <confidence> float | The confidence is a measure of the quality of the provided travel time
and speed. A value ranges between 0 and 1 where 1 means full confidence, meaning that the response
contains the highest quality data. Lower values indicate the degree that
the response may vary from the actual conditions on the road. |
| <coordinates> object | This includes the coordinates describing the shape of the segment.
Coordinates are shifted from the road depending on the zoom level to support high quality visualization in every scale. |
| <openlr> string | The OpenLR code for segment. |
| <roadClosure> boolean | This indicates if the road is closed to traffic or not. |

**Error response**

| Field | Description |
| --- | --- |
| detailedError object | Main object of the error response. |
| code string | One of a server-defined set of error codes. |
| message string | A human-readable description of the error code. |

#### Examples & payloads

**GET Request URL**

```text
https://{baseURL}/traffic/services/{versionNumber}/flowSegmentData/{style}/{zoom}/{format}?key={Your_API_Key}&point={point}&unit={unit}&thickness={thickness}&openLr={boolean}&jsonp={jsonp}
```

**GET Example**

```text
https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/xml?key={Your_API_Key}&point=52.41072,4.84239
```

**GET curl command**

```text
curl 'https:/api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/xml?key={Your_API_Key}&point=52.41072,4.84239'
```

**Response body - XML**

```xml
<flowSegmentData xmlns="http://lbs.tomtom.com/services" version="traffic-service 2.0.004">
  <frc>FRC2</frc>
  <currentSpeed>41</currentSpeed>
  <freeFlowSpeed>70</freeFlowSpeed>
  <currentTravelTime>153</currentTravelTime>
  <freeFlowTravelTime>90</freeFlowTravelTime>
  <confidence>0.59</confidence>
  <roadClosure>true</roadClosure>
  <coordinates>
    <coordinate>
      <latitude>52.40476</latitude>
      <longitude>4.844318</longitude>
    </coordinate>
    <coordinate>
      <latitude>52.411312</latitude>
      <longitude>4.8299975</longitude>
    </coordinate>
    <coordinate>
      <latitude>52.415073</latitude>
      <longitude>4.827327</longitude>
    </coordinate>
  </coordinates>
</flowSegmentData>
```

**Response body - JSON**

```json
{
  "flowSegmentData": {
    "-xmlns": "http://lbs.tomtom.com/services",
    "-version": "traffic-service 2.0.004",
    "frc": "FRC2",
    "currentSpeed": 41,
    "freeFlowSpeed": 70,
    "currentTravelTime": 153,
    "freeFlowTravelTime": 90,
    "confidence": 0.59,
    "roadClosure": true,
    "coordinates": {
      "coordinate": [
        {
          "latitude": 52.40476,
          "longitude": 4.844318
        },
        {
          "latitude": 52.411312,
          "longitude": 4.8299975
        },
        {
          "latitude": 52.415073,
          "longitude": 4.827327
        }
      ]
    }
  }
}
```

**Error response example - JSON**

```json
{
  "error": "Missing point parameter.",
  "httpStatusCode": 400,
  "detailedError": {
    "code": "INVALID_REQUEST",
    "message": "Missing point parameter."
  }
}
```

### Raster Flow Tiles

- **Source**: `https://developer.tomtom.com/traffic-api/documentation/tomtom-maps/traffic-flow/raster-flow-tiles`

#### Tables

**Request parameters**

| Required parameters | Description |
| --- | --- |
| baseURL string | Base URL for calling TomTom services. Values: api.tomtom.com : The default global API endpoint. kr-api.tomtom.com : The region-specific endpoint for
South Korea. See the region-specific content documentation . |
| versionNumber string | Version of the service to call. Value: The current value is 4 . |
| style string | The style to be used to render the tile. When the style is absolute , the colors will reflect the absolute speed
measured. Calls using the relative , relative0 and relative0-dark styles return the speed relative to
free-flow, highlighting areas of congestion. Style relative-delay displays relative speeds only
where they are different from the free-flow speeds. Style reduced-sensitivity displays relative speeds, but
a larger difference from free-flow (depending on FRC) is required
for a segment to change the color. Styles relative0 and relative0-dark are
recommended to use. Values: absolute relative relative0 relative0-dark relative-delay reduced-sensitivity |
| zoom integer | Zoom level of the tile to be rendered. Value: 0..22 |
| x integer | x coordinate of the tile on the zoom grid. Value: 0..2 zoom -1 |
| y integer | y coordinate of tile on zoom grid. Value: 0..2 zoom -1 |
| format string | The format of the response. Value: png |
| apiKey string | API Key valid for requested service. Value: Your valid API Key . |

**Request parameters**

| Optional parameters | Description |
| --- | --- |
| thickness integer | The segment width multiplier. This parameter can only be used with the
following styles: absolute relative relative-delay reduced-sensitivity Value: 1..20 Default value: 10 |
| tileSize integer | The tile size dimension in pixels. Values: 256 512 Default value: 256 |

**Request headers**

| Optional headers | Description |
| --- | --- |
| Tracking-ID | Specifies an identifier for the request. It can be used to trace a call.
The value must match the regular expression '^[a-zA-Z0-9-]{1,100}$' . An example of the format
that matches this regular expression is a UUID (e.g., 9ac68072-c7a4-11e8-a8d5-f2801f1b9fd1 ). For details check RFC 4122 . If specified, it is replicated in the Tracking-ID response header. It is
only meant to be used for support and does not involve tracking of you
or your users in any form. Value: <string> |
| Accept | Advertises which content types, expressed as MIME types, the client is
able to understand. In this service, the header is used to specify a
preferred Bad Request response format. Format: Accept: type/subtype Accept: type/subtype, type/subtype - for multiple types Value: type/subtype is one of: image/png - in case of the 200 OK application/json - in case of the 400 Bad Request text/xml - in case of the 400 Bad Request Examples: Accept: application/json Accept: image/png, application/json |

**Response data**

| Field | Description |
| --- | --- |
| detailedError object | Main object of the error response. |
| code string | One of a server-defined set of error codes. |
| message string | A human-readable description of the error code. |

**Response data**

| Code | Meaning & possible causes |
| --- | --- |
| 200 | OK |
| 400 | Bad request Unknown style : The requested style is not available. zoom n is out of range [0,22] : The requested zoom level is out of the possible range. x n is out of range [0,2 zoom -1] : The requested x coordinate is out of the possible range. y n is out of range [0,2 zoom -1] : The requested y coordinate is out of the possible range. Unknown format: The requested format is not supported. Invalid  thickness  parameter value . Invalid combination of the style and  thickness
parameter . |
| 403 | Forbidden : The supplied API Key is not valid for this request. |
| 405 | Method Not Allowed : The provided HTTP request method is known by
the server, but is not supported by the target resource. |
| 429 | Too Many Requests : Too many requests were sent in a given amount
of time for the supplied API Key. |
| 500 | Internal Server Error . |
| 503 | Service currently unavailable . |
| 596 | Service Not Found : Unknown version of the service. |

**Response data**

| Header | Description |
| --- | --- |
| Access-Control-Allow-Origin | Indicates that cross-origin resource sharing (CORS) is allowed. Value: * |
| Allow | Lists the set of supported HTTP methods. The header is sent in case a 405 HTTP response code is returned. Values: GET , HEAD |
| Cache-Control | Contains directives for a caching mechanism. Values: private , no-cache , no-store , max-age=0 , must-revalidate |
| Content-Length | Contains information about the size of the response body. Value: <decimal number> |
| Content-Type | Indicates the media type of the resource returned. Values: image/png - in case of the 200 OK application/json; charset=utf-8 - in case of the 400 Bad Request text/xml; charset=utf-8 - in case of the 400 Bad Request |
| Date | Contains the date and time when the message was originated. Value: <http-date> |
| Tracking-ID | An identifier for the request. If the Tracking-ID header was specified in
the request, it is replicated in the response. Otherwise, it is
generated automatically by the service. For details check RFC 4122 . It is only meant to be used for support and does not involve tracking
of you or your users in any form. Value: <string> |

**Error response**

| Field | Description |
| --- | --- |
| detailedError object | Main object of the error response. |
| code string | One of a server-defined set of error codes. |
| message string | A human-readable description of the error code. |

#### Examples & payloads

**GET Request URL**

```text
https://{baseURL}/traffic/map/{versionNumber}/tile/flow/{style}/{zoom}/{x}/{y}.{format}?key={Your_API_Key}&thickness={thickness}&tileSize={tileSize}
```

**GET Example**

```text
https://api.tomtom.com/traffic/map/4/tile/flow/absolute/12/2044/1360.png?key={Your_API_Key}
```

**GET curl command**

```text
curl 'https://{baseURL}/traffic/map/{versionNumber}/tile/flow/{style}/{zoom}/{x}/{y}.{format}?key={Your_API_Key}&thickness={thickness}&tileSize={tileSize}'
```

**Error response example - XML**

```xml
<errorResponse errorCode="400" description="z out of range 0 <= z <= 22" version="traffic-rasterizer 2.0.009">
  <detailedError>
    <code>INVALID_REQUEST</code>
    <message>z out of range 0 <= z <= 22</message>
  </detailedError>
</errorResponse>
```

**Error response example - JSON**

```json
{
  "detailedError": {
    "code": "INVALID_REQUEST",
    "message": "z out of range 0 <= z <= 22"
  }
}
```

### Vector Flow Tiles

- **Source**: `https://developer.tomtom.com/traffic-api/documentation/tomtom-maps/traffic-flow/vector-flow-tiles`

#### Tables

**Request parameters**

| Required parameters | Description |
| --- | --- |
| baseURL string | The base URL for calling TomTom services. Values: api.tomtom.com : The default global API endpoint. [a\|b\|c\|d].api.tomtom.com : The default global API
endpoint (see the Host Name Cycling section for
details on aliases). kr-api.tomtom.com : The region-specific endpoint for
South Korea. See the region-specific content documentation . |
| versionNumber string | The version of the service to call. Value: The current value is 4 . |
| type | Types of traffic flow. See the Traffic flow types section for
details. Value: absolute relative relative-delay |
| zoom integer | The zoom level of a tile to be rendered. Value: 0 .. 22 |
| x integer | The x coordinate of a tile on the zoom grid. Value: 0..2 zoom -1 |
| y integer | The y coordinate of a tile on the zoom grid. Value: 0..2 zoom -1 |
| format string | The format of the response. Value: pbf ( Protocolbuffer Binary Format ) |
| key string | An API Key valid for the requested service. Value: Your valid API Key . |

**Request parameters**

| Optional parameters | Description |
| --- | --- |
| roadTypes array | The list of values representing the road types, which are going to be
displayed on a particular zoom level according to the mapping: 0 : Motorway 1 : International road 2 : Major road 3 : Secondary road 4 : Connecting road 5 : Major local road 6 : Local road 7 : Minor local road 8 : Other roads (Non public road, Parking road, etc.) The list of values must be enclosed in square brackets [ ] ,
and each value must be separated by a comma. The parameter behaves as a filter,
narrowing down the road types displayed for a particular zoom level. If the
array of parameters is empty, an empty tile will be sent. Value: Square brackets [ ] enclosed list/array. |
| trafficLevelStep positive float | The step value, describing the minimum difference between values of the traffic_level protobuf tag. For example: In the case of the relative traffic type, for trafficLevelStep to equal 0.1 , the allowed
values of traffic_level are: 0.0 , 0.1 , 0.2 .. 1.0 In the case of the absolute traffic type, for trafficLevelStep to equal 10 , the allowed
values of traffic_level are: 0 , 10 , 20 , etc. Values: for relative and relative-delay traffic
types: 0.0 < trafficLevelStep < 1.0 for absolute traffic type: 0 < trafficLevelStep |
| margin fractional float | The size of the tile margin, relative to the tile size. Value: 0.0 .. 0.1 Default value: 0.1 |
| tags array | The list of the values representing the available tags in the tile: road_type traffic_level traffic_road_coverage left_hand_traffic road_closure road_category road_subcategory By default, only the default tags are attached to the tile geometry. See
the Vector format for details. The list of the values must be enclosed in square brackets [ ] (an array), and each value must be separated by a
comma. The parameter behaves as a filter by narrowing down the list of tags
enclosed in each tile. It also allows a decrease in the size of the
tile. If the array of parameters is empty, only the geometry will be sent. Value: Square brackets enclosed list/array. |

**Request headers**

| Optional headers | Description |
| --- | --- |
| Accept-Encoding | Contains the content encoding (usually a compression algorithm), that
the client is able to understand. Value: gzip |
| If-None-Match | Contains an identifier for a specific version of a resource. The server
will send back the requested resource with a 200 HTTP status code, only
if it doesn't have an ETag matching the given one. Value: <string> |
| Tracking-ID | Specifies an identifier for the request. It can be used to trace a call.
The value must match the regular expression '^[a-zA-Z0-9-]{1,100}$' . An example of the format
that matches this regular expression is a UUID (e.g., 9ac68072-c7a4-11e8-a8d5-f2801f1b9fd1 ). For details check RFC 4122 . If specified, it is replicated in the Tracking-ID response header. It is
only meant to be used for support and does not involve tracking of you
or your users in any form. Value: <string> |

**Response data**

| Field | Description |
| --- | --- |
| detailedError object | Main object of the error response. |
| code string | One of a server-defined set of error codes. |
| message string | A human-readable description of the error code. |

**Response data**

| Code | Meaning & possible causes |
| --- | --- |
| 200 | OK |
| 400 | Bad request : The combination of layer, type, and query parameters is not
supported. zoom n is out of range [0,22]: The requested zoom level is out of the possible range. x n is out of range [0,2 zoom -1]: The requested x coordinate is out of the possible range. y n is out of range [0,2 zoom -1]: The requested y coordinate is out of the possible range. |
| 403 | Forbidden : The supplied API Key is not valid for this request. |
| 405 | Method Not Allowed : The provided HTTP request method is known by
the server, but is not supported by the target resource. |
| 429 | Too Many Requests : Too many requests were sent in a given amount
of time for the supplied API Key. |
| 500 | Internal Server Error : There is a problem with the TomTom Traffic
Vector Flow Tiles API endpoint. |
| 503 | Service currently unavailable . |
| 596 | Service Not Found : Unknown version of the service. |

**Response data**

| Header | Description |
| --- | --- |
| Access-Control-Allow-Origin | Indicates that cross-origin resource sharing (CORS) is allowed. Value: * universal. |
| Allow | Lists the set of supported HTTP methods. The header is sent in case a 405 HTTP response code is returned. Value: GET , HEAD |
| Content-Encoding | Indicates which encodings were applied to the response body. Value: gzip |
| Content-Length | Contains information about the size of the response body. Value: decimal number |
| Content-Type | Indicates the media type of the resource returned. Value: image/pbf |
| Date | Contains the date and time when the message was originated. Value: http-date |
| ETag | Contains an identifier for a specific version of resource. Value: W/"2fdbd61f30456" |
| Expires | Contains the date after which the response is considered outdated. Value: http-date |
| Tracking-ID | An identifier for the request. If the Tracking-ID header was specified in
the request, it is replicated in the response. Otherwise, it is
generated automatically by the service. For details check RFC 4122 . It is only meant to be used for support and does not involve tracking
of you or your users in any form. Value: <string> |

**Error response**

| Field | Description |
| --- | --- |
| detailedError object | Main object of the error response. |
| code string | One of a server-defined set of error codes. |
| message string | A human-readable description of the error code. |

#### Examples & payloads

**GET Generic request URL**

```text
https://{baseURL}/traffic/map/{versionNumber}/tile/flow/{type}/{zoom}/{x}/{y}.{format}?key={Your_API_Key}&roadTypes={roadTypes[]}
```

**GET Example**

```text
https://api.tomtom.com/traffic/map/4/tile/flow/relative/5/4/8.pbf?key={Your_API_Key}&roadTypes={[2,4,5]}
```

**GET curl command**

```text
curl 'https://api.tomtom.com/traffic/map/4/tile/flow/relative/5/4/8.pbf?key={Your_API_Key}&roadTypes={[2,4,5]&trafficLevelStep={trafficLevelStep}&margin={margin}&tags={[tags]}'
```

**GET Request URL using a.api.tomtom.com**

```text
https://a.api.tomtom.com/traffic/map/4/tile/flow/relative/1/0/0.pbf?key={Your_API_Key}
```

**GET Request URL using b.api.tomtom.com**

```text
https://b.api.tomtom.com/traffic/map/4/tile/flow/relative/1/0/0.pbf?key={Your_API_Key}
```

**GET Request example - Absolute Flow Type**

```text
https://api.tomtom.com/map/4/tile/flow/absolute/17/64989/42178.pbf?key={Your_API_Key}
```

**Response example - Absolute Flow Type**

```text
layer: 0
    name: Traffic flow
    version: 2
    extent: 4096
    keys:
      0: road_type
      1: traffic_level
      2: traffic_road_coverage
      3: left_hand_traffic
    values:
      0: "Major local road" [string]
      1: 0 [double]
      2: "one_side" [string]
      3: 1 [bool]
      4: "Major road" [string]
      5: 45 [double]
      6: 1 [bool]
      7: 50 [double]
      8: 1 [bool]
    feature: 0
      id: (none)
      geomtype: linestring
      geometry:
        LINESTRING[count=3](3002 -409,2964 1292,2842 2382)
        LINESTRING[count=3](2842 2382,2964 1292,3002 -409)
      properties:
        road_type="Major local road" [string]
        traffic_level=0 [double]
        traffic_road_coverage="one_side" [string]
        left_hand_traffic=1 [bool]
    feature: 1
      id: (none)
      geomtype: linestring
      geometry:
        LINESTRING[count=7](4222 4505,4122 4366,3528 3882,3062 3494,2826 2932,2806 2752,2842 2382)
        LINESTRING[count=8](-409 656,-108 810,1260 1620,1832 1914,2842 2382,3792 2644,4400 2770,4505 2783)
      properties:
        road_type="Major road" [string]
        traffic_level=45 [double]
        traffic_road_coverage="one_side" [string]
        left_hand_traffic=1 [bool]
    feature: 2
      id: (none)
      geomtype: linestring
      geometry:
        LINESTRING[count=7](2842 2382,2806 2752,2826 2932,3062 3494,3528 3882,4122 4366,4222 4505)
        LINESTRING[count=10](4505 2766,4418 2752,3882 2660,3406 2552,2920 2430,2700 2308,2276 2114,1952 1958,940 1430,-409 648)
      properties:
        road_type="Major road" [string]
        traffic_level=50 [double]
        traffic_road_coverage="one_side" [string]
        left_hand_traffic=1 [bool]
```

**GET Request example - Relative Flow Type**

```text
https://api.tomtom.com/map/4/tile/flow/relative/17/64989/42178.pbf?key={Your_API_Key}
```

**Response example - Relative Flow Type**

```text
layer: 0
    name: Traffic flow
    version: 2
    extent: 4096
    keys:
      0: road_type
      1: traffic_level
      2: traffic_road_coverage
      3: left_hand_traffic
    values:
      0: "Major local road" [string]
      1: 0 [double]
      2: "one_side" [string]
      3: 1 [bool]
      4: "Major road" [string]
      5: 0.7 [double]
      6: 1 [bool]
      7: 0.767 [double]
      8: 1 [bool]
      9: 1 [double]
      10: 1 [bool]
    feature: 0
      id: (none)
      geomtype: linestring
      geometry:
        LINESTRING[count=3](3002 -409,2964 1292,2842 2382)
        LINESTRING[count=3](2842 2382,2964 1292,3002 -409)
      properties:
        road_type="Major local road" [string]
        traffic_level=0 [double]
        traffic_road_coverage="one_side" [string]
        left_hand_traffic=1 [bool]
    feature: 1
      id: (none)
      geomtype: linestring
      geometry:
        LINESTRING[count=8](-409 656,-108 810,1260 1620,1832 1914,2842 2382,3792 2644,4400 2770,4505 2783)
      properties:
        road_type="Major road" [string]
        traffic_level=0.7 [double]
        traffic_road_coverage="one_side" [string]
        left_hand_traffic=1 [bool]
    feature: 2
      id: (none)
      geomtype: linestring
      geometry:
        LINESTRING[count=10](4505 2766,4418 2752,3882 2660,3406 2552,2920 2430,2700 2308,2276 2114,1952 1958,940 1430,-409 648)
      properties:
        road_type="Major road" [string]
        traffic_level=0.767 [double]
        traffic_road_coverage="one_side" [string]
        left_hand_traffic=1 [bool]
    feature: 3
      id: (none)
      geomtype: linestring
      geometry:
        LINESTRING[count=7](2842 2382,2806 2752,2826 2932,3062 3494,3528 3882,4122 4366,4222 4505)
        LINESTRING[count=7](4222 4505,4122 4366,3528 3882,3062 3494,2826 2932,2806 2752,2842 2382)
      properties:
        road_type="Major local road" [string]
        traffic_level=1 [double]
        traffic_road_coverage="one_side" [string]
        left_hand_traffic=1 [bool]
```

**GET Request example - Relative Delay Flow Type**

```text
https://api.tomtom.com/map/4/tile/flow/relative-delay/17/64989/42178.pbf?key={Your_API_Key}
```

**Response example - Relative Delay Flow Type**

```text
layer: 0
    name: Traffic flow
    version: 2
    extent: 4096
    keys:
      0: road_type
      1: traffic_level
      2: traffic_road_coverage
      3: left_hand_traffic
    values:
      0: "Major local road" [string]
      1: 0 [double]
      2: "one_side" [string]
      3: 1 [bool]
      4: "Major road" [string]
      5: 0.694 [double]
      6: 1 [bool]
      7: 0.767 [double]
      8: 1 [bool]
    feature: 0
      id: (none)
      geomtype: linestring
      geometry:
        LINESTRING[count=3](3002 -409,2964 1292,2842 2382)
        LINESTRING[count=3](2842 2382,2964 1292,3002 -409)
      properties:
        road_type="Major local road" [string]
        traffic_level=0 [double]
        traffic_road_coverage="one_side" [string]
        left_hand_traffic=1 [bool]
    feature: 1
      id: (none)
      geomtype: linestring
      geometry:
        LINESTRING[count=8](-409 656,-108 810,1260 1620,1832 1914,2842 2382,3792 2644,4400 2770,4505 2783)
      properties:
        road_type="Major road" [string]
        traffic_level=0.694 [double]
        traffic_road_coverage="one_side" [string]
        left_hand_traffic=1 [bool]
    feature: 2
      id: (none)
      geomtype: linestring
      geometry:
        LINESTRING[count=10](4505 2766,4418 2752,3882 2660,3406 2552,2920 2430,2700 2308,2276 2114,1952 1958,940 1430,-409 648)
      properties:
        road_type="Major road" [string]
        traffic_level=0.767 [double]
        traffic_road_coverage="one_side" [string]
        left_hand_traffic=1 [bool]
```

**Error response example - JSON**

```json
{
  "error": "Invalid zoom value. Allowed values are <0,22>.",
  "httpStatusCode": 400,
  "detailedError": {
    "code": "INVALID_REQUEST",
    "message": "Invalid zoom value. Allowed values are <0,22>."
  }
}
```

## TomTom Orbis Maps endpoints

### Incident Details

- **Source**: `https://developer.tomtom.com/traffic-api/documentation/tomtom-orbis-maps/traffic-incidents/incident-details`

#### Tables

**Request parameters**

| Required parameters | Description |
| --- | --- |
| baseURL string | The base URL for calling the API. Value: api.tomtom.com |
| bbox float,float,float,float | The corners of the area to report on, expressed in the EPSG:4326 projection. These are two longitude-latitude pairs describing the corners of the
bounding box. The first pair is for the lower-left corner and the second pair for
the upper-right corner. All values should be separated by a comma. The maximum area of a bounding box is 10,000 km 2 . This parameter is mutually exclusive with the ids
parameter. This parameter is available only for GET requests. Values: minLon,minLat,maxLon,maxLat |
| ids string | Comma separated list of incidents IDs. The maximum number of incidents IDs is 5 for GET requests. This parameter is mutually exclusive with the bbox parameter. This parameter is available only for GET requests. Value: A comma separated string |
| key string | The authorization key for access to the API. Value: Your valid API Key. |

**Request parameters**

| Optional parameters | Description |
| --- | --- |
| fields string | The fields to be included in the response, nested as in the response
schema. In order to obtain all data, it is necessary to place the whole
object in the query. get Default value {
  incidents
    {
      type,
      geometry{
        type,coordinates
      },
      properties{
        iconCategory
      }
    }
} 1 { 2 incidents 3 { 4 type , 5 geometry { 6 type , coordinates 7 } , 8 properties { 9 iconCategory 10 } 11 } 12 } get Value with all available fields {
  incidents{
    type,
    geometry{
      type,
      coordinates
    },
    properties{
      id,
      iconCategory,
      magnitudeOfDelay,
      events{
        description,
        code,
        iconCategory
      },
      startTime,
      endTime,
      from,
      to,
      length,
      delay,
      roadNumbers,
      timeValidity,
      probabilityOfOccurrence,
      numberOfReports,
      lastReportTime
      tmc{
        countryCode,
        tableNumber,
        tableVersion,
        direction,
        points{
          location,
          offset
        }
      }
    }
  }
} 1 { 2 incidents { 3 type , 4 geometry { 5 type , 6 coordinates 7 } , 8 properties { 9 id , 10 iconCategory , 11 magnitudeOfDelay , 12 events { 13 description , 14 code , 15 iconCategory 16 } , 17 startTime , 18 endTime , 19 from , 20 to , 21 length , 22 delay , 23 roadNumbers , 24 timeValidity , 25 probabilityOfOccurrence , 26 numberOfReports , 27 lastReportTime 28 tmc { 29 countryCode , 30 tableNumber , 31 tableVersion , 32 direction , 33 points { 34 location , 35 offset 36 } 37 } 38 } 39 } 40 } |
| language string | The language code for the output language.
Affects the description fields in the response.
When an incident description does not have a
translation, an English description is returned. Default value: en-GB Allowed values: List of supported languages . |
| t string | The Traffic Model ID is the reference value for the state of traffic at
a particular time. It is updated every minute, and is valid for two
minutes before it times out. See the HTTP response headers section and Traffic Model ID page for
more information. Default value: current Traffic Model ID Allowed value: Traffic_Model_ID |
| categoryFilter string | This filter allows the choice of types of incidents and future incidents
to be included in the response. Filtering takes into account the main icon category of the incident.
Both value types can be used: numeric and descriptive strings. Multiple
values are supported and should be separated by a comma. Default values: 0,1,2,3,4,5,6,7,8,9,10,11,14 Allowed values: 0 : Unknown 1 : Accident 2 : Fog 3 : DangerousConditions 4 : Rain 5 : Ice 6 : Jam 7 : LaneClosed 8 : RoadClosed 9 : RoadWorks 10 : Wind 11 : Flooding 14 : BrokenDownVehicle |
| timeValidityFilter string | This filter allows the choice of incidents based on their occurrence in
time. Multiple values are supported and they should be separated by a
comma. Default value: present Allowed values: present future |
| apiVersion string | Contains a version of the API to call. Value: The current version is 1 . |

**Request headers**

| Required headers | Description |
| --- | --- |
| TomTom-Api-Version | Contains a version of the API to call. Value: The current version is 1 . |

**Request headers**

| Optional headers | Description |
| --- | --- |
| Accept-Encoding | Contains the content encoding (usually a compression algorithm),
that the client is able to understand. It is strongly
recommended using this header in order to limit
bandwidth usage. Value: gzip |
| Tracking-ID | Specifies an identifier for the request. It can be used to trace a call. The value must match the regular expression '^[a-zA-Z0-9-]{1,100}$' . An example of the format that matches this regular expression is a UUID (e.g., 9ac68072-c7a4-11e8-a8d5-f2801f1b9fd1 ). For details check RFC 4122 . If specified, it is replicated in the Tracking-ID response header. It is only meant to be used for support and does not involve
tracking of you or your users in any form. Value: <string> |

**Response data**

| Field | Description |
| --- | --- |
| incidents object | Incidents which belong to or intersect with
the given bounding box. |

**Response data**

| Field | Description |
| --- | --- |
| type string | The value is set as Feature ( GeoJSON feature object). |
| geometry object | A GeoJSON feature of type Point or Linestring (depending
on the incident). It always contains the type and coordinates fields. |
| properties object | The properties of a particular incident. |

**Response data**

| Field | Description |
| --- | --- |
| id string | The ID of the traffic incident, common among
Traffic Incident API services where it is available. |
| iconCategory integer | The main icon category associated with this incident.
This is an icon category associated with the first
event in the events list describing the incident.
The values meaning: 0 : Unknown 1 : Accident 2 : Fog 3 : Dangerous Conditions 4 : Rain 5 : Ice 6 : Jam 7 : Lane Closed 8 : Road Closed 9 : Road Works 10 : Wind 11 : Flooding 14 : Broken Down Vehicle |
| magnitudeOfDelay integer | The magnitude of delay associated with an incident. The values meaning: 0 : Unknown 1 : Minor 2 : Moderate 3 : Major 4 : Undefined (used for road closures and other
indefinite delays) |
| events object | The list of events describing the details of the
incident in the language requested. Traffic
incident can be described with more than one Event object. |
| startTime string | Start time of the incident, if available.
The date is described in the ISO8601 format. |
| endTime string | End time of the incident, if available.
The date is described in the ISO8601 format. |
| from string | The name of the location where the traffic
due to the incident starts. |
| to string | The name of the location where the traffic
due to the incident ends. |
| length float | The length of the incident in meters. |
| delay integer | The delay in seconds caused by the incident
(except road closures). It is calculated against
free-flow travel time (the travel time when the
traffic is minimal, e.g., night traffic). |
| roadNumbers array of strings | The road number(s) affected by the incident. |
| timeValidity string | Enumeration string describing if the incident
occurrence is now or in the future. |
| tmc object | TMC (Traffic Message Channel) data of the
traffic incident, needed to determine its location. |
| probabilityOfOccurrence string | Enumeration string specifying the likelihood
of the occurring incident. Allowed values: certain probable risk_of improbable |
| numberOfReports integer | The number of reports given by actual end-users. |
| lastReportTime string | The date in ISO8601 format, when the last time the incident was reported. Gives
the user confidence that the incident is fresh. |

**Response data**

| Field | Description |
| --- | --- |
| description string | The description of the event (being part of incident)
in the requested language. |
| code integer | The predefined alert code, describing the event
(part of incident). |
| iconCategory integer | The icon category associated with the event.
The icon category from the first event in the list
is replicated in the iconCategory field in the IncidentProperties object. |

**Response data**

| Field | Description |
| --- | --- |
| detailedError object | Main object of the error response. |
| code string | One of a server-defined set of error codes. |
| message string | A human-readable description of the error code. |

**Response data**

| Code | Meaning & possible causes |
| --- | --- |
| 200 | OK |
| 400 | Bad request: Usually due to a malformed syntax or incorrect
format of Traffic Model ID. |
| 403 | Forbidden: The supplied API Key is not valid for this request. |
| 405 | Method Not Allowed: The provided HTTP request method is known by
the server, but is not supported by the target resource. |
| 429 | Too Many Requests: Too many requests were sent in a given amount
of time for the supplied API Key. |
| 500 | Internal Server Error |

**Response data**

| Header | Description |
| --- | --- |
| Access-Control-Allow-Origin | Indicates that cross-origin resource sharing (CORS) is allowed. Value: * |
| Allow | Lists the set of supported HTTP methods. The header is sent in case a 405 HTTP response code is returned. Values: GET , POST , HEAD |
| Content-Encoding | Indicates which encodings were applied to the response body. Value: gzip |
| Content-Length | Contains information about the size of the response body. Value: <decimal number> |
| Content-Type | Indicates the media type of the resource returned. Value: <application/json; charset=utf-8> |
| Date | Contains the date and time when the message was originated. Value: <http-date> |
| TrafficModelID | Contains the reference value for the state of traffic at a particular
time. If the request contains a valid Traffic Model ID, its value is
replicated here. If the request does not contain a Traffic Model ID, or
it contains outdated data, then the most recent one is returned. Value: <numeric> |
| Tracking-ID | An identifier for the request. If the Tracking-ID header was specified in the request, it is replicated in the response. Otherwise, it is generated automatically by the service. For details check RFC 4122 . It is only meant to be used for support and does not involve tracking of you or your users in any form. Value: <string> |

**Successful response**

| Field | Description |
| --- | --- |
| incidents object | Incidents which belong to or intersect with
the given bounding box. |

**Successful response**

| Field | Description |
| --- | --- |
| type string | The value is set as Feature ( GeoJSON feature object). |
| geometry object | A GeoJSON feature of type Point or Linestring (depending
on the incident). It always contains the type and coordinates fields. |
| properties object | The properties of a particular incident. |

**Successful response**

| Field | Description |
| --- | --- |
| id string | The ID of the traffic incident, common among
Traffic Incident API services where it is available. |
| iconCategory integer | The main icon category associated with this incident.
This is an icon category associated with the first
event in the events list describing the incident.
The values meaning: 0 : Unknown 1 : Accident 2 : Fog 3 : Dangerous Conditions 4 : Rain 5 : Ice 6 : Jam 7 : Lane Closed 8 : Road Closed 9 : Road Works 10 : Wind 11 : Flooding 14 : Broken Down Vehicle |
| magnitudeOfDelay integer | The magnitude of delay associated with an incident. The values meaning: 0 : Unknown 1 : Minor 2 : Moderate 3 : Major 4 : Undefined (used for road closures and other
indefinite delays) |
| events object | The list of events describing the details of the
incident in the language requested. Traffic
incident can be described with more than one Event object. |
| startTime string | Start time of the incident, if available.
The date is described in the ISO8601 format. |
| endTime string | End time of the incident, if available.
The date is described in the ISO8601 format. |
| from string | The name of the location where the traffic
due to the incident starts. |
| to string | The name of the location where the traffic
due to the incident ends. |
| length float | The length of the incident in meters. |
| delay integer | The delay in seconds caused by the incident
(except road closures). It is calculated against
free-flow travel time (the travel time when the
traffic is minimal, e.g., night traffic). |
| roadNumbers array of strings | The road number(s) affected by the incident. |
| timeValidity string | Enumeration string describing if the incident
occurrence is now or in the future. |
| tmc object | TMC (Traffic Message Channel) data of the
traffic incident, needed to determine its location. |
| probabilityOfOccurrence string | Enumeration string specifying the likelihood
of the occurring incident. Allowed values: certain probable risk_of improbable |
| numberOfReports integer | The number of reports given by actual end-users. |
| lastReportTime string | The date in ISO8601 format, when the last time the incident was reported. Gives
the user confidence that the incident is fresh. |

**Successful response**

| Field | Description |
| --- | --- |
| description string | The description of the event (being part of incident)
in the requested language. |
| code integer | The predefined alert code, describing the event
(part of incident). |
| iconCategory integer | The icon category associated with the event.
The icon category from the first event in the list
is replicated in the iconCategory field in the IncidentProperties object. |

**Error response**

| Field | Description |
| --- | --- |
| detailedError object | Main object of the error response. |
| code string | One of a server-defined set of error codes. |
| message string | A human-readable description of the error code. |

#### Examples & payloads

**GET Request URL format with bounding box**

```text
https://{baseURL}/maps/orbis/traffic/incidentDetails?apiVersion=1&key={Your_Api_Key}&bbox={bbox}&fields={fields}&language={language}&t={t}&categoryFilter={categoryFilter}&timeValidityFilter={timeValidityFilter}
```

**GET Request URL format with IDs**

```text
https://{baseURL}/maps/orbis/traffic/incidentDetails?apiVersion=1&key={Your_Api_Key}&ids={ids}&fields={fields}&language={language}&t={t}&categoryFilter={categoryFilter}&timeValidityFilter={timeValidityFilter}
```

**GET Request URL example with bounding box**

```text
https://api.tomtom.com/maps/orbis/traffic/incidentDetails?apiVersion=1&key={Your_Api_Key}&bbox=4.8854592519716675,52.36934334773164,4.897883244144765,52.37496348620152&fields={incidents{type,geometry{type,coordinates},properties{iconCategory}}}&language=en-GB&t=1111&timeValidityFilter=present
```

**GET Request URL example with IDs**

```text
https://api.tomtom.com/maps/orbis/traffic/incidentDetails?apiVersion=1&key={Your_Api_Key}&ids=4819f7d0a15db3d9b0c3cd9203be7ba5&fields={incidents{type,geometry{type,coordinates},properties{iconCategory}}}&language=en-GB&t=1111&timeValidityFilter=present
```

**GET Request curl command example with boundingbox**

```text
curl 'https://api.tomtom.com/maps/orbis/traffic/incidentDetails?apiVersion=1&key={Your_Api_Key}&bbox=4.8854592519716675,52.36934334773164,4.897883244144765,52.37496348620152&fields={incidents{type,geometry{type,coordinates},properties{iconCategory}}}&language=en-GB&t=1111&timeValidityFilter=present'
```

**GET Request curl command example with IDs**

```text
curl 'https://api.tomtom.com/maps/orbis/traffic/incidentDetails?apiVersion=1&key={Your_Api_Key}&ids=4819f7d0a15db3d9b0c3cd9203be7ba5&fields={incidents{type,geometry{type,coordinates},properties{iconCategory}}}&language=en-GB&t=1111&timeValidityFilter=present'
```

**GET Request URL example with category filter**

```text
https://api.tomtom.com/maps/orbis/traffic/incidentDetails?apiVersion=1&key={Your_Api_Key}&bbox=4.8854592519716675,52.36934334773164,4.897883244144765,52.37496348620152&fields={incidents{type,geometry{type,coordinates},properties{iconCategory}}}&language=en-GB&t=1111&categoryFilter=Accident&timeValidityFilter=present
```

**GET Request curl command with category filter**

```text
curl 'https://api.tomtom.com/maps/orbis/traffic/incidentDetails?apiVersion=1&key={Your_Api_Key}&bbox=4.8854592519716675,52.36934334773164,4.897883244144765,52.37496348620152&fields={incidents{type,geometry{type,coordinates},properties{iconCategory}}}&language=en-GB&t=1111&categoryFilter=Accident&timeValidityFilter=present'
```

**POST Request URL format**

```text
https://{baseURL}/maps/orbis/traffic/incidentDetails?apiVersion=1&key={Your_Api_Key}&fields={fields}&language={language}&t={t}&categoryFilter={categoryFilter}&timeValidityFilter={timeValidityFilter}
```

**POST Request URL example with fields**

```text
https://api.tomtom.com/maps/orbis/traffic/incidentDetails?apiVersion=1&key={Your_Api_Key}&fields={incidents{type,geometry{type,coordinates},properties{iconCategory}}}&language=en-GB&t=1111&timeValidityFilter=present
```

**POST Request curl command example with fields**

```text
curl -X POST 'https://api.tomtom.com/maps/orbis/traffic/incidentDetails?apiVersion=1&key={Your_Api_Key}&fields={incidents{type,geometry{type,coordinates},properties{iconCategory}}}&language=en-GB&t=1111&timeValidityFilter=present -d '{
    "ids": [
        "4819f7d0a15db3d9b0c3cd9203be7ba5"
    ]
}'
```

**GET Default value**

```json
{
  incidents
    {
      type,
      geometry{
        type,coordinates
      },
      properties{
        iconCategory
      }
    }
}
```

**GET Value with all available fields**

```json
{
  incidents{
    type,
    geometry{
      type,
      coordinates
    },
    properties{
      id,
      iconCategory,
      magnitudeOfDelay,
      events{
        description,
        code,
        iconCategory
      },
      startTime,
      endTime,
      from,
      to,
      length,
      delay,
      roadNumbers,
      timeValidity,
      probabilityOfOccurrence,
      numberOfReports,
      lastReportTime
      tmc{
        countryCode,
        tableNumber,
        tableVersion,
        direction,
        points{
          location,
          offset
        }
      }
    }
  }
}
```

**Request body**

```json
{
    ids: [String!]!
}
```

**type Query**

```text
type Query {
  incidents : [Incident!]!
}
```

**type Query**

```text
type Query {
  incidents : [Incident]!
}
```

**type Incident**

```text
type Incident {
    type: GeojsonFeatureType!
    geometry : GeojsonGeometry!
    properties: IncidentProperties!
}
```

**type IncidentProperties, Event, GeojsonGeometry, GeojsonLinestring, Aci**

```text
type IncidentProperties {
    id : String!
    iconCategory  : Int!
    magnitudeOfDelay : Int!
    events : [Event!]!
    startTime : String
    endTime : String
    from : String
    to : String
    length : Float!
    delay : Int
    roadNumbers : [String!]!
    timeValidity : TimeValidity!
    probabilityOfOccurrence : ProbabilityOfOccurrence!
    numberOfReports : Int
    lastReportTime : String
    tmc : Tmc
}

type Event {
    description : String!
    code : Int!
    iconCategory : Int!
}

union GeojsonGeometry = GeojsonPoint | GeojsonLinestring

type GeojsonPoint {
    type : GeojsonPointType!
    coordinates : [Float!]!
}

type GeojsonLinestring {
    type : GeojsonLinestringType!
    coordinates : [[Float!]!]!
}

enum GeojsonLinestringType {
    LineString
}

enum GeojsonPointType {
    Point
}

enum GeojsonFeatureType {
    Feature
}

enum ProbabilityOfOccurrence {
    certain
    probable
    risk_of
    improbable
}

type Tmc {
    countryCode: String!
    tableNumber: String!
    tableVersion: String!
    direction: Direction!
    points [TmcPoint!]!
}

enum Direction {
    positive
    negative
}

type TmcPoint {
    location : Int!
    offset: Int
}

enum TimeValidity {
    present
    future
}
```

**Response example - JSON**

```json
{
  "incidents": [
    {
      "type": "Feature",
      "properties": {
        "iconCategory": 8
      },
      "geometry": {
        "type": "LineString",
        "coordinates": [
          [4.8905266414, 52.3725919469],
          [4.8905306647, 52.372535656],
          [4.8905360291, 52.3724806443],
          [4.8905387113, 52.3724028603],
          [4.8905440757, 52.3723505607],
          [4.8905467579, 52.3722754886],
          [4.8905574868, 52.3721722195],
          [4.8905762622, 52.3719066767],
          [4.8905963788, 52.371663905],
          [4.8905936966, 52.371524454],
          [4.8905749211, 52.3714278871],
          [4.8905440757, 52.3713393544],
          [4.8905065248, 52.3712669418],
          [4.8904555628, 52.3711703743],
          [4.8904166708, 52.3711100387],
          [4.8903268168, 52.3709759593],
          [4.8901725898, 52.370765372],
          [4.8900062928, 52.370581651],
          [4.8899472842, 52.3705320104]
        ]
      }
    }
  ]
}
```

**Response example with available fields - JSON**

```json
{
  "incidents" : [
    {
      "type" : "Feature",
      "properties" : {
        "id":"4819f7d0a15db3d9b0c3cd9203be7ba5",
        "iconCategory" : 8,
        "magnitudeOfDelay" : 4,
        "startTime" : "2021-02-02T15:37:00Z",
        "endTime" : "2021-04-30T22:00:00Z",
        "from" : "Paleisstraat",
        "to" : "Rosmarijnsteeg",
        "length" : 238.553,
        "delay" : 0,
        "roadNumbers" : [],
        "timeValidity" : "present",
        "events" : [
          {
            "code" : 401,
            "description" : "Closed",
            "iconCategory" : 8
          }
        ],
        "tmc" : null
	"probabilityOfOccurrence" : "certain",
	"numberOfReports" : "null",
	"lastReportTime" : "null"
      },
      "geometry" : {
        "type" : "LineString",
        "coordinates" : [[4.8905266414,52.3725919469],[4.8905306647,52.3725356560],[4.8905360291,52.3724806443],[4.8905387113,52.3724028603],[4.8905440757,52.3723505607],[4.8905467579,52.3722754886],[4.8905574868,52.3721722195],[4.8905762622,52.3719066767],[4.8905963788,52.3716639050],[4.8905936966,52.3715244540],[4.8905749211,52.3714278871],[4.8905440757,52.3713393544],[4.8905065248,52.3712669418],[4.8904555628,52.3711703743],[4.8904166708,52.3711100387],[4.8903268168,52.3709759593],[4.8901725898,52.3707653720],[4.8900062928,52.3705816510],[4.8899472842,52.3705320104]]
      }
    }
  ]
}
```

**Error response example - JSON**

```json
{
  "detailedError ": {
    "code": "INVALID_REQUEST",
    "message": "Unknown field in fields=incidents.properties.last"
  }
}
```

### Log in

- **Source**: `https://developer.tomtom.com/traffic-api/documentation/tomtom-orbis-maps/traffic-incidents/incident-details-v2`

### Raster Incident Tiles

- **Source**: `https://developer.tomtom.com/traffic-api/documentation/tomtom-orbis-maps/traffic-incidents/raster-incident-tiles`

#### Tables

**Request parameters**

| Required parameters | Description |
| --- | --- |
| baseURL string | The base URL for calling TomTom services. Value: api.tomtom.com |
| zoom integer | The zoom level of the tile to be rendered. Value: 0..22 |
| x integer | The x coordinate of the tile on the zoom grid. Value: 0..2 zoom -1 |
| y integer | The y coordinate of the tile on the zoom grid. Value: 0..2 zoom -1 |
| key string | An API Key valid for the requested service. Value: Your valid API Key . |
| format string | The format of the response. Value: png |

**Request parameters**

| Optional parameters | Description |
| --- | --- |
| style string | The style to be used to render the tile. Values: light dark |
| t string | The Traffic Model ID is the reference value for the state of traffic at
a particular time. Use -1 to get the most recent
traffic information. Default value: -1 |
| tileSize integer | The tile size dimension in pixels. Values: 256 , and 512 Default value: 256 |
| apiVersion integer | Contains a version of the API to call.
Value: The current version is 1 . |

**Request headers**

| Required headers | Description |
| --- | --- |
| TomTom-Api-Version | Contains a version of the API to call. Value: An integer; the current version is 1 . |

**Request headers**

| Optional headers | Description |
| --- | --- |
| Tracking-ID | Specifies an identifier for the request. It can be used to trace a call. The value must match the regular expression '^[a-zA-Z0-9-]{1,100}$' . An example of the format
that matches this regular expression is a UUID (e.g., 9ac68072-c7a4-11e8-a8d5-f2801f1b9fd1 ). For details check RFC 4122 . If specified, it is replicated in the Tracking-ID response header. It is
only meant to be used for support and does not involve tracking of you
or your users in any form. Value: <string> |
| Accept | Advertises which content types, expressed as MIME types, the client is
able to understand. In this service, the header is used to specify a
preferred response format. Format: Accept: type/subtype Value: image/png Example: Accept: image/png |

**Response data**

| Field | Description |
| --- | --- |
| detailedError object | Main object of the error response. |
| code string | One of a server-defined set of error codes. |
| message string | A human-readable description of the error code. |

**Response data**

| Code | Meaning & possible causes |
| --- | --- |
| 200 | OK |
| 400 | Bad request , usually due to a malformed syntax. Zoom n is out of range [0,22]: The requested zoom level is
out of the possible range. x n is out of range [0,2 zoom -1]: The requested x coordinate is out of the possible range. y n is out of range [0,2 zoom -1]: The requested y coordinate is out of the possible range. Unknown Content Type: nnn : The requested content type is not supported. |
| 403 | Forbidden : The supplied API Key is not valid for this request. |
| 405 | Method Not Allowed : The provided HTTP request method is known by
the server, but is not supported by the target resource. |
| 429 | Too Many Requests : Too many requests were sent in a given amount
of time for the supplied API Key. |
| 500 | Internal Server Error |
| 503 | Service currently unavailable |
| 596 | Service Not Found : Unknown version of the service |

**Response data**

| Header | Description |
| --- | --- |
| Access-Control-Allow-Origin | Indicates that cross-origin resource sharing (CORS) is allowed. Value: * |
| Allow | Lists the set of supported HTTP methods. The header is sent in case a 405 HTTP response code is returned. Value: GET , HEAD |
| Cache-Control | Contains directives for a caching mechanism. Value: max-age=<number> |
| Content-Length | Contains information about the size of the response body. Value: <decimal number> |
| Content-Type | Indicates the media type of the resource returned. Values: image/png application/json; charset=utf-8 - in case of the 400 Bad Request text/xml; charset=utf-8 - in case of the 400 Bad Request In case of the 200 OK the response content should be
interpreted according to the type of the format request
parameter. |
| Date | Contains the date and time when the message was originated. Value: <http-date> |
| Tracking-ID | An identifier for the request. If the Tracking-ID header was specified in the request, it is replicated in the response.
Otherwise, it is generated automatically by the service. For details
check RFC 4122 . It is only meant
to be used for support and does not involve tracking of you or your
users in any form. Value: <string> |
| TrafficModelID | Contains the reference value for the state of traffic at a particular
time. If the request contains a valid Traffic Model ID and is not equal
to -1 , its value is replicated here. If the request does
not contain a Traffic Model ID or it is equal to -1 , the
most recent one is returned. Value: <integer> |

**Error response**

| Field | Description |
| --- | --- |
| detailedError object | Main object of the error response. |
| code string | One of a server-defined set of error codes. |
| message string | A human-readable description of the error code. |

#### Examples & payloads

**GET Request URL format**

```text
https://{baseURL}/maps/orbis/traffic/tile/incidents/{zoom}/{x}/{y}.{format}?apiVersion=1&key={Your_API_Key}&style={style}&t={t}
```

**GET Request URL example**

```text
https://api.tomtom.com/maps/orbis/traffic/tile/incidents/12/2044/1360.png?apiVersion=1&key={Your_API_Key}&style=light
```

**GET Request curl command**

```text
curl 'https://{baseURL}/maps/orbis/traffic/tile/incidents/{zoom}/{x}/{y}.{format}?apiVersion=1&key={Your_API_Key}&style={style}&t={t}'
```

**Error response example - XML**

```xml
<errorResponse errorCode="400" description="z out of range 0 <= z <= 22" version="traffic-rasterizer 2.0.009">
  <detailedError>
    <code>INVALID_REQUEST</code>
    <message>z out of range 0 <= z <= 22</message>
  </detailedError>
</errorResponse>
```

**Error response example - JSON**

```json
{
  "detailedError": {
    "code": "INVALID_REQUEST",
    "message": "z out of range 0 <= z <= 22"
  }
}
```

### Log in

- **Source**: `https://developer.tomtom.com/traffic-api/documentation/tomtom-orbis-maps/traffic-incidents/raster-incident-tiles-v2`

### Vector Incident Tiles

- **Source**: `https://developer.tomtom.com/traffic-api/documentation/tomtom-orbis-maps/traffic-incidents/vector-incident-tiles`

#### Tables

**Request parameters**

| Required parameters | Description |
| --- | --- |
| baseURL string | The base URL for calling TomTom services. Value: api.tomtom.com |
| zoom integer | The zoom level of the tile to be rendered. Value: 0...22 |
| x integer | The x coordinate of the tile on the zoom grid. Value: 0...2 zoom -1 |
| y integer | The y coordinate of the tile on the zoom grid. Value: 0...2 zoom -1 |
| format string | The format of the response. Value: pbf (Protocolbuffer Binary Format) |
| key string | An API Key valid for the requested service. Value: Your valid API Key . |

**Request parameters**

| Optional parameters | Description |
| --- | --- |
| t string | The Traffic Model ID is the reference
value for the state of traffic at a particular time. Use -1 to get the most recent traffic information. See the Response headers section
and Traffic Model ID page for
more information. Default value: -1 |
| tags array | The list of the values representing the available tags
in the tile. Default value: icon_category,left_hand_traffic,magnitude_of_delay,road_category,road_subcategory Allowed values: icon_category (enables icon_category_[idx] ) left_hand_traffic magnitude_of_delay road_category road_subcategory description (enables description_[idx] ) delay part_of_two_way_road start_time end_time id probability_of_occurrence number_of_reports last_report_time average_speed_kmph openlr time_validity display_class By default, only the default tags are attached to the tile geometry.
See Vector format for details. Each value in the list must be separated by a comma. The parameter behaves as a filter, narrowing down the
list of tags enclosed in each tile. The fewer tags chosen, the smaller the tile size because
of better geometry merging. Only tags that are used in both of the two protobuf layers
can be used as a parameter value. Value: Comma-separated list. |
| roadCategoryFilter string | This filter allows the choice of types of road categories to be
included in the response. The filter narrows down the road categories
available at particular zoom level. Multiple values are supported and
should be separated by a comma. Default value: all road categories Allowed values: motorway motorway_link trunk trunk_link primary primary_link secondary secondary_link tertiary tertiary_link street service track |
| categoryFilter string | This filter allows the choice of types of incidents and future
incidents to be included in the response. Filtering takes into
account the main icon category of the incident. Both value types
can be used: numeric and descriptive strings. Multiple values
are supported and should be separated by a comma. Default values: all incidents types Allowed values: 0 : Unknown 1 : Accident 2 : Fog 3 : DangerousConditions 4 : Rain 5 : Ice 6 : Jam 7 : LaneClosed 8 : RoadClosed 9 : RoadWorks 10 : Wind 11 : Flooding 14 : BrokenDownVehicle |
| timeValidityFilter string | This filter allows the choice of incidents based on their
occurrence in time. Multiple values are supported and
they should be separated by a comma. Default value: present Allowed values: present future |
| language string | The language code for the output language. It affects the
description fields in the response. When an incident
description does not have a translation, an English
description is returned. Default value: en-GB Allowed values: List of supported languages . |
| apiVersion integer | Contains a version of the API to call. Value: The current version is 1 . |

**Request headers**

| Required headers | Description |
| --- | --- |
| TomTom-Api-Version | Contains a version of the API to call. Value: The current version is 1 . |

**Request headers**

| Optional headers | Description |
| --- | --- |
| Accept-Encoding | Contains the content encoding (usually a compression
algorithm), that the client is able to understand. Value: gzip |
| If-None-Match | Contains an identifier for a specific version of resource.
The server will send back the requested resource, with
a 200 HTTP status code, only if it doesn't have an ETag
matching the given one. Value: <string> |
| Tracking-ID | Specifies an identifier for the request. It can be used to trace a call. The value must match the regular expression '^[a-zA-Z0-9-]{1,100}$' . An example of the format that matches this regular
expression is a UUID (e.g., 9ac68072-c7a4-11e8-a8d5-f2801f1b9fd1 ). For details check RFC 4122 . If specified, it is replicated in the Tracking-ID response header. It is only meant to be used for support and does
not involve tracking of you or your users in any form. Value: <string> |

**Response data**

| Field | Description |
| --- | --- |
| detailedError object | Main object of the error response. |
| code string | One of a server-defined set of error codes. |
| message string | A human-readable description of the error code. |

**Response data**

| Code | Meaning & possible causes |
| --- | --- |
| 200 | OK |
| 304 | Not modified |
| 400 | Bad request: The combination of parameters is not supported. zoom n is out of range [0,22]: the requested zoom level is
out of the possible range x n is out of range [0,2 zoom -1]: The requested x
coordinate is out of the possible range. y n is out of range [0,2 zoom -1]: The requested y
coordinate is out of the possible range. Invalid Traffic Model ID. |
| 403 | Forbidden: The supplied API Key is not valid for this request. |
| 405 | Method Not Allowed: The provided HTTP request method is known by
the server, but is not supported by the target resource. |
| 429 | Too Many Requests: Too many requests were sent in a given amount
of time for the supplied API Key. |
| 500 | Internal Server Error: There is a problem with the TomTom Maps
Vector Tile service. |
| 503 | Service currently unavailable: The service is currently
unavailable. |
| 596 | Service not found: Unknown version of the service. |

**Response data**

| Header | Description |
| --- | --- |
| Access-Control-Allow-Origin | Indicates that cross-origin resource sharing (CORS) is allowed. Value: * |
| Allow | Lists the set of supported HTTP methods. The header is
sent in case a 405 HTTP response code is returned. Value: GET , HEAD |
| Cache-Control | Contains directives for a caching mechanism. Value: max-age=<number> |
| Content-Encoding | Indicates which encodings were applied to the response body. Value: <gzip> |
| Content-Length | Contains information about the size of the response body. Value: <decimal number> |
| Content-Type | Indicates the media type of the resource returned. Value: <image/pbf> |
| Date | Contains the date and time when the message was originated. Value: <http-date> |
| ETag | Contains an identifier for a specific version of resource. Value: W/"2fdbd61f30456" |
| TrafficModelID | Contains the reference value for the state of traffic at
a particular time. If the request contains a valid Traffic Model ID and is not
equal to -1 , its value is replicated here. If the request does not contain a Traffic Model ID or it is
equal to -1 , the most recent one is returned. Value: <numeric> |
| Tracking-ID | An identifier for the request. If the Tracking-ID header was specified in the request, it is replicated in the response.
Otherwise, it is generated automatically by the service. For details
check RFC 4122 . It is only meant
to be used for support and does not involve tracking of you or your
users in any form. Value: <string> |

**Error response**

| Field | Description |
| --- | --- |
| detailedError object | Main object of the error response. |
| code string | One of a server-defined set of error codes. |
| message string | A human-readable description of the error code. |

#### Examples & payloads

**GET URL request format**

```text
https://{baseURL}/maps/orbis/traffic/tile/incidents/{zoom}/{x}/{y}.{format}?apiVersion=1&key={Your_API_Key}&t={t}
```

**GET URL request example**

```text
https://api.tomtom.com/maps/orbis/traffic/tile/incidents/5/4/8.pbf?apiVersion=1&key={Your_API_Key}
```

**GET curl command request example**

```text
curl 'https://api.tomtom.com/maps/orbis/traffic/tile/incidents/5/4/8.pbf?apiVersion=1&key={Your_API_Key}'
```

**Error response example - JSON**

```json
{
  "detailedError": {
    "code": "INVALID_REQUEST",
    "message": "Invalid zoom value. Allowed values are <0,22>."
  }
}
```

### Log in

- **Source**: `https://developer.tomtom.com/traffic-api/documentation/tomtom-orbis-maps/traffic-incidents/vector-incident-tiles-v2`

### Log in

- **Source**: `https://developer.tomtom.com/traffic-api/documentation/tomtom-orbis-maps/extended/traffic-incidents-extended-tiles`

### Raster Flow Tiles

- **Source**: `https://developer.tomtom.com/traffic-api/documentation/tomtom-orbis-maps/traffic-flow/raster-flow-tiles`

#### Tables

**Request parameters**

| Required parameters | Description |
| --- | --- |
| baseURL string | The base URL for calling TomTom services. Value: api.tomtom.com |
| zoom integer | Zoom level of the tile to be rendered. Value: 0..22 |
| x integer | x coordinate of the tile on the zoom grid. Value: 0..2 zoom -1 |
| y integer | y coordinate of tile on zoom grid. Value: 0..2 zoom -1 |
| format string | The format of the response. Value: png |
| apiKey string | API Key valid for requested service. Value: Your valid API Key . |

**Request parameters**

| Optional parameters | Description |
| --- | --- |
| style string | The style to be used to render the tile. Values: light dark |
| tileSize integer | The tile size dimension in pixels. Values: 256 512 Default value: 256 |
| apiVersion integer | Contains a version of the API to call. Value: The current version is 1 . |

**Request headers**

| Required headers | Description |
| --- | --- |
| TomTom-Api-Version | Contains a version of the API to call. Value: An integer; the current version is 1 . |

**Request headers**

| Optional headers | Description |
| --- | --- |
| Tracking-ID | Specifies an identifier for the request. It can be used to trace a call. The value must match the regular expression '^[a-zA-Z0-9-]{1,100}$' . An example of the format that matches this regular
expression is a UUID (e.g., 9ac68072-c7a4-11e8-a8d5-f2801f1b9fd1 ). For details check RFC 4122 . If specified, it is replicated in the Tracking-ID response header. It is only meant to be used for support and does
not involve tracking of you or your users in any form. Value: <string> |
| Accept | Advertises which content types, expressed as MIME types, the client is
able to understand. In this service, the header is used to specify a
preferred Bad Request response format. Format: Accept: type/subtype Accept: type/subtype, type/subtype - for multiple types Value: type/subtype is one of: image/png - in case of the 200 OK application/json - in case of the 400 Bad Request text/xml - in case of the 400 Bad Request Examples: Accept: application/json Accept: image/png, application/json |

**Response data**

| Field | Description |
| --- | --- |
| detailedError object | Main object of the error response. |
| code string | One of a server-defined set of error codes. |
| message string | A human-readable description of the error code. |

**Response data**

| Code | Meaning & possible causes |
| --- | --- |
| 200 | OK |
| 400 | Bad request Unknown style : The requested style is not available. zoom n is out of range [0,22] : The requested zoom level is out of the possible range. x n is out of range [0,2 zoom -1] : The requested x coordinate is out of the possible range. y n is out of range [0,2 zoom -1] : The requested y coordinate is out of the possible range. Unknown format: The requested format is not supported. |
| 403 | Forbidden : The supplied API Key is not valid for this request. |
| 405 | Method Not Allowed : The provided HTTP request method is known by
the server, but is not supported by the target resource. |
| 429 | Too Many Requests : Too many requests were sent in a given amount
of time for the supplied API Key. |
| 500 | Internal Server Error |
| 503 | Service currently unavailable |
| 596 | Service Not Found : Unknown version of the service. |

**Response data**

| Header | Description |
| --- | --- |
| Access-Control-Allow-Origin | Indicates that cross-origin resource sharing
(CORS) is allowed. Value: * |
| Allow | Lists the set of supported HTTP methods. The
header is sent in case a 405 HTTP response
code is returned. Values: GET , HEAD |
| Cache-Control | Contains directives for a caching mechanism. Value: max-age=<number> |
| Content-Length | Contains information about the size of the
response body. Value: <decimal number> |
| Content-Type | Indicates the media type of the resource returned. Values: image/png - in case of the 200 OK application/json; charset=utf-8 - in case of the 400 Bad Request |
| Date | Contains the date and time when the message was originated. Value: <http-date> |
| Tracking-ID | An identifier for the request. If the Tracking-ID header was specified in
the request, it is replicated in the response. Otherwise,
it is generated automatically by the service. For details check RFC 4122 .
It is only meant to be used for support and does not involve tracking
of you or your users in any form. Value: A <string> |

**Error response**

| Field | Description |
| --- | --- |
| detailedError object | Main object of the error response. |
| code string | One of a server-defined set of error codes. |
| message string | A human-readable description of the error code. |

#### Examples & payloads

**GET Request URL**

```text
https://{baseURL}/maps/orbis/traffic/tile/flow/{zoom}/{x}/{y}.{format}?apiVersion=1&key={Your_API_Key}&style={style}&tileSize={tileSize}
```

**GET Example**

```text
https://api.tomtom.com/maps/orbis/traffic/tile/flow/12/2044/1360.png?apiVersion=1&key={Your_API_Key}&style=light
```

**GET curl command**

```text
curl 'https://{baseURL}/maps/orbis/traffic/tile/flow/{zoom}/{x}/{y}.{format}?apiVersion=1&key={Your_API_Key}&style={style}&tileSize={tileSize}'
```

**Error response example - XML**

```xml
<errorResponse errorCode="400" description="z out of range 0 <= z <= 22" version="traffic-rasterizer 2.0.009">
  <detailedError>
    <code>INVALID_REQUEST</code>
    <message>z out of range 0 <= z <= 22</message>
  </detailedError>
</errorResponse>
```

**Error response example - JSON**

```json
{
  "detailedError": {
    "code": "INVALID_REQUEST",
    "message": "z out of range 0 <= z <= 22"
  }
}
```

### Log in

- **Source**: `https://developer.tomtom.com/traffic-api/documentation/tomtom-orbis-maps/traffic-flow/raster-flow-tiles-v2`

### Vector Flow Tiles

- **Source**: `https://developer.tomtom.com/traffic-api/documentation/tomtom-orbis-maps/traffic-flow/vector-flow-tiles`

#### Tables

**Request parameters**

| Required parameters | Description |
| --- | --- |
| baseURL string | The base URL for calling TomTom services. Value: api.tomtom.com |
| zoom integer | The zoom level of a tile to be rendered. Value: 0 ... 22 |
| x integer | The x coordinate of a tile on the zoom grid. Value: 0...2 zoom -1 |
| y integer | The y coordinate of a tile on the zoom grid. Value: 0...2 zoom -1 |
| format string | The format of the response. Value: pbf ( Protocolbuffer Binary Format ) |
| key string | An API Key valid for the requested service. Value: Your valid API Key . |

**Request parameters**

| Optional parameters | Description |
| --- | --- |
| roadCategoryFilter string | This filter allows the choice of types of road
categories to be included in the response. The filter
narrows down the road categories available at a
particular zoom level. Multiple values are supported
and should be separated by a comma. Default value: all road categories Allowed values: motorway motorway_link trunk trunk_link primary primary_link secondary secondary_link tertiary tertiary_link street service track |
| tags array | The list of the values representing the available tags in the tile. Default value: road_category,road_subcategory,left_hand_traffic,road_closure,relative_speed Allowed values: road_category road_subcategory left_hand_traffic road_closure relative_speed absolute_speed part_of_two_way_road openlr display_class By default, only the default tags are attached to the tile geometry. See Vector format for details. Each value in the list must be separated by a comma. The parameter behaves as a filter, narrowing down the list of tags enclosed in each tile. The fewer tags chosen, the smaller the tile size because of better geometry merging. Value: Comma-separated list. |
| apiVersion integer | Contains a version of the API to call. Value: The current version is 1 . |

**Request headers**

| Required headers | Description |
| --- | --- |
| TomTom-Api-Version | Contains a version of the API to call. Value: The current version is 1 . |

**Request headers**

| Optional headers | Description |
| --- | --- |
| Accept-Encoding | Contains the content encoding (usually a compression algorithm),
that the client is able to understand. Value: gzip |
| If-None-Match | Contains an identifier for a specific version of a resource. The server
will send back the requested resource with a 200 HTTP status code, only
if it doesn't have an ETag matching the given one. Value: string |
| Tracking-ID | Specifies an identifier for the request. It can be used to trace a call. The value must match the regular expression '^[a-zA-Z0-9-]{1,100}$' . An example of the format that matches this regular expression is a
UUID (e.g., 9ac68072-c7a4-11e8-a8d5-f2801f1b9fd1 ). For details check RFC 4122 . If specified, it is replicated in the Tracking-ID response header. It is only meant to be used for support and does not involve
tracking of you or your users in any form. Value: string |

**Response data**

| Field | Description |
| --- | --- |
| detailedError object | Main object of the error response. |
| code string | One of a server-defined set of error codes. |
| message string | A human-readable description of the error code. |

**Response data**

| Code | Meaning & possible causes |
| --- | --- |
| 200 | OK |
| 400 | Bad request: The combination of layer, type, and query parameters is not
supported. zoom n is out of range [0,22]: The requested zoom level is out of the possible range. x n is out of range [0,2 zoom -1]: The requested x coordinate is out of the possible range. y n is out of range [0,2 zoom -1]: The requested y coordinate is out of the possible range. |
| 403 | Forbidden: The supplied API Key is not valid for this request. |
| 405 | Method Not Allowed: The provided HTTP request method is known by
the server, but is not supported by the target resource. |
| 429 | Too Many Requests: Too many requests were sent in a given amount
of time for the supplied API Key. |
| 500 | Internal Server Error: There is a problem with the TomTom Traffic
Vector Flow Tiles API endpoint. |
| 503 | Service currently unavailable |
| 596 | Service Not Found: Unknown version of the service. |

**Response data**

| Header | Description |
| --- | --- |
| Access-Control-Allow-Origin | Indicates that cross-origin resource sharing (CORS) is allowed. Value: * universal. |
| Allow | Lists the set of supported HTTP methods. The header is sent in case a 405 HTTP response code is returned. Value: GET , HEAD |
| Cache-Control | Contains directives for a caching mechanism. Value: max-age=<number> |
| Content-Encoding | Indicates which encodings were applied to the response body. Value: gzip |
| Content-Length | Contains information about the size of the response body. Value: decimal number |
| Content-Type | Indicates the media type of the resource returned. Value: image/pbf |
| Date | Contains the date and time when the message was originated. Value: http-date |
| ETag | Contains an identifier for a specific version of resource. Value: W/"2fdbd61f30456" |
| Tracking-ID | An identifier for the request. If the Tracking-ID header was specified in the request, it is replicated in the response.
Otherwise, it is generated automatically by the service. For details
check RFC 4122 .I t is only meant to
be used for support and does not involve tracking of you or your users
in any form. Value: string |

**Error response**

| Field | Description |
| --- | --- |
| detailedError object | Main object of the error response. |
| code string | One of a server-defined set of error codes. |
| message string | A human-readable description of the error code. |

#### Examples & payloads

**GET URL request format**

```text
https://{baseURL}/maps/orbis/traffic/tile/flow/{zoom}/{x}/{y}.{format}?apiVersion=1&key={Your_API_Key}
```

**GET URL request example**

```text
https://api.tomtom.com/maps/orbis/traffic/tile/flow/5/4/8.pbf?apiVersion=1&key={Your_API_Key}
```

**GET curl command request example**

```text
curl 'https://api.tomtom.com/maps/orbis/traffic//tile/flow/5/4/8.pbf?apiVersion=1&key={Your_API_Key}'
```

**GET Request example**

```text
https://api.tomtom.com/maps/orbis/traffic/tile/flow/17/64989/42178.pbf?apiVersion=1&key={Your_API_Key}
```

**Response example**

```text
layer: 0
    name: Traffic flow
    version: 2
    extent: 4096
    feature: 0
      id: (none)
      geomtype: linestring
      geometry:
        LINESTRING[count=3](3002 -409,2964 1292,2842 2382)
        LINESTRING[count=3](2842 2382,2964 1292,3002 -409)
      properties:
        road_category="primary" [string]
        realtive_speed=0 [double]
        left_hand_traffic=1 [bool]
    feature: 1
      id: (none)
      geomtype: linestring
      geometry:
        LINESTRING[count=8](-409 656,-108 810,1260 1620,1832 1914,2842 2382,3792 2644,4400 2770,4505 2783)
      properties:
        road_category="primary" [string]
        relative_speed=0.7 [double]
        left_hand_traffic=1 [bool]
    feature: 2
      id: (none)
      geomtype: linestring
      geometry:
        LINESTRING[count=10](4505 2766,4418 2752,3882 2660,3406 2552,2920 2430,2700 2308,2276 2114,1952 1958,940 1430,-409 648)
      properties:
        road_category="secondary" [string]
        relative_speed=0.77 [double]
        left_hand_traffic=1 [bool]
    feature: 3
      id: (none)
      geomtype: linestring
      geometry:
        LINESTRING[count=7](2842 2382,2806 2752,2826 2932,3062 3494,3528 3882,4122 4366,4222 4505)
        LINESTRING[count=7](4222 4505,4122 4366,3528 3882,3062 3494,2826 2932,2806 2752,2842 2382)
      properties:
        road_category="primary" [string]
        relative_speed=1 [double]
        left_hand_traffic=1 [bool]
```

**Error response example - JSON**

```json
{
  "detailedError": {
    "code": "INVALID_REQUEST",
    "message": "Invalid zoom value. Allowed values are <0,22>."
  }
}
```

### Log in

- **Source**: `https://developer.tomtom.com/traffic-api/documentation/tomtom-orbis-maps/traffic-flow/vector-flow-tiles-v2`

### Log in

- **Source**: `https://developer.tomtom.com/traffic-api/documentation/tomtom-orbis-maps/extended/traffic-flow-extended-tiles`
