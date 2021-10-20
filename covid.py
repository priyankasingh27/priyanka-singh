for i in range(0,100):
    print(" ")
    from covid import Covid 
    print("Covid tracker")
    cv=Covid()
    act=cv.get_total_active_cases()
    rec=cv.get_total_recovered()
    death=cv.get_total_deaths()
    con=cv.get_total_confirmed_cases()
    print("1.gobal count")
    print("2.active cases")
    print("3.confirmed cases")
    print("4.recovered cases")
    print("5.deceased")
    print("6.get covid updates by country name")
    choice=input("enter a number of your choice")
    if choice=='1':
        print("Active classes:",act,"\nConfirmed cases:",con,"\nRecovered cases:",rec,"\nDeceased:",death)
    elif choice=='2':
        print("Active classes:",act)
    elif choice=='3':
        print("Confirmed classe:",con)
    elif choice=='4':
        print("Recovered classes:",rec)
    elif choice=='5':
        print("Deceased :",death)
    elif choice=='6':
        str=i=input("enter country name:")
        cname=cv.get_status_by_country_name(i)
        print(cname)
    else:
        print("Invalid Option")
