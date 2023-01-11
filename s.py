import socket
import threading
import random
import webbrowser, os

class game(threading.Thread):
	dict = {1:'1',2:'2',3:'3',4:'4',6:'6'}
	valid_input = ['1','2','3','4','6']
	opt = ['BAT','BOWL']
	dict_opt = {1:'BAT',2:'BOWL'}
	error = "invalid input pls try again"
	
	def __init__(self,name,c,addr):
		threading.Thread.__init__(self)
		self.name = name
		self.c = c
		self.addr = addr
		
	def run(self):
		self.user_name = self.c.recv(1024).decode("utf-8")
		print("Game started of user "+self.user_name)
		Stage = 0
		wic = 0
		score = 0
		target = 0
		wiceq = 0


		while (Stage==0):
			user_input = self.c.recv(1024).decode("utf-8")
			if user_input in game.opt:
				if user_input == "BAT":
					result = "BAT FIRST"
					Stage = 1
				else:
					result = "BOWL FIRST"
					Stage = 5
				print("sending to user "+self.user_name+" "+result)
				self.c.send(result.encode("utf-8"))
			else:
				self.c.send("invalid input pls try again".encode("utf-8"))

		while(Stage==1):
			while (wic < 2):
				user_input = self.c.recv(1024).decode("utf-8")
				if user_input in game.valid_input:
					c = random.choice([1,2,3,4,6])
					comp = game.dict[c]
					if user_input == comp:
						result = "Wicket!!  "
						wic = wic + 1
						if(wic==2):
							Stage = 2
							target = score
					else:
						addscore = int(user_input)
						score = score + addscore
						if(addscore==1):
							result = "Single    "
						elif(addscore==2):
							result = "double    "
						elif(addscore==3):
							result = "Triple    "
						elif(addscore==4):
							result = "Four!!    "
						else:
							result = "SIX!!     "
					
					strwic = str(wic)
					strscore = str(score)

					strtosend = result+self.user_name+" "+strscore+"-"+strwic
					strversion = str(strtosend)
					print("sending to user "+self.user_name+" "+result+" "+strscore+"-"+strwic)
					self.c.send(strversion.encode("utf-8"))

				else:
					self.c.send("invalid input pls try again".encode("utf-8"))

		while(Stage==2):

			user_input = self.c.recv(1024).decode("utf-8")
			if user_input in game.valid_input:
				result = "COMPUTER'S TURN TO BAT"
				Stage = 3
				score = 0
				wic = 0
				wiceq = 0
				print("sending to user "+self.user_name+" "+result)
				self.c.send(result.encode("utf-8"))
			else:
				self.c.send("invalid input pls try again".encode("utf-8"))

		while(Stage==3):
			while (score<target):
				while (wiceq < 2):
					user_input = self.c.recv(1024).decode("utf-8")
					if user_input in game.valid_input:
						c = random.choice([1,2,3,4,6])
						comp = game.dict[c]
						if user_input == comp:
							result = "Wicket!!  "
							wic = wic + 1
							wiceq = wiceq + 1
							if(wiceq==2):
								if(score==target):
									result = "DRAW!!"
									output(self.user_name, score, wic, target, wiceq, result)
									Stage = 4
								else:
									result = "YOU WIN!!"
									output(self.user_name, target, wic, score, wiceq, result)
									Stage = 4

						else:
							addscore = int(comp)
							score = score + addscore
							if(score>target):
								result = "COMPUTER WIN!! "
								Stage = 4
								wiceq = 2
								output(self.user_name, target, wic, score, wiceq, result)

							elif(addscore==1):
								result = "Single    "
							elif(addscore==2):
								result = "double    "
							elif(addscore==3):
								result = "Triple    "
							elif(addscore==4):
								result = "Four!!    "
							else:
								result = "SIX!!     "
						
						strwic = str(wic)
						strscore = str(score)

						strtosend = result+" "+strscore+"-"+strwic
						strversion = str(strtosend)
						print("sending to user "+"COMP "+self.user_name+" "+result+" "+strscore+"-"+strwic)
						self.c.send(strversion.encode("utf-8"))

					else:
						self.c.send("invalid input pls try again".encode("utf-8"))
		
		while(Stage==4):
			self.c.recv(1024).decode("utf-8")
			print("Game over with "+self.user_name)
			self.c.send("GAME OVER".encode("utf-8"))

		
		while(Stage==5):
			while (wic < 2):
				user_input = self.c.recv(1024).decode("utf-8")
				if user_input in game.valid_input:
					c = random.choice([1,2,3,4,6])
					comp = game.dict[c]
					if user_input == comp:
						result = "Wicket!!  "
						wic = wic + 1
						if(wic==2):
							Stage = 6
							target = score
					else:
						addscore = int(comp)
						score = score + addscore
						if(addscore==1):
							result = "Single    "
						elif(addscore==2):
							result = "double    "
						elif(addscore==3):
							result = "Triple    "
						elif(addscore==4):
							result = "Four!!    "
						else:
							result = "SIX!!     "
					
					strwic = str(wic)
					strscore = str(score)

					strtosend = result+"COMP"+" "+strscore+"-"+strwic
					strversion = str(strtosend)
					print("sending to user "+"COMP "+self.user_name+" "+result+" "+strscore+"-"+strwic)
					self.c.send(strversion.encode("utf-8"))

				else:
					self.c.send("invalid input pls try again".encode("utf-8"))

		while(Stage==6):

			user_input = self.c.recv(1024).decode("utf-8")
			if user_input in game.valid_input:
				result = "YOUR'S TURN TO BAT"
				Stage = 7
				score = 0
				wic = 0
				wiceq = 0
				print("sending to user "+self.user_name+" "+result)
				self.c.send(result.encode("utf-8"))
			else:
				self.c.send("invalid input pls try again".encode("utf-8"))

		while(Stage==7):
			while (score<target):
				while (wiceq < 2):
					user_input = self.c.recv(1024).decode("utf-8")
					if user_input in game.valid_input:
						c = random.choice([1,2,3,4,6])
						comp = game.dict[c]
						if user_input == comp:
							result = "Wicket!!  "
							wic = wic + 1
							wiceq = wiceq + 1
							if(wiceq==2):
								if(score==target):
									result = "DRAW!!    "
									output(self.user_name, score, wic, target, wiceq, result)
									Stage = 8
								else:
									result = "COMPUTER WIN !! "
									output(self.user_name, target, wic, score, wiceq, result)
									Stage = 8

						else:
							addscore = int(user_input)
							score = score + addscore
							if(score>target):
								result = "YOU WIN"
								output(self.user_name, score, wic, target, wiceq, result)
								Stage = 8
								wiceq = 2

							elif(addscore==1):
								result = "Single    "
							elif(addscore==2):
								result = "double    "
							elif(addscore==3):
								result = "Triple    "
							elif(addscore==4):
								result = "Four!!    "
							else:
								result = "SIX!!     "
						
						strwic = str(wic)
						strscore = str(score)


						strtosend = result+self.user_name+" "+strscore+"-"+strwic
						strversion = str(strtosend)
						print("sending to user "+self.user_name+" "+result+" "+strscore+"-"+strwic)
						self.c.send(strversion.encode("utf-8"))

					else:
						self.c.send("invalid input pls try again".encode("utf-8"))

		while(Stage==8):
			self.c.recv(1024).decode("utf-8")
			print("Game over with "+self.user_name)
			self.c.send("GAME OVER".encode("utf-8"))



