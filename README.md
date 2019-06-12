# OMS api
- `loginApi.py` handles cassandra interface login api story
- `server.py` http server
- `test.py` test script for oms api
- `test.tavern.yaml` test file for api
# setup
- `pip install flask`
- `pip install tavern[pytest]`
- `pip install cassandra-driver`

# endpoints
## isUser
`/isUser`
Method: POST
```
{
"username":"user",
"password":"pass"
}
```
response
```
{
"valid": false,
"isAdmin": false
}
```
## test
`/test`
Method: GET
```
{   "status":"server is running"}
```

# running tests
`python test.py`