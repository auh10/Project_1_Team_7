#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress


# In[2]:


#load csv
final = ("../Project_1_Team_7/final_df.csv")
salaries_data = ("../Project_1_Team_7/Players_Salaries.xlsx")

final_df = pd.read_csv(final)
salaries_stats_df = pd.read_excel(salaries_data)
salary_2015_df = pd.read_excel(salaries_data, sheet_name='2015')
salary_2016_df = pd.read_excel(salaries_data, sheet_name='2016')
salary_2017_df = pd.read_excel(salaries_data, sheet_name='2017')
salary_2018_df = pd.read_excel(salaries_data, sheet_name='2018')
salary_2019_df = pd.read_excel(salaries_data, sheet_name='2019')


# In[3]:


final_df.columns


# In[4]:


salaries_stats_df.columns


# In[5]:


#create dataframe for 2015 Clippers salaries
clipper_salary_2015_df = salary_2015_df.loc[salary_2015_df['TEAM'] == "LA Clippers"]
clipper_salary_2015_df.head(5)


# In[6]:


#create dataframe and show 2016 Clippers Salaries
clipper_salary_2016_df = salary_2016_df.loc[salary_2016_df['TEAM'] == "LA Clippers"]
clipper_salary_2016_df.head(5)


# In[7]:


#create dataframe and show 2017 Clippers Salaries
clipper_salary_2017_df = salary_2017_df.loc[salary_2017_df['TEAM'] == "LA Clippers"]
clipper_salary_2017_df.head(5)


# In[8]:


#create dataframe and show 2018 Clippers Salaries
clipper_salary_2018_df = salary_2018_df.loc[salary_2018_df['TEAM'] == "LA Clippers"]
clipper_salary_2018_df.head(5)


# In[9]:


#create dataframe and show 2019 Clippers Salaries
clipper_salary_2019_df = salary_2019_df.loc[salary_2019_df['TEAM'] == "LA Clippers"]
clipper_salary_2019_df.head(5)


# In[10]:


#set variables for positions listed on dataset: 
#(G)Guard,(PG)Point Guard,(SG)Shooting Guard,(PF)Power Forward,(SF)Small Forward,(C)Center
point_guard_stats_df = final_df.loc[final_df['POSITION'] == ' PG' ]
guard_stats_df = final_df.loc[final_df['POSITION'] == ' G' ]
shooting_guard_stats_df = final_df.loc[final_df['POSITION'] == ' SG' ]
power_forward_stats_df = final_df.loc[final_df['POSITION'] == ' PF' ]
small_forward_stats_df = final_df.loc[final_df['POSITION'] == ' SF' ]
center_stats_df = final_df.loc[final_df['POSITION'] == ' C' ]


# In[11]:


#create dataframe for Point Guard
point_guard_stats_df = final_df.loc[final_df['POSITION'] == ' PG' ]
point_guard_stats_df


# In[12]:


final_df[["REB","PLAYER"]]


# In[13]:


#set PLAYER  index
players_index_df = final_df.set_index("PLAYER")
players_index_df


# In[14]:


#highest paid 
highest_paid = final_df.loc[final_df["SALARY"] > 30000000, ["PLAYER","YEAR", "TEAM","POSITION", "PTS","GP","SALARY","REB","AST","TOV","STL","BLK","MIN"]]
highest_paid


# In[140]:


#highest paid overal nba players
#set with of bar
barWidth = 0.15

#set height of bars
PTS_means = [26.4, 27.3, 20.3, 27.4, 25.5, 22.6, 23.5, 25.8]
GP_means = [51, 69, 4, 55, 38, 33, 26, 30]
MIN_means = [32, 33.8, 28, 35.2, 34.9, 34.5, 30.7, 32.2]
REB_means = [5.1, 5.3, 5.1, 8.5, 7.8, 7.9, 6.0, 7.5]
SALARY = [37, 37, 40, 35, 37, 32, 30, 32]


# the label locations
r1 = np.arange(len(PTS_means))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]
r5 = [x + barWidth for x in r4]
# Add xticks on the middle of the group bars

