#coding=utf-8

from urllib import parse
import os,re


filepath = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath("__file__")))) + os.sep + "logs"
print(filepath)
files = os.walk(filepath)
for i in files:
    a = (i[2][0])
    files = filepath + os.sep + a
    print(files)
    with open(files,'r',encoding="utf-8") as f:
        b = f.read()


def url_decode(txt):
    return parse.unquote(txt)

c = url_decode(b)
print(c)
re.findall()
# android
re.findall("?<=info_customevent\":).*(?=\,\"info_page)")
# list_b = (re.findall("(?<=info_customevent\":).*(?=\,\"info_)",(f.read())))
# #bp_keys_list = ['exposureValue', 'expvalue', 'udid', 'eleid', 'pageid', 'clickno', 'modid', 'id', 'open', 'PositionSerNo']
# bp_keys_list = ['exposureValue','clickno']
# for i in (eval(list_b[0])):
#     # print(i["event_name"])
#     print(i["event_detail"])
#     for n in i["event_detail"].keys():
#         if n in bp_keys_list:
#             print(i["event_detail"][n])
#     print(i["event_detail"])
#     print(file,i)
#     for key in (i["event_detail"].keys()):
#         bp_keys_list.append(key)
#         bp_keys_tuple = set(bp_keys_list)
#         print(bp_keys_tuple)
#
#     if "clickno" in bp_keys_tuple:
#         print(i["event_detail"]["clickno"])
#     elif "exposureValue" in bp_keys_tuple:
#         print(i["event_detail"]["exposureValue"])
#     else:
#         pass
#
#     print(i)
#     print(i["event_detail"]["exposureValue"])
#     print(i["event_detail"]["clickno"])

# if __name__ == "__main__":
#     c = url_decode(b)
#     print(c)
# filepath = "e:" + os.sep + "android_logs_new"
# files = os.walk(filepath)
# for root,dirs,fileslist in files:
#     for file in fileslist:
#         with open(filepath + os.sep + file,'r',encoding='utf-8') as f:
#             try :
                # ios
                # list_a = (re.findall("(?<=info_customevent\":\[).*(?=\]\})", f.read()))
                # print(file,eval(list_a[0]))
                # print(type(list_a))
                # for i in list_a:
                #     print(i)

                # android
                # list_b = (re.findall("(?<=info_customevent\":).*(?=\,\"info_)",(f.read())))
                # #bp_keys_list = ['exposureValue', 'expvalue', 'udid', 'eleid', 'pageid', 'clickno', 'modid', 'id', 'open', 'PositionSerNo']
                # bp_keys_list = ['exposureValue','clickno']
                # for i in (eval(list_b[0])):
                #     # print(i["event_name"])
                #     print(i["event_detail"])
                #     for n in i["event_detail"].keys():
                #         if n in bp_keys_list:
                #             print(i["event_detail"][n])
                    # print(i["event_detail"])
                    # print(file,i)
                    # for key in (i["event_detail"].keys()):
                    #     bp_keys_list.append(key)
                    #     bp_keys_tuple = set(bp_keys_list)
                    #     print(bp_keys_tuple)

                    # if "clickno" in bp_keys_tuple:
                    #     print(i["event_detail"]["clickno"])
                    # elif "exposureValue" in bp_keys_tuple:
                    #     print(i["event_detail"]["exposureValue"])
                    # else:
                    #     pass

                    # print(i)
                    # print(i["event_detail"]["exposureValue"])
                    # print(i["event_detail"]["clickno"])
            # except Exception as e:
            #     print("this data is invalid data %s" %e)
            # finally:
            #     f.close()
    # print(i)


                # a = {
#     "bizdata": {
#         "info_customevent": [
#             {
#                 "ct": "20180730163525590",
#                 "viewtp": "native",
#                 "event_detail": {
#                     "expvalue": "appHome_recsntt_1-3_7974201600_none_0_19-56_0_A",
#                     "id": "12"
#                 },
#                 "event_name": "exposure"
#             },
#             {
#                 "ct": "20180730163525519",
#                 "viewtp": "native",
#                 "event_detail": {
#                     "expvalue": "appHome_recqpxh_1-2_0000000000_000000000139217976_01A_5-5_B99_A_f28d29cff76d5aa92505ffc09ed28029",
#                     "id": "12"
#                 },
#                 "event_name": "exposure"
#             },
#             {
#                 "ct": "20180730163525518",
#                 "viewtp": "native",
#                 "event_detail": {
#                     "expvalue": "appHome_recqpxh_1-1_0000000000_000000010550944120_01A_5-5_B99_A_f28d29cff76d5aa92505ffc09ed28029",
#                     "id": "12"
#                 },
#                 "event_name": "exposure"
#             }
#         ]
#     }
# }
# dict = (re.findall("(\[)(.*)(\])",repr(a)))
# print(dict)


b = {
    "EventPackge": [
        {
            "ref": "324324324324",
            "da": 14,
            "ts": 3123434,
            "access": "easfsfds",
            "event_type": "page"
        },
        {
            "ref": "32432432324324",
            "da": 1423,
            "ts": 312332434,
            "access": "eas32fsfds",
            "event_type": "p32age"
        }
    ]
}



# for root,dirs,files in os.walk(filepath):
#     for i in range(len(files)):
# f = open(filepath + os.sep + '165.txt','r',encoding='utf-8')
# print(eval(f.readlines()[3])[0])


