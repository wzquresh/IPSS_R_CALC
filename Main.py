from flask import Flask, render_template, request

app = Flask(__name__)


# Cytogenic group: VG: 0, G: 1, I: 2, P: 3, VP: 4
def getcg(cg):
    switcher = {
        "VG": 0,
        "G": 1,
        "I": 2,
        "P": 3,
        "VP": 4
    }
    print(cg)
    print(switcher["VP"])
    print(switcher.get(str.upper(cg),0))
    return switcher[str.upper(cg)]

# HG Blasts: <=2: 0, >2 to 5<: 1, 5 to 10: 2, >10: 3
def gethg(hg):
    if hg <= 2:
        return 0
    elif 2 < hg < 5:
        return 1
    elif 5 <= hg <= 10:
        return 2
    else:
        return 3


# Platelets: >=100: 0, 50 to <100: 0.5, <50: 1
def getplatelets(platelets):
    if platelets >= 100:
        return 0
    elif 100 < platelets >= 50:
        return 0.5;
    else:
        return 1


# ANC: >=0.8: 0, <0.8: 0.5
def getanc(anc):
    if anc >= 0.8:
        return 0
    else:
        return 0.5


# Hemoglobin: >=10: 0, 8 to <10: 1, <8: 1.5
def getheme(heme):
    if heme >= 10:
        return 0
    elif 10 > heme >= 8:
        return 1
    else:
        return 1.5


# Risk Category: VL: <=1.5, L: >1.5 to 3, I: >3 to 4.5, H: >4.5 to 6, VH: >6
def getriskcat(risk):
    if risk <= 1.5:
        return "Very Low"
    elif 1.5 < risk <= 3:
        return "Low"
    elif 3 < risk <= 4.5:
        return "Intermediate"
    elif 4.5 < risk <= 6:
        return "High"
    else:
        return "So Very Incredibly High OH MY GOD"


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("main.html")
    elif request.method == 'POST':
        #Access the Users Inputs
        #CG = str(request.args.get('cg', '0'))
        CG = request.form['cg']
        HG = float(request.args.get('hg', '0'))
        platelets = float(request.args.get('platelets', '0'))
        ANC = float(request.args.get('anc', '0'))
        heme = float(request.args.get('heme', '0'))
        #Call the adding functions
        risk = getcg(CG) + gethg(HG) + getplatelets(platelets) + getanc(ANC) + getheme(heme)
        #Associate number with value
        riskcat = getriskcat(risk)
        answer = "Risk: %s %s" % (risk, riskcat)
        return render_template('main.html', text=answer)

# Print score and Risk Category
# pages with variables <username> or <int:id>
# route two pages to same url: list @app.route<'/whatever'>


if __name__ == "__main__":
    app.run(debug=True)
