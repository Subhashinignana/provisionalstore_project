your_order=input("choose your items(grocery,fresh vegetables):")
items=["grocery","fresh vegetables"]
if your_order in items:
    if your_order=="grocery":
        grocery_item=["milk","cheese","sugar","rice","dhal"]
        grocery_order=input("do you want order(yes or no):")
        if grocery_order=="yes":
            milk=30
            print("****milk->rs.30****")
            milk_count=int(input("how many litres:"))
            milk_price=milk*milk_count
            gst_price=(milk_price*8)/100
            total_price=milk_price+gst_price
            print(f"Total milk price is {total_price} (include gst)")
        if grocery_order=="yes": 
            cheese=65
            print("****cheese->rs.65****")
            cheese_count=int(input("how many grams:"))
            cheese_price=cheese*cheese_count
            gst_price=(cheese_price*12)/100
            total_price=cheese_price+gst_price
            print(f"Total cheese price is {total_price} (include gst)")
        if grocery_order=="yes":  
            sugar=125
            print("****sugar->rs.125****")
            sugar_count=int(input("how many kg:"))
            sugar_price=sugar*sugar_count
            gst_price=(sugar_price*20)/100
            total_price=sugar_price+gst_price
            print(f"Total sugar price is {total_price} (include gst)")
        if grocery_order=="yes": 
            rice=100
            print("****rice->rs.100****")
            rice_count=int(input("how many kg:"))
            rice_price=rice*rice_count
            gst_price=(rice_price*19)/100
            total_price=rice_price+gst_price
            print(f"Total rice price is {total_price} (include gst)")
        if grocery_order=="yes": 
            dhal=100
            print("****dhal->rs.130****")
            dhal_count=int(input("how many kg:"))
            dhal_price=dhal*dhal_count
            gst_price=(dhal_price*21)/100
            total_price=dhal_price+gst_price
            print(f"Total dhal price is {total_price} (include gst)")
        else:
            print("NOT AVAILABLE")
        print("****Sorry it is not available****")  
        total_bill=milk_price + cheese_price + sugar_price + rice_price + dhal_price  
        print(f"Your Total Bill is {total_bill} (include gst)")
    elif your_order=="fresh vegetables":
        freshvegetables_item=["tomato","peas","carrot","beetroot"]
        freshvegetables_order=input("do you want order(yes or no):")
        if freshvegetables_order=="yes":
            tomato=15
            print("****tomato->rs.15****")
            tomato_count=int(input("how many kg:"))
            tomato_price=tomato*tomato_count
            gst_price=(tomato_price*5)/100
            total_price=tomato_price+gst_price
            print(f"Total tomato price is {total_price} (include gst)")
        if freshvegetables_order=="yes":
            peas=20
            print("****peas->rs.20****")
            peas_count=int(input("how many kg:"))
            peas_price=peas*peas_count
            gst_price=(peas_price*10)/100
            total_price=peas_price+gst_price
            print(f"Total peas price is {total_price} (include gst)")
        if freshvegetables_order=="yes":
            carrot=30
            print("****carrot->rs.30****")
            carrot_count=int(input("how many kg:"))
            carrot_price=carrot*carrot_count
            gst_price=(carrot_price*12)/100
            total_price=carrot_price+gst_price
            print(f"Total carrot price is {total_price} (include gst)")
        if freshvegetables_order=="yes":
            beetroot=25
            print("****beetroot->rs.25****")
            beetroot_count=int(input("how many kg:"))
            beetroot_price=beetroot*beetroot_count
            gst_price=(beetroot_price*9)/100
            total_price=beetroot_price+gst_price
            print(f"Total beetroot price is {total_price} (include gst)")
        else:
            print("NOT AVAILABLE")
        print("****Sorry it is not available****")  
        total_bill=tomato_count + peas_price + carrot_price + beetroot_price 
        print(f"Your Total Bill is {total_bill} (include gst)")
    else:
        print("THANKS FOR PURCHASING")
else:
    print("THANKS FOR PURCHASING")


        
                
        
        
            
   
            
   
  
 
  
