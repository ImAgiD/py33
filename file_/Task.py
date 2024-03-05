# import csv
# import datetime
# import time
# filename = 'rows_300.csv'
# with open(filename, 'w', newline='') as file:
#     writer = csv.writer(file)
#     for i in range(1, 301):
#         now = datetime.datetime.now()
#         second = now.second
#         microsecond = now.microsecond
#         writer.writerow([i, second, microsecond])
#         time.sleep(0.01) #file

# import csv
# import time
# from datetime import datetime

# with open('rows_300.csv', 'w') as file_:
#     writer = csv.writer(file_)
    
#     for i in range(1, 301):
#         sec = time.strftime('%S', time.localtime())
#         mil_sec = time.strftime(datetime.now().microsecond.__str__())
#         writer.writerow([i, sec, mil_sec]) 
#         time.sleep(0.01)
        
