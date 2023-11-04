import subprocess

def extract_wifi_password():

    profiles_data = subprocess.check_output('netsh wlan show profiles').decode('utf-8').split('\n')
    profiles = [i.split(':')[1].strip() for i in profiles_data if 'All User Profile' in i]
    for profile in profiles:
        try:
            profile_info = subprocess.check_output(f'netsh wlan show profile {profile} key = clear').decode('utf-8').split('\n')
            password = [i.split(':')[1].strip() for i in profile_info if 'Key Content' in i]
        except:
            continue

        with open(file='wifi_passwords.txt', mode='a', encoding='utf-8') as file:
            file.write(f'Profile: {profile}\nPassword: {password}\n{"-"*20}\n')


def main():
    subprocess.check_output("chcp 65001", shell=True)
    extract_wifi_password()


if __name__=="__main__":
    main()