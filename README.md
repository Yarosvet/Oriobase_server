# Oriobase server
Storing data in form of related objects (graphs)

# Run server
```bash
pip3 install -r requirements.txt
python3 main.py
```
# Data representations
There are two types of data: object and object-group. Object-group can contain unlimited count of objects.
Objects (or groups) can be related and got by relations.

# Api
This server application can be controlled only by using API.
For example:

Request URL ```http://127.0.0.1:8080/api/v1/get_object?id=1```

Responce:
```json
{"fields":[],
"id":3,
"name":"c",
"relations":[
  {"name":"to a",
  "target_id":1,
  "type":"Object"},
  
  {"name":"to b",
  "target_id":2,
  "type":"Object"}
]}
```
See *api/api_v1/api.py* and flask rules in *main.py* to understand how does API work.
