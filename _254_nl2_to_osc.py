"""Small example OSC server

This program listens to several addresses, 
and creates an Open Sound Control Server to forward all telemetry
values of No Limits 2. 


Launch NoLimits 2 with the "--telemetry --telemetryport=15151" option, then execute.
"""

# For the case that nl2telemetry has not been added to PYTHONPATH
import pathlib
import sys
import time

sys.path.append(str(pathlib.Path(__file__).absolute().parent.parent))

from pprint import pprint

from nl2telemetry import NoLimits2
from nl2telemetry.message import get_telemetry, Answer
import argparse

from pythonosc import udp_client

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip", default="127.0.0.1",
      help="The ip of the OSC server")
  parser.add_argument("--port", type=int, default=8000,
      help="The port the OSC server is listening on")
  args = parser.parse_args()

  client = udp_client.SimpleUDPClient(args.ip, args.port)

  with NoLimits2() as nl2:
    while True:
      nl2.send(get_telemetry)
      data = Answer.get_data(nl2.receive())
      # pprint(data.__dict__)
      if data is not None:
        client.send_message("/braking", data.braking)
        client.send_message("/coaster_style_id", data.coaster_style_id)
        client.send_message("/current_car", data.current_car)
        client.send_message("/current_coaster", data.current_coaster)
        client.send_message("/current_seat", data.current_seat)
        client.send_message("/current_train", data.current_train)
        client.send_message("/gforce_x", data.gforce_x)
        client.send_message("/gforce_y", data.gforce_y)
        client.send_message("/gforce_z", data.gforce_z)
        client.send_message("/in_play_mode", data.in_play_mode)
        client.send_message("/paused_state", data.paused_state)
        client.send_message("/position_x", data.position_x)
        client.send_message("/position_y", data.position_y)
        client.send_message("/position_z", data.position_z)
        client.send_message("/rendered_frame", data.rendered_frame)
        client.send_message("/rotation_quaternion_w", data.rotation_quaternion_w)
        client.send_message("/rotation_quaternion_x", data.rotation_quaternion_x)
        client.send_message("/rotation_quaternion_y", data.rotation_quaternion_y)
        client.send_message("/rotation_quaternion_z", data.rotation_quaternion_z)
        client.send_message("/speed", data.speed)
        client.send_message("/view_mode", data.view_mode)
        time.sleep(0.01)