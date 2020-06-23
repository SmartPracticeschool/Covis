# Analysis of sentiments during COVID-19
## Starting the project





# Step 1. Gathering the data from ieee site (^_^)
### The data that we have downloaded from ieee site only contains the *text-id's and Sentiments of those tweets which were related to COVID-19 , but the problem is here that we can't feed text-id's and sentiments to our ML model , Our ML model needs actual texts 

### So to deal with this issue we have created a section Data_collection in which we have 4 important python files 
### (|)  {csv_to_text.py} is used to convert csv files to text files which will be further feeded to HYDRATOR to gather all the features { Text , Date , Location etc } of the id holder , HYDRATOR return all this data in {json} format 
### (||)  After getting the {json} files from HYDRATOR , we use our {add_sentiments.py} and {add_sentiments.py} to extract all the necessary features { Text id , Text , Date , Location etc } to train our ML model 
### (|||)  Now the above 2 steps were performed on a number of small csv files which we had downloaded from ieee site , so we decided to concatenate all the smaller files to a bigger one which is done using {into_one_csv.py}


# Step 2 Data Preprocessing phase begins from here (^_^)
### Despite all this hard work , our data still needs some more changes to be ready for our ultimate goal which is obviously MODEL TRAINING!!!
### [$] We have provided a file named {model_training.ipynb} in which we firstly cleans data , checks it's accuracy and then finally train it on our ML model 
### [$] Now we have 5 features in our data {Text_Id , Text , Date , Location , Sentiments } , and from these 5 , first 4 are our independent features and 5th one is our Dependent/Target feature
### [$] Firstly we modify our date variable and remove unnecessary things such as timezone from it because we have already included a separated feature location in our dataset
### [$] After we have changed our dependent feature 'Sentiments' date from continuous form to discrete form so that our model can easily differentiate between Positive , Negative and Neutral sentiments...
#### (|)   if value < 0 , assign new_value == -1 [Negative sentiment]
#### (||)  if value > 0 , assign new_value == +1 [Positive sentiment]
#### (|||) if valuee == 0 , assign new_value == 0[Neutral sentiment]

### [$] We had done some other changes such as converting all the words to lowercase , removing '\#' special symbol , '@'character  and extra spaces from texts
