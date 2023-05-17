## PASO Nro 1
pip3 install pyserial

## PASO Nro 2
vincularse con el modulo bluetooth HC.05
contraseña: 1234
Buscar el puerto de bluetooth COM4                      ##anotar el puerto que opte el bluetooth
## PASO Nro 3 instalar un Entorno virtual

pip install virtualenv
cd Desktop \Robotica+Python+Arduino                      ##ubicacion donde se creara el entorno virtual
virtualenv Py_Arduino                                    ##nombre del entorno virtual
.\Py_Arduino\Scripts\activate                            ##activar el entorno virtual

pip freeze                                               ##para ver las librerias o paquetes instalados

## PASO Nro4 Cómo correr un programa usando entornos virtuales en python
cd Desktop \Robotica+Python+Arduino
.\Py_Arduino\Scripts\activate
python py+Arduino.py

.\Py_Arduino\Scripts\deactivate 