def output(client_player, pscore, pwickets, cscore, cwickets, result):
	server_player = "Computer"
	f = open("index.html", "w")
	f.write('''<!DOCTYPE html>
            <html>
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Hand Cricket Game</title>
                <link rel="stylesheet" href="/style.css">
            </head>

            <style>
            @import url("https://fonts.googleapis.com/css?family=Asap:400,500,700&display=swap");

            /* All */
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            /* Body */
            body {
                background-color: #292C34;
            }

            /* Header */
            header {
                background: white;
                padding: 20px;
            }

            header > h1 {
                color: #24272E;
                text-align: center;
                font-family: Asap, sans-serif;
            }

            /* Status Bar */
            .status {
                margin: 20px auto;
                border: 3px solid white;
                border-radius: 4px;
                text-align: center;
                width: 85%;
                color: white;
                font-size: 46px;
                padding: 15px 20px;
                font-family: Asap, sans-serif;
                position: relative;
            }


            #img_bat {
                position: relative;
                max-height: 46px;
                top: 10px;
                left: -30px;
            }

            #img_ball {
                position: relative;
                max-height: 46px;
                top: 10px;
                right: -30px;
            }

            /* To Remove bug of relative placement of bat & ball */

            /* To Do Scoreboard */

            /* Score-Card bar */
            .score-card {
                margin: 20px auto;
                border: 3px solid white;
                border-radius: 4px;
                text-align: center;
                width: 250px;
                color: white;
                font-size: 46px;
                padding: 15px 20px;
                font-family: Asap, sans-serif;
                position: relative;
            }

            .card-badge {
                background: #e25840;
                color: white;
                font-size: 14px;
                padding: 2px 10px;
                font-family: Asap sans-serif;
            }

            #runs-label {
                position: absolute;
                top: 30px;
                left: -25px;
            }

            #wickets-label {
                position: absolute;
                top: 30px;
                right: -30px;
            }


            #overs {
                width: 50%;
                background: #909090;
                color: white;
                font-size: 14px;
                padding: 2px 10px;
                font-family: Asap sans-serif;
                position: absolute;
                bottom: -24px;
                right: 0;
            }

            #target {
                width: 50%;
                background: #909090;
                color: white;
                font-size: 14px;
                padding: 2px 10px;
                font-family: Asap sans-serif;
                position: absolute;
                bottom: -48px;
                right: 0;
                visibility: hidden;
            }

            /* Who played what... and the result of that action */
            .results {
                margin-top: 60px;
                font-size: 40px;
                color: white;
                text-align: center;
            }

            #results-disp {
                margin: 20px;
                padding: 15px 15px;
                font-family: Asap, sans-serif;
                visibility: hidden;
            }

            #result-message {
                margin: 15px auto;
                padding: 15px 15px;
                text-align: center;
                /* font-weight: bold; */
                font-family: Asap, sans-serif;
            }

            .action-img {
                max-height: 80px;
                max-width: 80px;
                position: relative;
                top: 20px;
            }


            /* Choices for Game Play */
            .hand {
                max-height: 60px;
                max-width: 60px;
            }

            .Choices {
                margin: 30px 0;
                text-align: center;
            }

            .choice {
                border: 4px solid white;
                border-radius: 50%;
                margin: 0 12px;
                padding: 10px;
                display: inline-block;
                transition: all 0.3s ease;
            }

            .choice:hover {
                cursor: pointer;
                background: #3c404a;
            }

            /* Display "Make Your Move" */
            #action-message {
                text-align: center;
                color: white;
                font-size: 20px;
                font-weight: bold;
                font-family: Asap, sans-serif;
            }
            </style>

            <script>
                function startFirstInnings() {
                alert("Game On!\nAll the best to both the teams.");

                target = 0;
                target_p.style.visibility = "hidden";

                runs = 0;
                wickets = 0;
                overs = 0.0;
                
                p1name = "A Sarkar";
                p2name = "Computer";
                p1name_span.innerHTML = p1name;
                p2name_span.innerHTML = p2name;
                result_message_p.innerHTML = "The Game Started! Make your first move!";
                }

                

            </script>


            <body>
                    <!-- HEADER BAR -->
                    <header>
                        <h1>Hand Cricket</h1>
                    </header>

                <!-- STATUS BAR -->
                    <div class="status">
                        
                        <span class="status-txt" id="p1-name">''' + client_player + '''</span>
                        <span class="status-txt" id="status_center_text">&nbsp&nbspVS&nbsp&nbsp</span>
                        <span class="status-txt" id="p2-name">''' + server_player + ''' </span>
                        
                    </div>

                    <!-- FULL SCORE BOARD and TARGET RUNS, OVERS(to-do later) or FIRST BAT -->
                <div class="score-board">
                    <!-- TO DO-->
                </div>
            
                <!-- SCORE CARD (Runs/Wickets) -->
                <p id="action-message">PLAYER - ''' + client_player + ''''s SCORE</p>
                <div class="score-card">
                    <div id="runs-label" class="card-badge">runs</div>
                    <div id="wickets-label" class="card-badge">wickets</div>
                    <span id="runs">''' + str(pscore) + '''</span>/<span id="wickets">''' + str(pwickets) + '''</span>
                    <div class="score-card-footer">
                        <p id="target">Target: Nil</p>
                    </div>
                    
                </div>
                <br>

                <p id="action-message">COMPUTER's SCORE</p>
                <div class="score-card">
                    <div id="runs-label" class="card-badge">runs</div>
                    <div id="wickets-label" class="card-badge">wickets</div>
                    <span id="runs">''' + str(cscore) + '''</span>/<span id="wickets">''' + str(cwickets) + '''</span>
                    <div class="score-card-footer">
                        <p id="target">Target: Nil</p>
                    </div>
                    
                </div>

                <p id="action-message">''' + result + '''</p>

            

                <!-- Display "Make Your Move"--><br>
                <p id="action-message">Thank you for playing!</p>

            </body>
            </html>''')

	webbrowser.open('file://' + os.path.realpath("index.html"))


			

def Main():
	host = "192.168.1.102"
	port = 1234
	
	s = socket.socket()
	s.bind((host,port))
	
	s.listen(3)
	for i in range(3):
		print(str(i))
		c,addr = s.accept()
		print("connect with "+str(i))
		print("starting Game..... with "+str(i))
		game(str(i),c,addr).start()

	

if __name__ == "__main__":
	Main()

