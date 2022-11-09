from flask import Flask, request, send_from_directory
import controller


app = Flask(__name__)

@app.route("/rotate", methods = ["POST"])
def rotate():
    try:
        f = request.files['file']
        page_numbers = request.form["page_numbers"]
        angle = request.form["angle"]
        print(page_numbers, angle)

        res = controller.rotate_and_save(f, page_numbers, angle)
        print(res)
        if res:
            return {"result": True, "url": res}
    
    except Exception as e:
        print(e)
    
    return {"result": False}


@app.route('/file/<path:path>')
def send_pdf(path):
    return send_from_directory('outputs', path)


if __name__ == "__main__":
    app.run(
        host = "127.0.0.1",
        port = 8000,
        debug = True
    )