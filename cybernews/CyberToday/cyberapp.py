from flask import Flask 
import subprocess
from flask import render_template_string
import csv

subprocess.run('scrapy crawl cyberspider -O CyberToday/CyberToday.csv', shell=True)
subprocess.run('scrapy crawl cyberspider2 -o CyberToday/CyberToday.csv', shell=True)
subprocess.run('scrapy crawl cyberspider3 -o CyberToday/CyberToday.csv', shell=True)
subprocess.run('scrapy crawl cyberspider4 -o CyberToday/CyberToday.csv', shell=True)
subprocess.run('scrapy crawl cyberspider5 -o CyberToday/CyberToday.csv', shell=True)

app = Flask(__name__)

@app.route('/')
def read():
    # variable to hold CSV data
    data = []
    
    # read data from CSV file
    with open('CyberToday/CyberToday.csv', encoding="utf-8") as f:
        # create CSV dictionary reader instance
        reader = csv.DictReader(f)
        # init CSV dataset
        [data.append(dict(row)) for row in reader]     
  
    return render_template_string('''
       <!DOCTYPE html>
         <head>
            <!--Bootstrap CSS-->
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css"/>
         </head>
         <body style="background-image: url('https://socradar.io/wp-content/uploads/2020/12/socradar-web-cover-home.png'); background-repeat: no-repeat; background-attachment: fixed; background-size: cover;" >
           <div class="container">        
             <!--CSV-->
             <table class="table table-striped mt-2" style="max-width: 100%; border: 1px solid black;">
             <!--All Titles-->
               <thead>
                  <tr style="background-color: #DCEAF5;">
                    {% for header in data[0].keys() %}
                     <th scope="col" style="font-weight: normal;">
                        {% if header == list(data[0].keys())[1] %}
                          <a style="color:#0B3A64; font-size:18px;"><b>Cyber Security News</b></a>
                        {% endif %}
                        {{ header }}
                     </th>
                   {% endfor %}
               </thead>
               <!--Rows-->
               <tbody>
                 {% for row in range(0, len(data)) %}
                   <tr style="background-color: #DCEAF5;" id="{{row}}">
                     {% for col in range(0, len(list(data[row].values()))) %}
                       <td style="word-break: break-word;">
                          {% if row == 10 and col == 3 or row == 21 and col == 3 or row == 32 and col == 3 or row == 40 and col == 3 %}
                            <a>Link</a>
                          {% elif row == 10 and col == 1 %}
                            <a style="color:#0B3A64; font-size:18px;"><b>Malware & Vulnerability News</b></a>
                          {% elif row == 21 and col == 1 %}
                            <a style="color:#0B3A64; font-size:18px;"><b>Breaches and Incidents</b></a>
                          {% elif row == 32 and col == 1 %}
                            <a style="color:#0B3A64; font-size:18px;"><b>From HackerNews</b></a>
                          {% elif row == 40 and col == 1 %}
                            <a style="color:#0B3A64; font-size:18px;"><b>From Bleeping Computer</b></a>
                          {% elif col == 3 %}
                            <a class="btn" style="background-color: #EB4757; height: 40px; width: 80px;" href="{{ list(data[row].values())[col] }}" target="_blank">Click</a>
                          {% elif col == 0 %}
                           <a>{{ list(data[row].values())[col] }}</a>
                          {% else %}
                           {{ list(data[row].values())[col] }}
                          {% endif %}
                     {% endfor %}
                 {% endfor %}
               </tbody>
             </table>
           </div>
         </body>
       </html>
    ''', data=data, list=list, len=len, str=str)
  
if __name__ == '__main__':
    app.run(host="localhost", port=int("5000"))
