import requests
class IRCTC:
    def __init__(self):

        UI=input(print("""HOW WOULD you LIKE TO PROCEES
        1. ENTER 1 TO CHECK LIVE TRAIN STATUS:-
        2. ENTER 2 TO CHECK PNR STATUS:-
        3. ENTER 3 TO CHECK TRAIN SCHEDULE:-
        4. ENTER 4 TO FIND STATION CODE:- """))
        if UI == "1":
            print("Live Train status")
        elif UI == "2":
            print("PNR Status")
        elif UI == "3":
            self.train_schedule()
        else:
            self.Station_Code()
    def Station_Code(self):
        S_Name=input("Enter the station name:-")
        self.fetch_SDATA(S_Name)
    def fetch_SDATA(self,StationName):
        Data = requests.get("https://indianrailapi.com/api/v2/StationNameToCode/apikey/87cfdab75085c4fe94a75a9ba9bec02b/StationName/{}".format(StationName))
        Data = Data.json()
        i=Data["Station"]
        print("Station code is:--",i["StationCode"])





    def train_schedule(self):
            T_NO=int(input("Enter the Train Number:--"))
            self.fetch_data(T_NO)

    def fetch_data(self,train_number):
            Data = requests.get("https://indianrailapi.com/api/v2/TrainSchedule/apikey/87cfdab75085c4fe94a75a9ba9bec02b/TrainNumber/{}".format(train_number))
            Data = Data.json()
            for i in Data["Route"]:
                print("Station:-",i["StationName"],"|","ArrivalTime:-",i["ArrivalTime"],"|","DepartureTime:-",i["DepartureTime"],"|","Distance:-",i["Distance"],"kms")

Object = IRCTC()

