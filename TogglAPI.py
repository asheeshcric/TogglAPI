import requests
import datetime


class TogglAPI():
    def __init__(self, api_token=""):
        self.api_token = api_token
        self.url = "https://www.toggl.com/api/v8/me?with_related_data=true"
        self.auth = (self.api_token, 'api_token')

    def display_todays_updates(self):
        try:
            response = requests.get(self.url, auth=self.auth)
            response_json = response.json()
            workspaces = response_json['data']['workspaces']
            for ws in workspaces:
                print(ws['name'])

            # For todays's date:
            now = str(datetime.datetime.now())
            now = now.split(" ")[0]

            time_entries = response_json['data']['time_entries']
            todays_updates = []
            for notes in time_entries:
                todays_date_notes = notes['start'].split('T')[0]
                if todays_date_notes == now and 'description' in notes.keys():
                    # print(notes)
                    todays_updates.append(notes['description'])

            return todays_updates

        except Exception as error:
            print(error)
            print("Try again!")

    def display_formatted_output(self, updates):
        try:
            count = 1
            for update in updates:
                print("{}. {}".format(count, update))
                count += 1
        except Exception as error:
            print(error)
            print("TRY AGAIN!")
