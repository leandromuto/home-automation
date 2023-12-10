# This file is executed on every boot (including wake-boot from deepsleep)

import network
import webrepl

LAN_SSID = ""
LAN_PASS = ""
PORT = 8266  # ESP32 default port


def _activate_wlan():
    wlan = network.WLAN(network.STA_IF)

    try:
        wlan.active(True)
        return wlan
    except Exception as err:
        print(f"Couldn't activate WLAN. {type(err).__name__} error: {err}")


def connect():
    wlan = _activate_wlan()
    networks = wlan.scan()

    if len(networks) == 0:
        print("No networks found.")

    wlan.connect(LAN_SSID, LAN_PASS)
    print("Successfully connected") if wlan.isconnected() else print(
        "Something went wrong. Try to connect again."
    )


connect()
webrepl.start()
