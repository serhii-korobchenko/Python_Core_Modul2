text1 = "https://us04web.zoom.us/j/79453881997?pwd=SzVXIblJc4_lIPCURw0c30Jve5QMtV.1"
text2 = "https://us04web.zoom.us/j/79453881997?pwd=SzVXIblJc4_lIPCURw0c30Jve5QMtV.1"

if len(text1) == len(text2):

    for i in range(len(text1)):
        
        a = True if text1 [i] == text2 [i] else False
        if a == False:
            print ("Sequense is not equal!") 
            print(f"There is problem in {i} symbol NOTE:==>{text1 [i]}, ==>{text2 [i]}") 
            break
    else:
        print ("There is complete accordance!")

else:
    print("Assigned texts have different lenght. It is not possible to compare!")
