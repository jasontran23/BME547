import requests

server = "http://vcm-7631.vm.duke.edu:5002"
r = requests.get(server + "/get_patients/jnt12")
print(r.text)
r = requests.get(server + "/get_blood_type/M1")
print(r.text)
r = requests.get(server + "/get_blood_type/F1")
print(r.text)
out_data = {"Name": "jnt12", "Match": "No"}
r = requests.post(server + "/match_check", json=out_data)
print(r.text)