plt.xlabel('group', fontweight='bold')
plt.ylabel('group', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(PTS_means))], ['Stephen Curry 2017', 'Stephen Curry 2018', 'Stephen Curry 2019', 'Lebron James 2018', 'Lebron James 2019', 'Blake Griffin 2017', 'Paul George 2019', 'Kawhi Leonard 2019'],rotation=90)
plt.title('Overall Highest Paid NBA Players')

#create group based on highest paid players
plt.xlabel("Players")
plt.ylabel("(Salary in Millions)")
 
#make plot
#highest_paid.plot(r1,highest_paid["SALARY"],kind="bar",figsize=(20,3))

#Plot bar and colors and labels
plt.bar(r1, REB_means, color='blue', width=barWidth, label='Rebounds per Game')
plt.bar(r2, PTS_means, color='orange', width=barWidth, label='Points per Game')
plt.bar(r3, GP_means, color='green', width=barWidth, label='Games per Year')
plt.bar(r4, MIN_means, color='yellowgreen', width=barWidth, label='Minutes per Game')
plt.bar(r5, SALARY, color='red', width=barWidth, label='SALARY in Millions')

plt.legend(bbox_to_anchor=(1, 1, 0.6, 0), loc=2, ncol=1, mode="normal", borderaxespad=1)
plt.show()


# In[21]:


highest_paid = final_df.loc[final_df["SALARY"] > 20000000, ["PLAYER","YEAR", "TEAM","POSITION", "PTS","GP","SALARY","REB","AST","TOV","STL","BLK","MIN"]]
highest_paid


# In[145]:


#set with of bar
barWidth = 0.15
# Add xticks on the middle of the group bars
plt.title('Highest Paid Clippers Players')
plt.xlabel('group', fontweight='bold')
plt.ylabel('group', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(PTS_means))], ['Chris Paul (PG) 2015', "DeAndre Jordan (C) 2016", "Chris Paul (PG) 2016", 'Blake Griffin (PF) 2016', 'Blake Griffin (PF) 2017', 'Danilo Gallinari (PF) 2017', 'DeAndre Jordan (C) 2017', 'Danilo Gallinari (PF) 2018', 'Paul George (SF) 2019', 'Kawhi Leonard (SF) 2019'],rotation=90)


#set height of bars
REB_means = [4.2, 13.8, 5.0, 8.1, 7.9, 4.8, 15.2, 6.1, 6.0, 7.5]
PTS_means = [19.5, 12.7, 18.1, 21.6, 22.6, 15.3, 12.0, 19.8, 23.5, 25.8]
GP_means = [74, 81, 61, 61, 33, 21, 77, 68, 26, 30]
MIN_means = [32.7, 31.7, 31.5, 34.0, 34.5, 32.0, 31.5, 30.3, 30.7, 32.2]
SALARY = [21.4, 21.1, 22.8, 20.1, 32.1, 20.5, 22.6, 21.5, 21.5, 32.7]

# the label locations
r1 = np.arange(len(PTS_means))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]
r5 = [x + barWidth for x in r4]

#create group based on highest paid players
plt.xlabel("Players")
plt.ylabel("(Salary in Millions)")
 
#make plot
#highest_paid.plot(r1,highest_paid["SALARY"],kind="bar",figsize=(20,3))

#Plot bar and colors and labels
plt.bar(r1, REB_means, color='blue', width=barWidth, label='Rebounds per Game')
plt.bar(r2, PTS_means, color='orange', width=barWidth, label='Points per Game')
plt.bar(r3, GP_means, color='green', width=barWidth, label='Games per Year')
plt.bar(r4, MIN_means, color='yellowgreen', width=barWidth, label='Minutes per Game')
plt.bar(r5, SALARY, color='red', width=barWidth, label='SALARY in Millions')

plt.legend(bbox_to_anchor=(1, 1, 0.6, 0), loc=2, ncol=1, mode="normal", borderaxespad=1)
plt.show()


# In[ ]:


curry_pts = players_index_df.loc[["Stephen Curry","YEAR"]]
print(curry_pts)


