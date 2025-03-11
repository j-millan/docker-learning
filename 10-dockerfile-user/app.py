from flask import Flask, render_template
import os
import pwd
import grp

app = Flask(__name__)

@app.route('/')
def home():
    # Get the current user ID and name
    user_id = os.getuid()
    username = pwd.getpwuid(user_id).pw_name

    # Get the current group ID and name
    group_id = os.getgid()
    group_name = grp.getgrgid(group_id).gr_name
    
    # Return a text response displaying the user and the group
    return f'Hello from user: {username} (UID: {user_id}) and group {group_name} (GID: {group_id})'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)