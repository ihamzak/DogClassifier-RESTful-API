from flask import Flask,request
from flask_restful import Api,Resource
from .module.image_processing import predict_breed_transfer
from logging import FileHandler,WARNING

app = Flask(__name__)
api = Api(app)

# adding logger
filehandler = FileHandler('./Restful Api/error_logging/error.txt')
filehandler.setLevel(WARNING)
app.logger.addHandler(filehandler)

supportd_formats = [
    'image/jpeg',
    'image/jpg',
    'image/png'
]

class DogClassifier(Resource):

    def post(self):
        try:

            # checking photo if there is any picture provided or not
            if 'photos' in request.files:
                img = request.files['photos']
                format = img.mimetype

                # check for supported format
                if format in ['image/jpeg','image/jpg','image/png']:
                    breed = str(predict_breed_transfer(img))

                    response = { "message" : "success" , "response": { "breed":breed } , "status code" : 200 }
                    return response, 200

                response = {"message": "invalid img format.", "status code": 400}
                return response , 400

            else:
                response = {"message": "image not provided", "status code": 400}
                return response, 400

        except:
            response = {"message": "failure", "status code": 400 }
            return response, 400

api.add_resource(DogClassifier,'/dogclassifier')
app.run(host='0.0.0.0',port=5000)