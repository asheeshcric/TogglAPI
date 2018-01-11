from TogglAPI import TogglAPI

tog = TogglAPI(api_token="")                #Enter your API_Token here.

updates = tog.display_todays_updates()      #Returns a list of Today's working descriptions

tog.display_formatted_output(updates)       #To print the list in a structured format
