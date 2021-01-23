# Lab 3 - Analyzing Tweets 

## Names: Sara Díaz - Gabriela Martinez

## Task 3.2: Analyzing tweets - Counting terms

One of the retrieved tweets gave us this information:

[('…', 196), (':', 195), ('RT', 145), ('#ArtificialIntelligence', 86), ('to', 67), ('the', 67), ('#AI', 57), ('.', 48), ('of', 46), ('in', 46)]<br/>
[('#ArtificialIntelligence', 86), ('#AI', 57), ('#MachineLearning', 25), ('#artificialintelligence', 21), ('#DeepLearning', 17), ('#BigData', 16), ('#Industry40', 14), ('#IoT', 11), ('#', 10), ('#DataScience', 10)]<br/>
[('…', 196), ('The', 34), ('Read', 29), ('Artificial', 26), ('AI', 25), ('Intelligence', 17), ('This', 17), ('Ronald_vanLoon', 16), ('How', 14), ('Is', 14)]<br/>

## Task 3.3: Case study

For this exercise, we analyzed the most common hashtags related to the term "Machine Learning". The plot we obtained was the following:

![Plot related to machine learning](https://github.com/mgmartinezl/CLOUD-COMPUTING-CLASS-2019/blob/master/Labs-solutions/Lab3/CaseStudy.png)

## Task 3.4: Student proposal

### Q34: Write in README.md a brief description of your proposal and the compelling insights that you have gained on this topic.

For this proposal, we wanted to observe the most common terms and hashtags that reflect people’s reaction to news related to Donald Trump (e.g. Trump's 2020 budget allocation).

From the script we created, we extracted the top 5 most common terms and hashtags related to Donald Trump and this is what we got:

[('#POTUS', 5), ('#Trump', 4), ('#Venezuela', 4), ('#Ohio', 4), ('#BackfireTrump', 4)]<br/>
[('Trump', 222), ('President', 45), ('budget', 42), ('Medicare', 40), ('people', 39)]<br/>

Main insights found:

* In this context, we can see that the hashtags "#POTUS" and "#Trump" and the frequent terms "Trump" and "President" refer explicitly to Donald Trump. 

* People are talking about "#Venezuela" given the current humanitarian crisis there and the fact that the US has pulled all its remaining diplomatic staff from the country (article published on the news two hours ago).

* Additionally, people are mentioning tweets under the hashtag "#Ohio" because Donald Trump is asking to reduce 2020 budget funds for different cultural and social communities and programs of this state.

* Moreover, the hashtag "#BackFireTrump" has to do with the auto-tweet generator under the account @backfiretrump, which posts a tweet every time an American dies because of gun violence. This account aims to protest agains the lack of regulation to gun ownership.

* Note that the frequent term "budget" refers to the proposal for the 2020 budget that Donald Trump delivered to the House of Representatives. This budget proposal includes a cut for the "Medicare" program, the public health system for the elderly (let us remember that Donald Trump had promised not to destroy this program before).

### Q35: 
### How long have you been working on this session?
One hour and 45 minutes.

### What have been the main difficulties you have faced and how have you solved them?
The main difficulty we had was related to the understanding of how jsons are generated in real time from the real-time Twitter API. However, the scripts helped us figuring it out.
