from nltk.sentiment.vader import SentimentIntensityAnalyzer 

from tkinter import *
 
def clearAll() : 
	
	negative.delete(0, END) 
	neutral.delete(0, END) 
	positive.delete(0, END) 
	overall.delete(0, END) 

	textArea.delete(1.0, END) 
	
def sentiment_detect(): 

	sentence = textArea.get("1.0", "end") 

	sia = SentimentIntensityAnalyzer() 

	sd = sia.polarity_scores(sentence) 

	string = str(sd['neg']*100) + "% Negative"
	negative.insert(10, string) 
	

	string = str(sd['neu']*100) + "% Neutral"
	neutral.insert(10, string) 

	string = str(sd['pos']*100) +"% Positive"
	positive.insert(10, string) 

	if sd['compound'] >= 0.05 : 
		string = "Positive"

	elif sd['compound'] <= - 0.05 : 
		string = "Negative"
	

	else : 
		string = "Neutral"

	overall.insert(10, string) 
		

 
if __name__ == "__main__" : 
	
	gui = Tk() 
	
	gui.config(background = "light blue") 
 
	gui.title("Text Sentiment Detector") 

	gui.geometry("300x600") 

	enterText = Label(gui, text = "Type a Sentence", 
									bg = "light blue") 

	textArea = Text(gui, height = 10, width = 30, font = "serif") 
 
	check = Button(gui, text = "Sentiment Check", fg = "Black", 
						bg = "Red", command = sentiment_detect) 

	negative = Label(gui, text = "sentence is: ", 
										bg = "yellow") 
	
	neutral = Label(gui, text = "sentence was rated as: ", 
									bg = "blue") 
	
	positive = Label(gui, text = "sentence was rated as: ", 
										bg = "green") 


	overall = Label(gui, text = "Sentence Overall Rated As: ", 
										bg = "light green") 

	negative = Entry(gui) 

	neutral = Entry(gui) 
 
	positive = Entry(gui) 
 
	overall = Entry(gui) 
 
	clear = Button(gui, text = "Clear", fg = "Black", 
					bg = "Red", command = clearAll) 
	 
	Exit = Button(gui, text = "Exit", fg = "Black", 
						bg = "Red", command = exit) 

	enterText.grid(row = 0, column = 2) 
	
	textArea.grid(row = 1, column = 2, padx = 10, sticky = W) 
	
	check.grid(row = 2, column = 2) 
	
	negative.grid(row = 3, column = 2) 
	
	neutral.grid(row = 5, column = 2) 
	
	positive.grid(row = 7, column = 2) 
	
	overall.grid(row = 9, column = 2) 
	
	negative.grid(row = 4, column = 2) 

	neutral.grid(row = 6, column = 2) 
						
	positive.grid(row = 8, column = 2) 
	
	overall.grid(row = 10, column = 2) 
	
	clear.grid(row = 11, column = 2) 
	
	Exit.grid(row = 12, column = 2) 

	gui.mainloop() 
	
