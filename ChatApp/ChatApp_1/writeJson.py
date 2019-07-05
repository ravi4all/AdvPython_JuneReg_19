import json

data = [{"Ram" :
             [{'msg':'hi'},
              {'rply':'hi'}]
         },
        {"Shyam" : [
            {'msg': 'hello'},
            {'rply': 'yes'}]
        }
        ]

file = open('data_2.json','w')
json.dump(data, file)
file.close()