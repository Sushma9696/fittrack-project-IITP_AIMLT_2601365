prev_cnt=0
total_bookings=0
rej=0
while True:
  age=[]
  total_seats=350
  count=0
  number_of_tickets=int(input("Enter number of tickets:"))
  
  if number_of_tickets==0:
    rem_seats=total_seats-prev_cnt
    print(f"Final Report: Total Bookings: {total_bookings},Total Tickets Sold: {prev_cnt},Rejected Bookings: {rej},Remaining Seats: {rem_seats}")
    break
  
  elif number_of_tickets<=15:
    for i in range(number_of_tickets):
      abc=int(input("Enter age:"))
      age.append(abc)
    #print(age)

    for i in age:
      if i <12:
        count+=1
      
    #print(count)  
    

    if count>0:
      print("BOOKING REJECTED - Age restriction") 
      rej+=1

    else:
      cnt=len(age)
      prev_cnt+=cnt
      total_bookings+=1
      #print(cnt)  
      #print(f"prev_cnt - {prev_cnt}") 
      #print(f"total_bookings - {total_bookings}") 
      print(f"BOOKING CONFIRMED - {cnt} tickets")   


  else:
      continue
