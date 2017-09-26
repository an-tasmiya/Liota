import time
import math
import pint
from liota.dcc_comms.socket_comms import SocketDccComms
from liota.entities.metrics.metric import Metric
from liota.entities.edge_systems.dell5k_edge_system import Dell5KEdgeSystem
from liota.device_comms.mqtt_device_comms import MqttDeviceComms
from liota.dcc_comms.socket_comms import SocketDccComms
from custom_socket_dcc import CustomSocketDcc
import csv

i=-1


with open('data.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=';')
    for row in plots:
	arr = row[0].split(',')#send this arr to datacenter

def on_message(client, data, msg):
    m = msg.payload
    print(m)

def send_output():
    # Also works with string or integer
    print 'sending output'
    #my_bytes = bytearray()
    global i
    i=i+1
    #my_bytes.append(123)
    return arr[i]

# getting values from conf file
config = {}
execfile('sampleProp.conf', config)

if __name__ == '__main__':
    # Device to gateway subscription
    #mqtt = MqttDeviceComms(url = "test.mosquitto.org", port = 1883, clean_session=True,conn_disconn_timeout=1000)
    print('Connection to broker established...')
    #mqtt.subscribe("random_data", callback = on_message, qos = 2)
    print('Subscribed to random_data')
    # Edge system object
    sdcc = CustomSocketDcc(SocketDccComms(ip = config["SocketIP"], port = config["SocketPort"]))
    edge_system = Dell5KEdgeSystem(config['EdgeSystemName'])
    reg_edge_system = sdcc.register(edge_system)
    # Edge system to DCC connection
    print(config["SocketIP"], config["SocketPort"])
    metric_name = "model.output"
    metric = Metric(
        name = metric_name,
        interval = 5,
        sampling_function = send_output
    )
    reg_metric = sdcc.register(metric)
    sdcc.create_relationship(reg_edge_system, reg_metric)
    reg_metric.start_collecting()
