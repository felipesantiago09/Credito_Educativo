from flask import Flask, request, jsonify, url_for
from flask import render_template 

import sys
sys.path.append( "src" )


from view.web import vista_credito 

app = Flask(__name__)

app.register_blueprint( vista_credito.blueprint )

if __name__ == '__main__':
    app.run( debug=True )
