import os
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)


# == Your Routes Here ==

# # Request: ===============
# POST /submit

# # With body parameters:
# name=Leo
# message=Hello world

# # Expected response (2OO OK):
# Thanks Leo, you sent this message: "Hello world"
@app.route('/submit', methods = ['POST'])
def return_welcome():
    name = request.form ['name']
    message = request.form ['message']
    return f"Thanks {name}, you sent this message:{message}"


# # Request: ==================
# GET /wave?name=Leo

# # Expected response (200 OK):
# I am waving at Leo

@app.route('/wave', methods = ['GET'])
def wave_at_caller():
    name = request.args ['name']
    return f"I am waving at {name}"

# def test_post_count_vowels_eee(web_client): =================
#     response = web_client.post('/count_vowels', data={'text': 'eee'})
#     assert response.status_code == 200
#     assert response.data.decode('utf-8') == 'There are 3 vowels in "eee"'

# test for vowels
# GET /count_vowels?text= text

@app.route('/count_vowels', methods = ['POST'])
def count_vowels_in_text():
    text = request.form ['text']
    vowel_num = 0
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    for char in text:
        if char in vowels:
            vowel_num +=1

    return f'There are {vowel_num} vowels in "{text}"'


# # Request: ==================================
# POST http://localhost:5001/sort-names

# # With body parameters:
# names=Joe,Alice,Zoe,Julia,Kieran

# # Expected response (sorted list of names):
# Alice,Joe,Julia,Kieran,Zoe


@app.route('/sort_names', methods = ['POST'])
def sort_names():
    names_string = request.form ['names']
    names_list = names_string.split(",")
    names_list.sort()
    return (','.join(names_list)) 





# # Request: ==================================
# GET /names?add=Eddie

# # This route should return a list of pre-defined names, plus the name given.

# # Expected response (2OO OK):
# Julia, Alice, Karim, Eddie

@app.route('/names', methods = ['GET'])
def names():
    name = request.args ['add']
    name_string = 'Julia, Alice, Karim'
    name_string = name_string + f', {name}'
    return name_string




# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

