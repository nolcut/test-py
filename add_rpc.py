def add(folder, num1, num2, output):
    num3 = num1 + num2
    with open("/tmp/output.txt", 'w') as f:
        f.write(str(num3))
    try:
        request_json = {
            "ProcedureID": "faasr_put_file",
            "Arguments": {"local_file": "/tmp/output.txt",
                          "remote_folder": folder,
                          "remote_file": output}
        }
        r = requests.post("http://127.0.0.1:8000/faasr-action", json=request_json)
    except Exception as e:
        print(f"Exception with faasr_put_file: {str(e)}")
    print(f"add: {num1} + {num2} = {num3}")

