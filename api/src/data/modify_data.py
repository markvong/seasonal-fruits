import json
from pprint import pprint

data_fn     = 'data.json'
modified_data_fn = 'modeled_data.json'

with open(data_fn, 'r') as infile:
    data = json.load(infile)

modified_data = []

for state in data:
    # modified_data[state] = {
    #     'state': state,
    #     'seasons': []
    # }
    modified_data[state] = {}
    modified_data[state]['state'] = state
    modified_data[state]['seasons'] = []

    print(state)
    month = 1
    for season in data[state]:
        print('current season is: {:d} {:s}'.format(month, season))
        month += 1
        season_data = {}
        season_data['season'] = season
        season_data['fruits'] = data[state][season]

        modified_data[state]['seasons'].append(season_data)
    
    # input('Waiting')
# pprint(modified_data)

with open(modified_data_fn, 'w') as outfile:
    json.dump(modified_data, outfile)