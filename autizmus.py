print("Welcome To Who Wants to be a Millionaire")
print ("First Question: In the children's book series, where is Paddington Bear originally from?")
print ("Choices: ")
print ("------")
print ("India")
print ("Canada")
print ("Peru")
print ("Iceland")
print ("-------")
def keep_going():
  answer = raw_input("What is your Choice?: ")
  if answer == "Peru":
      print "Right Answer! Good Luck in Next round!"
      print "Second Round!"
      print "The Question is:What letter must appear at the beginning of the registration number of all non-military aircraft in the U.S.?"
      print "Choices: "
      print "N"
      print "A"
      print "U"
      print "L"
  answer2 = raw_input("What is your Choice?: ")
  if answer2 == "N":
    print "Right Answer Good luck in the third round!"
    print "Welcome to the third round , u are fighting for 5000 dollars! please share applause for this guy!"
    print " Ok , so back to the question"
    print " The Question is: Who delivered the less famous two-hour speech that preceded Abraham Lincoln's two-minute Gettysburg Address?"
    print " The Choices are: "
    print " Wenndell Phillips"
    print " Daniel Webster"
    print "Rober G. Ingersoll"
    print "Edwart Everett"
  answer3 =raw_input("What is your Choice?: ")
  if answer3 == "Edwart Everett":
    print "is it right?"
    print "Yes , it is! You are going to fourth round!"
    print "Welcome to the Fourth Round"
    print " You are Fighting for 10000 dollars"
    print " Lets get right to the question!"
    print " The question is: Nephelococcygia is the practice of doing what?"
    print " Here are the choices: "
    print " Finding Shapes in clouds"
    print " Sleeping with your eyes open"
    print " Breaking glass with your voice"
    print " Swimming in the Freezing water"
  answer4 =raw_input("What is your Choice?: ")
  if answer4 == "Finding Shapes in clouds":
    print "Well , it may be but what bout Breaking Glass with your voice?"
    print "We'll reveal the answer in 5 seconds"
    print "1"
    print "2"
    print "3"
    print "4"
    print "5"
    print " You Got it Right! You got 10000 dollars on your account!"
    print " Welcome to the Fifth Round!"
    print "You are Fighting for 100000 dollars! this is the penultimate question!"
    print " The Question is: Which insect shorted out an early supercomputer and inspired the term computer bug?"
    print " The Choices are: "
    print " Moth "
    print " Roach "
    print " Fly "
    print " Japanese Beetle "
  answer5 =raw_input("What is your Choice?: ")
  if answer5 == "Moth":
    print "You are GOING TO THE LAST ROUND TO FIGHT FOR MILLION DOLLARS!!"
    print " Ladies and Gentlemen , this is the LAST ROUND OF WHO WANTS TO BE A MILLIONAIRE, WE ARE FIGHTING FOR ONE MILLION DOLLARS!"
    print  "Are you ready? type yes when you're ready"
    answerforready =raw_input("Am I?")
    if answerforready == "yes":
      print "Ok so the last question is: Which of the following landlocked countries is entirely contained within another country?"
      print "Here are the choices!: "
      print " Lesotho"
      print " Burkina Faso"
      print " Mongolia"
      print " Luxembourg"
      print " Are you ready to answer,type yes when you're ready"
    answerfoready2 =raw_input("Am I?")
    if answerfoready2 == "yes":
      print "Okay , Lets go, you've got 45 seconds, if you have problems you can still choose one of the final round helpers that are not that accurate but if you're lucky enough you will win with them"
    usejokers =raw_input("Do i want to use helpers?")
    if usejokers == "yes":
      print "The Right answer should be Lesotho but im not sure enough!"
    answer6 = raw_input("What is your Choice?: ")
    if answer6 == "Lesotho":
      print "YOU WON ONE MILLION DOLLARS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    copyrightclaim =raw_input("Do you want to see who created the game?")
    if copyrightclaim == "yes":
      print "Matthew Petrinec - Creator"
      print " 2017 "
    else:
        print "Bad Answer !"
        print "Please Quit!"
keep_going()