# In[ ]:





# In[ ]:


#get avg of Stephen Curry points
curry_pts.mean()


# In[ ]:


curry_salary = players_index_df.loc["Stephen Curry","SALARY"]
print(curry_salary)


# In[ ]:


#avg of salary s.curry
curry_salary.mean()


# In[ ]:





# In[33]:


lowest_paid = final_df.loc[final_df["SALARY"] < 600000, ["PLAYER","TEAM","POSITION", "PTS","SALARY","REB","MIN", "GP"]]
lowest_paid


# In[ ]:


blake_pts = players_index_df.loc[["Blake Griffin","REB"]]
print(blake_pts)


# In[ ]:





# In[ ]:


#set index to 'Team'
team_df = point_guard_stats_df.set_index("TEAM")
team_df


# In[ ]:


#grab only LA Clippers data with .loc
clippers_df = final_df.loc[final_df["TEAM"] == "LA Clippers"]
clippers_df


# In[ ]:


#grab only LA Clippers data with .loc
clippers_df = final_df.loc[final_df["PLAYER"] == 'Blake Griffin']
clippers_df


# In[ ]:


#stats for Guard position Clippers
# guard_stats_df = players_index_df.loc[players_index_df['POSITION'] == ' G']
# guard_stats_df


# In[174]:


guard_stats_df = players_index_df.loc[players_index_df['POSITION'] == ' G', ["TEAM","POSITION", "PTS","SALARY","REB","MIN", "GP"]]
guard_stats_df.head(10)


# In[147]:


#plot graph for salary correlation to position 'Guard' non clippers
#guard_stats_df


#set with of bar
barWidth = 0.15
# Add xticks on the middle of the group bars
plt.title('Stats for Guards in NBA')
plt.xlabel('group', fontweight='bold')
plt.ylabel('group', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(PTS_means))], ['Shaun Livingston (G) 2015', "Leandro Barbosa (G) 2015", "Ian Clark (G) 2015", 'Briante Weber (G) 2016', 'Ian Clark (G) 2016', 'Shaun Livingston (G) 2016', 'Shaun Livingston (G) 2017', 'Nick Young (G) 2017', 'Shaun Livingston (G) 2018', 'Nick Young (G) 2015'],rotation=90)

#set height of bars
REB_means = [2.2, 1.7, 1.0, 0.6, 1.6, 2.0, 1.8, 1.6, 1.8, 1.8]
PTS_means = [6.3, 6.4, 3.6, 1.7, 6.8, 5.1, 5.5, 7.3, 4.0, 7.3]
GP_means = [78, 68, 66, 7, 77, 76, 71, 80, 64, 54]
MIN_means = [19.5, 15.9, 8.8, 6.6, 14.8, 17.7, 15.9, 17.4, 15.1, 19.1]
SALARY = [5.0, 2.5, 0.9, 0.1, 0.9, 5.7, 7.6, 5.1, 8.3, 5.2]

# the label locations
r1 = np.arange(len(PTS_means))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]
r5 = [x + barWidth for x in r4]

#create group based on highest paid players
plt.xlabel("Guard Players")
plt.ylabel("(Millions for Salary)")
 
#make plot
#highest_paid.plot(r1,highest_paid["SALARY"],kind="bar",figsize=(20,3))

#Plot bar and colors and labels
plt.bar(r1, REB_means, color='blue', width=barWidth, label='Rebounds per Game')
plt.bar(r2, PTS_means, color='orange', width=barWidth, label='Points per Game')
plt.bar(r3, GP_means, color='green', width=barWidth, label='Games per Year')
plt.bar(r4, MIN_means, color='yellowgreen', width=barWidth, label='Minutes per Game')
plt.bar(r5, SALARY, color='red', width=barWidth, label='SALARY in Millions')

plt.legend(bbox_to_anchor=(1, 1, 0.6, 0), loc=2, ncol=1, mode="normal", borderaxespad=1)
plt.show()


# In[175]:


