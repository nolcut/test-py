def add(folder, num1, num2, output):
    import FaaSr_py
    num3 = num1 + num2
    with open("output.txt", 'w') as f:
        f.write(str(num3))
    try:
        FaaSr_py.faasr_put_file(local_file="output.txt", remote_folder=folder, remote_file=output)   
    except Exception as e:
        print(f"Exception with faasr_put_file: {str(e)}")
    print(f"add: {num1} + {num2} = {num3}")


