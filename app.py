from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/test')
def test():
    return jsonify({"message": "Aqui veras los servicios de BRECOMPERU"})

from services import services

@app.route('/services')
def getServices():
    return jsonify({"Services": services, "Contenido": "Lista de Servicios BRECOMPERU"})

@app.route('/services/<string:service_name>')
def getService(service_name):
    serviceFound = [service for service in services if service['name'] == service_name]
    if (len(serviceFound) > 0):
        return jsonify({"Service": serviceFound[0]})
    return jsonify({"Message": "Servicio no encontrado"})

@app.route('/services', methods=['POST'])
def addService():
    new_service = {
        "name": request.json['name'],
        "description": request.json['description']
    }
    services.append(new_service)
    return jsonify({"message": "Producto agregado", "services": services})

@app.route('/services/<string:service_name>', methods =['PUT'])
def updateService(service_name):
    serviceFound = [service for service in services if service['name'] == service_name]
    if (len(serviceFound) > 0):
        serviceFound[0]['name'] = request.json['name']
        serviceFound[0]['description'] = request.json['description']
        return jsonify({"message": "Servicio actualizado", "service": serviceFound[0]})
    return jsonify({"Message": "Servicio no encontrado"})




if __name__ == '__main__':
    app.run(debug=True, port=4000)