guard_stats_df = players_index_df.loc[players_index_df['POSITION'] == ' G',["YEAR","TEAM","POSITION","PTS","SALARY","REB","MIN", "GP"]]
guard_stats_df


# In[182]:


clippers_guard_stats_df = players_index_df.loc[players_index_df['POSITION'] == ' G', ["TEAM", "YEAR", "POSITION", "PTS","SALARY","REB","MIN", "GP"]]
clippers_guard_stats_df


# In[183]:


#plot graph for salary correlation to position 'Guards' CLIPPERS
#clippers Guards


#set with of bar
barWidth = 0.15
# Add xticks on the middle of the group bars
plt.title('Clippers Guards Stats')
plt.xlabel('group', fontweight='bold')
plt.ylabel('group', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(PTS_means))], ['Jamal Crawford (G) 2015', 'Raymond Felton (G) 2016', 'Jamal Crawford (G) 2016', 'C.J. Williams (G) 2017', 'Jawun Evans (G) 2017', 'Milos Teodosic (G) 2017', 'Sindarius Thornwell (G) 2017', 'Milos Teodosic (G) 2018', 'Sindarius Thornwell (G) 2018', 'Tyrone Wallace (G) 2018'],rotation=90)
#set height of bars
REB_means = [1.8, 2.7, 1.6, 1.5, 1.8, 2.8, 1.9, 1.1, 0.7, 1.6]
PTS_means = [14.2, 6.7, 12.3, 5.5, 4.8, 9.5, 3.9, 3.2, 1.0, 3.5]
GP_means = [79, 80, 82, 38, 48, 45, 73, 15, 64, 62]
MIN_means = [26.9, 21.2, 26.3, 18.6, 16.2, 25.2, 15.8, 10, 4.9, 10.1]
SALARY = [5.6, 0.9, 13.2, 0.3, 0.8, 6, 0.8, 6.3, 1.37, 1.34]

# the label locations
r1 = np.arange(len(PTS_means))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]
r5 = [x + barWidth for x in r4]

#create group based on highest paid players
plt.xlabel("Clippers Guard Stats")
plt.ylabel("(Salary in Millions)")
 
#make plot
#highest_paid.plot(r1,highest_paid["SALARY"],kind="bar",figsize=(20,3))

#Plot bar and colors and labels
plt.bar(r1, REB_means, color='blue', width=barWidth, label='Rebounds per Game')
plt.bar(r2, PTS_means, color='orange', width=barWidth, label='Points per Game')
plt.bar(r3, GP_means, color='green', width=barWidth, label='Games per Year')
plt.bar(r4, MIN_means, color='yellowgreen', width=barWidth, label='Minutes per Game')
plt.bar(r5, SALARY, color='red', width=barWidth, label='SALARY in Millions')

plt.legend(bbox_to_anchor=(1, 1, 0.6, 0), loc=2, ncol=1, mode="normal", borderaxespad=1)
plt.show()


# In[176]:


shooting_guard_stats_df = players_index_df.loc[players_index_df['POSITION'] == ' SG' ,["YEAR","TEAM","POSITION","PTS","SALARY","REB","MIN", "GP"]]
shooting_guard_stats_df.tail(40)


# In[160]:


#plot graph for salary correlation to position 'SG' for clippers
# Shooting Guard positions get paid less 

#set with of bar
barWidth = 0.15
# Add xticks on the middle of the group bars
plt.title('Stats for Shooting Guards for Clippers')
plt.xlabel('group', fontweight='bold')
plt.ylabel('group', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(PTS_means))], ['JJ Redick (SG) 2015', 'JJ Redick (SG) 2016', 'Alan Anderson (SG) 2016', 'Lou Williams (SG) 2017', 'Jerome Robinson (SG) 2018', 'Lou Williams (SG) 2018', 'Shai Gilgeous-Alexander (SG) 2018', 'Terance Mann (SG) 2019', 'Rodney McGruder (SG) 2019', 'Lou Williams (SG) 2019'],rotation=90)

