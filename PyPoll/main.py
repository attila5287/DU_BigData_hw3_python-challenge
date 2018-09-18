#dependencies
import os
import csv
#creating a variable to store path
path='Resources\election_data.csv'
#creates a variable to store accumulator for counting popular votes
vote_counter=0
#creates a dictionary with candidates as keys and popular vote count stored as values
poll = {}
# opening csv in read mode for data analysis
with open(path, 'r') as file:
#code uses reader function of imported csv library
    reader=csv.reader(file)
#skips the header line
    next(reader)
# loop will fo through each line and performs below
    for row in reader:
        vote_counter+=1
#condition will check each vote to match with keys/candidate names
        if row[2] in poll.keys():
# operation that will increase values/vote count
            poll[row[2]] = poll[row[2]]+1
#below will run only for the first vote for each candidate
        else:
            poll[row[2]] = 1
# print(poll.keys())
# cand_names = []
cand_names = list(poll.keys())
# print(cand_names)
# creating a list to store final vote count for print/output
cand_votes = []
cand_votes = list(poll.values())
# print(cand_votes)
# creates a list to store final vote percentage
cand_perc_list=[]
print("-----ELECTION RESULTS-----")
print("Total votes:"' {:,.0f}'.format(vote_counter))
print("--------------------------")
#each loop will candidate name, percentage and vote count
for n in range(0,len(cand_names)):
    cand_perc = cand_votes[n] / vote_counter
    cand_perc_list.append(cand_perc)
    # will print in acct format separated by tabs for easy read
    print(cand_names[n],": \t",'{:,.0%}'.format(cand_perc),"\t(",'{:,.0f}'.format(cand_votes[n]),")")
print("--------------------------")
# method .get will return key(candidate) for maximum value(votes)
winner_key=max(poll, key=poll.get)
print('Winner is...\n          .....'+winner_key)
#below addresses imported operating system library
# and creates a text document .txt for output
PyPoll_output=os.path.join('PyPoll_output.txt')
#now the file is created, below block opens the document
# if already created then overwrites the content inside
with open(PyPoll_output,'w') as txt_only:
    txt_only.writelines('-----ELECTION RESULTS-----\n')
    txt_only.writelines("Total votes:"' {:,.0f}'.format(vote_counter))
    txt_only.writelines("\n")
    txt_only.writelines("--------------------------\n")
    for n in range(0, len(cand_names)):
        cand_perc = cand_votes[n] / vote_counter
        cand_perc_list.append(cand_perc)
        txt_only.writelines(cand_names[n])
        txt_only.writelines(": ")
        txt_only.writelines(": \t")
        txt_only.writelines('{:,.0%}'.format(cand_perc))
        txt_only.writelines("\t(")
        txt_only.writelines('{:,.0f}'.format(cand_votes[n]))
        txt_only.writelines(")")
        txt_only.writelines("\n")
    #...
    txt_only.writelines('Winner is...\n')
    txt_only.writelines('            ..... ')
    txt_only.writelines(winner_key)