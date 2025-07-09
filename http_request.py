def http_request():
    print("test action")
    test_json = {"ProcedureID": "test",
                 "Arguments": {"arg1": 1, "arg2": 2}}
    r = requests.post("http://127.0.0.1:8000/faasr-action", json=test_json)