#set height of bars
REB_means = [1.9, 2.2, 0.8, 2.5, 2.5, 1.2, 2.2, 3.0, 2.8, 1.0]
PTS_means = [16.3, 15.0, 2.9, 22.6, 3.4, 20, 10.8, 2.2, 3.6, 19.8]
GP_means = [75, 78, 30, 79, 33, 75, 82, 24, 28, 37]
MIN_means = [28, 28.2, 10.3, 32.8, 9.7, 26.6, 26.5, 8.5, 16.6, 30.4]
SALARY = [7.08, 7.37, 0.98, 7, 3.04, 8.0, 3.37, 1, 4.8, 8]

# the label locations
r1 = np.arange(len(PTS_means))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]
r5 = [x + barWidth for x in r4]

#create group based on highest paid players
plt.xlabel("Shooting Guard Clippers")
plt.ylabel("(Millions for Salary)")
 
#make plot
#highest_paid.plot(r1,highest_paid["SALARY"],kind="bar",figsize=(20,3))

#Plot bar and colors and labels
plt.bar(r1, REB_means, color='blue', width=barWidth, label='Rebounds per Game')
plt.bar(r2, PTS_means, color='orange', width=barWidth, label='Points per Game')
plt.bar(r3, GP_means, color='green', width=barWidth, label='Games per Year')
plt.bar(r4, MIN_means, color='yellowgreen', width=barWidth, label='Minutes per Game')
plt.bar(r5, SALARY, color='red', width=barWidth, label='SALARY in Millions')

plt.legend(bbox_to_anchor=(1, 1, 0.6, 0), loc=2, ncol=1, mode="normal", borderaxespad=1)
plt.show()


# In[177]:


power_forward_stats_df = players_index_df.loc[players_index_df['POSITION'] == ' PF' ,["YEAR","TEAM","POSITION","PTS","SALARY","REB","MIN", "GP"]]
power_forward_stats_df


# In[143]:


#plot graph for salary correlation to position 'PF' for clippers
# power forward positions inconsistent pay ratio to points scored; some get paid less than others even though they score points

#set with of bar
barWidth = 0.15
# Add xticks on the middle of the group bars
plt.title('Power Forwards for Clippers')
plt.xlabel('group', fontweight='bold')
plt.ylabel('group', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(PTS_means))], ['Blake Griffin (PF) 2016', 'Blake Griffin (PF) 2017', 'Danilo Gallinari (PF) 2017', 'Montrezl Harrell (PF) 2017', 'Danilo Gallinari (PF) 2018', 'Montrezi Harrell (PF) 2018', 'Patrick Patterson (PF) 2019', 'Montrezl Harrell (PF) 2019', 'Mfiondu Kabenge (PF) 2019', 'JaMychal Green (PF) 2019'],rotation=90)

#set height of bars
REB_means = []
PTS_means = [21.6, 22.6, 15.3, 11, 19.8, 16.6, 5.1, 19.3, 2.9, 6.9]
GP_means = [61, 33, 21, 76, 68, 82, 35, 39, 10, 31]
MIN_means = [34, 34.5, 32, 17, 30.3, 26.3, 14.1, 29.2, 4.4, 21.2]
SALARY = [20.1, 32.08, 20.55, 1.4, 21.5, 6, 1.6, 6, 1.97, 4.76]

# the label locations
r1 = np.arange(len(PTS_means))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]
r5 = [x + barWidth for x in r4]


#create group based on highest paid players
plt.xlabel("Power Forward Players")
plt.ylabel("(Millions for Salary)")
 
#make plot
#highest_paid.plot(r1,highest_paid["SALARY"],kind="bar",figsize=(20,3))

#Plot bar and colors and labels
plt.bar(r1, REB_means, color='blue', width=barWidth, label='Rebounds per Game')
plt.bar(r2, PTS_means, color='orange', width=barWidth, label='Points per Game')
plt.bar(r3, GP_means, color='green', width=barWidth, label='Games per Year')
plt.bar(r4, MIN_means, color='yellowgreen', width=barWidth, label='Minutes per Game')
plt.bar(r5, SALARY, color='red', width=barWidth, label='SALARY in Millions')

