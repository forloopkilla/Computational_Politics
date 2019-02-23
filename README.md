# Computational_Politics
These are my on-going research and codes to my master's thesis entitled "A Machine Learning Approach to Predicting China's Industrial Policy."

## Literature:
Why is predicting China’s Industrial Policy important? Many economies, governments, and businesses are closely watching China’s every economic policy to plan appropriate responses to political relationships and economic agreement with China. Government policy in China is set by ‘steering committees’, in both party and state at all levels of government. Policy is formed by the party, set into administrative regulation by the state bureaucracy and finally molded into legislation for passage through the National People's Congress Current literature (Chan & Zhong, 2018) have used machine learning to predict policy change with china’s news media propaganda (人民日报), but none have used online ministry data to directly predict China’s industrial policy tightening. Metadata features like posts website address section code, date, title of the posts, and ministry name, etc can be used to predict China’s Industrial policy change. The policy tightening/loosening will be defined by an Index. The ML model training windows will be consisted of quarters and predict on “future forecasted” quarters (which the labels are already given). Unlike the previous mentioned literature, this will be more focused on short-term industrial policy tightening or loosening predictions, 1 to 5 quarters, as oppose to long term structural changes. In the calculations of the China’s Industrial Policy Index (CIPI), main industry sectors that are associated with the most industrial policy “hot industries” will be given individual indexes that compose the General Industrial Policy Index. Think of stock market indices like the SP500 are consisted of the best performing stocks, the CIPI are composed of industries/sectors that are the government is focused on controlling (thus publishing more policies). Theoretically, this research will consider data from the government ministry posts, economic indicators, and potentially financial indicators to predict China’s Industrial Policy tightening and Control.

## Research Question: With China increasingly publishing industrial policy programs, how can stakeholders track and predict China’s Industrial Policy?
## Solution: creating the China Industrial Policy Index (CIPI)
How? Through scraped ministry online data to train Natural Language Process Model to analyze the relationship between ministry online data and other metadata signals to predict tightening or loosening of a China’s Industrial Policy? 
-	How measure the tightening and loosening of policy?
-	How to track the relationship between media and state?

### What this project is NOT about:
-	Not about predicting a certain policy coming out
-	Not about 100% accurate in predicting the time window of the policy publishing.
