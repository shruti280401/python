import pandas as pd
data = pd.read_csv('7. Udemy Courses.csv')
print(data.head())

#printing data for different subjects which udemey is offering courses
print(data.subject.unique())#returns only unique element
#######print(pd.Series(data.subject))

#printing data for which subject has maximum no of courses
print(data.subject.value_counts())

#printing data for courses which are free of courses
myvar = data[data.is_paid == False]
########print(myvar.to_string())

#showing data for all courses which r paid
myvar = data[data.is_paid == True]
print(myvar)

#showing data for top selling courses
print(data.sort_values('num_subscribers',ascending=False))

#least selling courses
print(data.sort_values('num_subscribers'))

#all courses of graphic design where price is below 100
print(data[(data.price > '100') & (data.subject == 'Graphic Design') ]) #filtering

#all coursesrelated to python
print(data[data.course_title.str.contains('Python')])

#courses published in yr 2015
data['published_timestamp'] = pd.to_datetime(data.published_timestamp)
data['Year'] = data['published_timestamp'].dt.year
print(data[data.Year == 2015])

#max no of suscriber for each level of courses
data.level.unique()
print(data.groupby('level')['num_subscribers'].max())
print(data.groupby('level').max())


