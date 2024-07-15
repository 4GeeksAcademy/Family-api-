"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

#Get all members of Jackson's family
@app.route('/members', methods=['GET'])
def get_all_members():
    members = jackson_family.get_all_members()  
    if not members:
        return jsonify({"done": False, "msg":"Error"}), 400  
    return jsonify(members), 200 

#GET one member of Jackson's family
@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    one_member = jackson_family.get_member(member_id)  
    if not one_member:
        return jsonify({"done": False, "msg":"Error getting member"}), 400  
    return jsonify(one_member), 200 


#POST for add a new member on the Jackson's family
@app.route('/member', methods=['POST'])
def add_member():
    new_member = request.json  
    jackson_family.add_member(new_member) 
    return jsonify({"done": True, "msg": "Your new family member has been added successfully"}), 200 

#DELETW for remove a member on the Jackson's family
@app.route('/member/<int:id>', methods=['DELETE'])
def delete_member(id):
    delete_member = jackson_family.delete_member(id) 
    if not delete_member:
        return jsonify({"done": True, "msg":"It has been successfully removed"}), 200

#PUT for update members ID
@app.route('/member/<int:member_id>', methods=['PUT'])
def update_member(member_id):
    new_member = request.json  
    update_member = jackson_family.update_member(member_id, new_member)  
    if not update_member:
        return jsonify({"done": False, "msg":"Error"}), 400 
    return jsonify({"done": True, "msg":"it has been updated"}), 200 

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
