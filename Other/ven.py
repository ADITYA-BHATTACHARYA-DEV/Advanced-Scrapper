# import json
#
# def export_to_csv():
#     with open("hello.json") as f:
#         listl=[]
#         data=json.loads(f.read())
#         temp=data[0]
#         header_items=[]
#         get_header_items(header_items, temp)
#         listl.append(header_items)
#
#         for obj in data:
#             d=[]
#             add_items_to_data(d,obj)
#             listl.append(d)
#         print(listl)
#
#
# def get_header_items(items, obj):
#     for x in obj:
#         if isinstance(obj[x],dict):
#             items.append(x)
#             get_header_items(items,obj[x])
#         else:
#             items.append(x)
#
# def add_items_to_data(items, obj):
#     for x in obj:
#         if isinstance(obj[x],dict):
#             items.append("")
#             get_header_items(items,obj[x])
#         else:
#             items.append(obj[x])
#
# export_to_csv()


import pandas as pd
obj=pd.read_json('../response.json', orient='index')
print(obj)
obj.to_csv('res_index.csv')

#
# import json
# import csv
#
# with open ("hello.json","r") as f:
#     data=json.load(f)
#     names=data["quiz"]
#
# with open ("hello.csv","w") as f:
#     fieldnames=names["sport"].keys()
#     writer=csv.DictWriter(f,fieldnames=fieldnames)
#     writer.writeheader()
#
#     for name in names:
#         writer.writerow(name)