plt.legend(bbox_to_anchor=(1, 1, 0.6, 0), loc=2, ncol=1, mode="normal", borderaxespad=1)
plt.show()


# In[167]:


small_forward_stats_df = players_index_df.loc[players_index_df['POSITION'] == ' SF' ,["YEAR","TEAM","POSITION","PTS","SALARY","REB","MIN", "GP"]]
small_forward_stats_df


# In[173]:


#plot graph for salary correlation to position 'SF' for clippers
# small forward positions; Kawhi Leonard 2019 highest paid; high points 25pts avg per game; low games played; but others low pay

#set with of bar
barWidth = 0.15
# Add xticks on the middle of the group bars
plt.title('Small Forwards for Clippers')
plt.xlabel('group', fontweight='bold')
plt.ylabel('group', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(PTS_means))], ['Paul Pierce (SF) 2015', 'Branden Dawson (SF) 2015', 'Paul Pierce (SF) 2016', 'Tobias Harris (SF) 2017', 'Paul George (SF) 2019', 'Maurice Harkless (SF) 2019', 'Kawhi Leonard (SF) 2019'],rotation=90)

#set height of bars
REB_means = [2.7, 0.7, 1.9, 6.0, 6.1, 3.8, 7.5]
PTS_means = [6.1, 0.8, 3.2, 19.3, 23.5, 5.7, 25.8]
GP_means = [68, 6, 25, 32, 26, 40, 30]
MIN_means = [18.1, 4.8, 11.1, 34.5, 30.7, 22.9, 32.2]
SALARY = [3.37, 0.5, 3.5, 16, 30.5, 11, 32.7]

# the label locations
r1 = np.arange(len(PTS_means))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]
r5 = [x + barWidth for x in r4]

#create group based on highest paid players
plt.xlabel("Small Forward Players")
plt.ylabel("(Millions for Salary)")
 
#make plot
#highest_paid.plot(r1,highest_paid["SALARY"],kind="bar",figsize=(20,3))

#Plot bar and colors and labels
plt.bar(r1, REB_means, color='blue', width=barWidth, label='Rebounds per Game')
plt.bar(r2, PTS_means, color='orange', width=barWidth, label='Points per Game')
plt.bar(r3, GP_means, color='green', width=barWidth, label='Games per Year')
plt.bar(r4, MIN_means, color='yellowgreen', width=barWidth, label='Minutes per Game')
plt.bar(r5, SALARY, color='red', width=barWidth, label='SALARY in Millions')

plt.legend(bbox_to_anchor=(1, 1, 0.6, 0), loc=2, ncol=1, mode="normal", borderaxespad=1)
plt.show()


# In[168]:


center_stats_df = players_index_df.loc[players_index_df['POSITION'] == ' C' ,["YEAR","TEAM","POSITION","PTS","SALARY","REB","MIN", "GP"]]
center_stats_df


# In[169]:


#plot graph for salary correlation to position 'C' for clippers
# Center positions 

#set with of bar
barWidth = 0.15
# Add xticks on the middle of the group bars
plt.title('Centers for Clippers')
plt.xlabel('group', fontweight='bold')
plt.ylabel('group', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(PTS_means))], ['DeAndre Jordan (C) 2015', 'Cole Aldrich (C) 2015', 'Diamond Stone (C) 2016', 'DeAndre Jordan (C) 2016', 'Boban Marjanovic (C) 2017', 'DeAndre Jordan (C) 2017', 'Willie Reed (C) 2017', 'Marcin Gortat (C) 2018', 'Ivica Zubac (C) 2019'],rotation=90)

#set height of bars
REB_means = [13.8, 4.8, 0.9, 13.8, 4.4, 15.2, 3.1, 5.6, 6.8]
PTS_means = [12.7, 5.5, 1.4, 12.7, 5.9, 12, 4.9, 5, 8.2]
GP_means = [77, 60, 7, 81, 20, 77, 39, 47, 40]
MIN_means = [33.7, 13.3, 3.5, 31.7, 8.3, 31.5, 10.7, 16, 17.3]
SALARY = [19.6, 1.1, 0.54, 21.1, 7, 22.6, 1.47, 13.5, 6.4]

