import re

#NEED PATH LOG AND PATH OF FILE FOR WRITTING
r_file = 'C:\\Users\dev\Desktop\dir1\\4zad\python\log.log'
w_file = 'C:\\Users\dev\Desktop\dir1\\4zad\p3\\python_top_urls.txt'

with open(r_file, 'r') as rf, open(w_file, 'w') as wf:
    text = rf.read()

    # LOOK FOR UNIC STATUS REQUESTS
    suc_req = re.findall(r' [\d]{3,3} ', text)  # mask for success requests
    unique_s = dict(zip(suc_req, [suc_req.count(i) for i in suc_req]))
    result_s = (unique_s[' 200 '])/((unique_s[' 200 '])+(unique_s[' 404 ']))

    # LOOK FOR UNIC SITES AND QUANTITIES
    urls = re.findall(r'http://[a-zA-Z.\d-]*', text)  # mask for sites
    unique = dict(zip(urls, [urls.count(i) for i in urls])) # select unic sites
    l1 = sorted(unique.items(), key=lambda x: x[1], reverse=True) #sorting big -> small

    # UNPACKING LIST, SELECT ITEMS FROM TUPLE
    for i in range(0, 9):
        g_tuple = l1[i]
        get_url = g_tuple[0]
        get_q = g_tuple[1]
        # CHECK INPUT SITE and QUANTITIES
        #print(get_url, get_q)
        wf.write(f"{get_url} - {get_q}\n")
    wf.write(f"\nУспешные запросы имеют статус 200.\nИмея количество повторений статусов, выразим отношение успешных ко всем запросам.\n{unique_s}\n")
    wf.write(f"Процент успешных запросов = {result_s}")

    # CHECK REQUESTS 200 FROM ALL REQUESTS
    #print(result_s)