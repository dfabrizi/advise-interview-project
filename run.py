#!interview_site\Scripts\python
from app import app
app.run(debug=True)


##If you want to make it live and viewable on a local network 
##replace app.run(debug=true) with app.run('0.0.0.0')