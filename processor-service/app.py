from flask import Flask, request

app = Flask(__name__)

# Store students grouped by branch
students_by_branch = {
    "CSE": [],
    "ECE": [],
    "EEE": [],
    "MECH": [],
    "UNKNOWN": []
}

@app.route("/", methods=["GET"])
def home():
    html = "<h1>Branch-wise Student List</h1><hr>"

    for branch, students in students_by_branch.items():
        html += f"<h2>{branch} Students</h2>"
        if not students:
            html += "<p>No students in this branch yet.</p><hr>"
            continue

        for s in students:
            html += s + "<br><br>"
        html += "<hr>"

    return html

@app.route("/process", methods=["POST"])
def process():
    data = request.get_json()
    branch = data.get("branch", "").upper()

    result = f"""
    <p><b>Name:</b> {data['name']}</p>
    <p><b>Age:</b> {data['age']}</p>
    <p><b>Gmail:</b> {data['gmail']}</p>
    <p><b>Roll No:</b> {data['rollno']}</p>
    <p><b>Branch:</b> {branch}</p>
    """

    # Decide correct branch bucket
    if branch not in ["CSE", "ECE", "EEE", "MECH"]:
        students_by_branch["UNKNOWN"].append(result)
    else:
        students_by_branch[branch].append(result)

    # Return student result to UI
    return f"""
    <h2>Student Branch Segregation Result</h2>
    {result}
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)
