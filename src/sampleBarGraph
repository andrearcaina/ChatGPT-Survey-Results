import matplotlib.pyplot as plt

#data for the bars
x = ['Architecture', 'Arts', 'Business', 'Community Service', 'Economics', 'Engineering', 'Human Geography', 'Math and Science', 'Mathematics', 'Science', 'Science and Business']
y1HaveNotUsed = [1, 5, 5, 2, 2, 6, 0, 2, 0, 21, 0]
y2No = [0, 3, 2, 3, 0, 1, 0, 0, 1, 5, 1]
y3Yes = [0, 2, 2, 0, 0, 4, 1, 0, 0, 17, 0]

newBottom = [1,8,7,5,2,7,0,2,1,26,1]

#in inches for some reason???? needs to be big because of x axis
plt.figure(figsize=(20,6))

haveNotColor = '#064042'
noColor = '#7281C1'
yesColor = '#931EBF'

# create a stacked bar graph
plt.bar(x, y1HaveNotUsed, color = haveNotColor, label='I have not used ChatGPT for academia')
plt.bar(x, y2No, bottom=y1HaveNotUsed, color = noColor, label='No')
plt.bar(x, y3Yes, bottom=newBottom, color = yesColor, label='Yes')

# add title and axis labels
plt.title("If you have used ChatGPT for academia, did you see an improvement in your grade? VS Students' majors")
plt.xlabel('Majors')
plt.ylabel('Number of Students')

# add legend
plt.legend()

# show the graph
plt.show()