# the label locations
r1 = np.arange(len(PTS_means))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]
r5 = [x + barWidth for x in r4]


#create group based on highest paid players
plt.xlabel("Centers Players")
plt.ylabel("(Millions for Salary)")
 
#make plot
#highest_paid.plot(r1,highest_paid["SALARY"],kind="bar",figsize=(20,3))

#Plot bar and colors and labels
plt.bar(r1, REB_means, color='blue', width=barWidth, label='Rebounds per Game')
plt.bar(r2, PTS_means, color='orange', width=barWidth, label='Points per Game')
plt.bar(r3, GP_means, color='green', width=barWidth, label='Games per Year')
plt.bar(r4, MIN_means, color='yellowgreen', width=barWidth, label='Minutes per Game')
plt.bar(r5, SALARY, color='red', width=barWidth, label='SALARY in Millions')

plt.legend(bbox_to_anchor=(1, 1, 0.6, 0), loc=2, ncol=1, mode="normal", borderaxespad=1)
plt.show()


# In[171]:


point_guard_stats_df = players_index_df.loc[players_index_df['POSITION'] == ' PG' ,["YEAR","TEAM","POSITION","PTS","SALARY","REB","MIN", "GP"]]
point_guard_stats_df


# In[172]:


#plot graph for salary correlation to position 'PG' for clippers
# Point Guards positions 

#set with of bar
barWidth = 0.15
# Add xticks on the middle of the group bars
plt.title('Point Guards for Clippers')
plt.xlabel('group', fontweight='bold')
plt.ylabel('group', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(PTS_means))], ['Pablo Prigioni (PG) 2015', 'Chris Paul (PG) 2015', 'Austin Rivers (PG) 2015', 'Chris Paul (PG) 2016', 'Austin Rivers (PG) 2016', 'Austin Rivers (PG) 2017', 'Avery Bradley (PG) 2017', 'Patrick Beverly (PG) 2017', 'Patrick Beverley (PG) 2018', 'Patrick Beverley (PG) 2019', 'Derrick Walton, Jr. (PG) 2019'],rotation=90)

#set height of bars
REB_means = [1.9, 4.2, 1.9, 5.0, 2.2, 2.4, 3.7, 4.1, 5.0, 6.2, 0.7 ]
PTS_means = [2.5, 19.5, 8.9, 18.1, 12, 15.1, 9.2, 12.2, 7.6, 8.1, 2.5]
GP_means = [59, 74, 67, 61, 74, 61, 6, 11, 78, 32, 20]
MIN_means = [13.9, 32.7, 21.8, 31.5, 27.8, 33.7, 27.5, 30.3, 27.4, 29.1, 10.3]
SALARY = [0.9, 21.4, 3.1, 22.8, 11, 12.6, 8.8, 5.5, 5, 12.3, 1.4]

# the label locations
r1 = np.arange(len(PTS_means))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]
r5 = [x + barWidth for x in r4]


#create group based on highest paid players
plt.xlabel("Point Guards Players")
plt.ylabel("(Millions for Salary)")
 
#make plot
#highest_paid.plot(r1,highest_paid["SALARY"],kind="bar",figsize=(20,3))

#Plot bar and colors and labels
plt.bar(r1, REB_means, color='blue', width=barWidth, label='Rebounds per Game')
plt.bar(r2, PTS_means, color='orange', width=barWidth, label='Points per Game')
plt.bar(r3, GP_means, color='green', width=barWidth, label='Games per Year')
plt.bar(r4, MIN_means, color='yellowgreen', width=barWidth, label='Minutes per Game')
plt.bar(r5, SALARY, color='red', width=barWidth, label='SALARY in Millions')

plt.legend(bbox_to_anchor=(1, 1, 0.6, 0), loc=2, ncol=1, mode="normal", borderaxespad=1)
plt.show()


# In[ ]:





# In[ ]:


get_ipython().system(' jupyter nbconvert')

