import webbrowser, os

pscore = 10
pwickets = 2

cscore = 11
cwickets = 2

client_player = "Sanjana"
server_player = "Computer"
result = "SANJANA WON!"

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