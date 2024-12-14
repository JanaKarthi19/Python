import requests
import hashlib


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/'+query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error Fetching: {res.status_code} check the API and try again')
    return res

def get_psswrd_leaks_count(hash, hash_to_check):
    hashes = (line.split(':') for line in hash.text.splitlines())
    for h, count in hashes:
        if h==hash_to_check:
            return count
    return 0

def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_char ,last_char = sha1password[:5] ,sha1password[5:]
    response = request_api_data(first_char)
    return get_psswrd_leaks_count(response, last_char)
    

if __name__ == "__main__":

    print('\nPassword Checker')

    password = input('\tEnter the Password : ')
    count = pwned_api_check(password)
    if count:
        print(f'\tyour password {password} has been found {count}....')
        print('\tChange Your Password Quickly for Safety Measures')
    else:
        print('\tYour Password has Secured')
        print('/n\tThank You')