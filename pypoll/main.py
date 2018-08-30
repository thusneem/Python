import os
import csv


election_data=os.path.join("election_data.csv")
with open(election_data,'r') as csvfile:
    csvreader= csv.reader(csvfile,delimiter=',')
    csvheader=next(csvreader)

    total_votes=0
    khan_count =0 
    correy_count=0
    li_count =0
    otooley_count=0



    for row in csvreader:

        total_votes += 1

        if (str(row[2]) == "Khan"):
            khan_count += 1
        elif (str(row[2])  == "Correy"):
            correy_count += 1
        elif (str(row[2]) == "Li"):
            li_count += 1  
        else:
            otooley_count += 1 

     


khan_percent= round(((khan_count/total_votes) * 100),3)
correy_percent= round(((correy_count/total_votes) * 100),3) 
li_percent= round(((li_count/total_votes) * 100),3) 
otooley_percent= round(((otooley_count/total_votes) * 100),3) 

   
print(f"Total Votes: {str(total_votes)}")
print(f"Khan : {str(khan_percent)}%,{str(khan_count)}")
print(f"Correy : {str(correy_percent)}%,{str(correy_count)}")
print(f"Li : {str(li_percent)}%,{str(li_count)}")
print(f"O'Tooley : {str(otooley_percent)}%,{str(otooley_count)}")

can_score_dict = {}
can_score_dict.setdefault('khan',khan_count)
can_score_dict.setdefault('correy',correy_count)
can_score_dict.setdefault('li',li_count)
can_score_dict.setdefault('otooley',otooley_count)
# finding winner using dictionary
#print('Winner :', max(zip(can_score_dict.values(),can_score_dict.keys())))

# finding winner using if statements 
if khan_count > correy_count and khan_count > li_count and khan_count > otooley_count:

    print("Winner : Khan")
    
elif correy_count > khan_count and correy_count > li_count and correy_count > otooley_count:

    print("winner : Correy")

elif li_count > correy_count and li_count > khan_count and li_count > otooley_count:

    print("winner : Li")
else :

    print("winner : Otooley")   



 # Set variable for output file
output_file = os.path.join("pypoll_final.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    
    
    # Write the output to datafile
    print("Total Votes", total_votes,file=datafile)
    print("Khan ", khan_percent,"%", khan_count,file=datafile)
    print("Correy", correy_percent,"%", correy_count,file=datafile)
    print("Li ", li_percent,"%", li_count,file=datafile)
    print("O \'Tooley", otooley_percent,"%", otooley_count,file=datafile)
    print("Winner", max(zip(can_score_dict.values(),can_score_dict.keys())),file=datafile)


