# OMS api
- `loginApi.py` handles cassandra interface login api story
- `server.py` http server
- `test.py` test script for oms api
- `test.tavern.yaml` test file for api
# setup
- `pip install flask`
- `pip install tavern[pytest]`
- `pip install cassandra-driver`
# running tests
`py.test test.tavern.yaml  -v`