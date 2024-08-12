
import sys
import requests
token = 'INSERT_TOKEN_HERE'
headers = {"X-Instance-Name": "mobilesec2", "X-API-KEY": token}
host = 'https://online.miradore.com'
def addDevice():
        id = 6
        data={
                "id": id,
                "category": "iPhone",
                "manufacturer": sys.argv[2],
                "model": sys.argv[3],
                "identifier": "new" + sys.argv[2] + "dev" + str(id),
                "friendlyName": "appledevice4",
                "ownership": "Purchased",
                "ownershipStartDate": "2024-07-30T02:06:18.965Z",
                "ownershipEndDate": "2024-07-30T02:06:18.965Z",
                "userEmailAddress": "sk47799@nyu.edu",
                "organization": ["NYU"],
                "location": ["NY"],
                "tags": ["new"],
                "customAttributes": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string"}
                }
        get_user_url = f"{host}/api/v2/Device"
        resp = requests.post(get_user_url, headers=headers, json=data)
        return resp
def getLocation():
        id= input("Please enter the ID of the user to obtain Location:\n")
        url=f"{host}/api/v2/Device/{id}/Location"
        resp=requests.get(url, headers=headers)
        return resp.text
def getUserByEmail():
        email = input("Please enter the email of the user you're searching for:\n")
        url=f"{host}/api/v2/User?email={email}"
        resp=requests.get(url, headers=headers)
        return resp.text
def getUser():
        userId=input("Which user ID would you like to review?:\n")
        get_user_url = f"{host}/api/v2/User/{userId}"
        resp = requests.get(get_user_url, headers=headers)
        return resp.text
def lockDevice():
        userId = input("Please enter the ID of the device you'd like to lock:\n")
        get_user_url = f"{host}/api/v2/Device/{userId}/Lock"
        resp = requests.post(get_user_url, headers=headers)
        return resp.text
def lostMode():
        body={
                "message": "locking device",
                "phoneNumber": "9152532328",
                "footnote": "test",
                "enableLocationTracking": True
                }
        userId= input("Please enter the ID of the device you'd like to place in Lost Mode: \n")
        url=f"{host}/api/v2/Device/{userId}/LostMode"
        resp=requests.post(url, headers=headers, json=body)
        return resp.text
def lostModeOff():
        id=input("Please enter the id of the device to turn off Lost Mode:\n")
        url=f"{host}/api/v2/Device/{id}/LostMode"
        resp = requests.delete(url, headers=headers)
        return resp.text
def deployApp(appName):
        name_to_id = {'yahoo': 0, 'teams': 1}
        id=input("Please enter the id of the device to deploy the app to:\n")
        deploy_device_url = f"{host}/api/v2/Device/{id}/Application"
        deploy_device_body = {
                "appDeploymentMethodId": 2, # App store
                "managedConfigurationId": name_to_id[appName]
        }
        resp = requests.post(deploy_device_url, headers=headers, json=deploy_device_body)
        print(resp.text)

choice = sys.argv[1]
if choice == "add":
        print(addDevice())
elif choice == "location":
        print(getLocation())
elif choice == "email":
        print(getUserByEmail())
elif choice == "user":
        print(getUser())
elif choice == "lock":
        print(lockDevice())
elif choice == "lost":
        print(lostMode())
elif choice == "lostOff":
        print(lostModeOff())
elif choice == "app":
        print(deployApp(sys.argv[2]))
else:
        print("Incorrect choice!")
