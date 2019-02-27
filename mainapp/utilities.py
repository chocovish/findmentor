import requests

def linkedin_api(code):
    url = "https://www.linkedin.com/oauth/v2/accessToken"
    id = "81w9qew3mn68ih"
    secret = "op5jx5uuYCNOHsns"
    redirect_uri = "http://localhost:8000/login/linkedin/callback"
    params = {'code':code,'client_secret':secret,'client_id':id,'redirect_uri':redirect_uri,'grant_type':'authorization_code'}
    res = requests.get(url,params=params).json()
    at = res['access_token']
    headers = {'Authorization': 'Bearer {}'.format(at)}
    res = requests.get("https://api.linkedin.com/v2/me?projection=(id,firstName,lastName)",headers=headers).json()
    print(res)
    first_name = res['firstName']['localized']['en_US']
    last_name = res['lastName']['localized']['en_US']
    linkedin_id = res['id']
    res2 = requests.get("https://api.linkedin.com/v2/emailAddress?q=members&projection=(elements*(handle~))",headers=headers).json()
    email = res2['elements'][0]['handle~']['emailAddress']
    print("Email Address: ",email)
    print("First_name: ",first_name)
    print("last_name: ",last_name)
    print("LinkedIn ID: ",linkedin_id)
    
    ret = {}
    ret['email'] = email
    ret['first_name'] = first_name
    ret['last_name'] = last_name
    ret['linkedin_id'] = linkedin_id
    return ret