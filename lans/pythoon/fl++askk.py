from flask import *
itz3obd_app = Flask(__name__)
 
myskills=[("css",50 ) ,("py",90 ),("c",70 ),("c#",0 ),("3oooo",67)]

@itz3obd_app.route("/")
def homepage():
    # return "this's me and this is the began"
    return render_template("homepage.html", 
                           title="homepage" ,
                           file_link ="home")#زود هنا اي حاجه ي برو 


@itz3obd_app.route("/about")
def about():
    return render_template("about.html",
                           title="aboutpage" )

@itz3obd_app.route('/add' )
def add():
    return render_template("add.html",
                           title="addpage" ,
                           file_link="add")

@itz3obd_app.route("/skills")
def skills():
    return render_template("skills.html", 
                           title="skillpage" ,
                           ph="This Is My Skills" ,
                           descrip=" All Skill About Me: ",
                           sk=myskills ,
                           file_link="skilll")

if __name__ == "__main__":
    itz3obd_app.run(debug=open, port=9000)
