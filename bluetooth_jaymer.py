"""
=============================================================
  BLUETOOTH JAYMER - INFINITE VOID DOMAIN EXPANSION
  Created by: Sandeep Patra
  Instagram: @devloper_sandeep
=============================================================
"""

import math
import sys
import time
import threading
import os
import subprocess

ACTIVE_THREADS = []

def ensure_bluetooth_on():
    """Automatically turns on Bluetooth interface if it's off."""
    animated_spinner("Checking and enabling Bluetooth adapter...", duration=1.5)
    try:
        subprocess.call("sv up bluetooth > /dev/null 2>&1", shell=True)
        subprocess.call("hciconfig hci0 up > /dev/null 2>&1", shell=True)
        subprocess.call("rfkill unblock bluetooth > /dev/null 2>&1", shell=True)
        rainbow_line("[+] Bluetooth interface powered ON automatically.", 10)
    except Exception as e:
        rainbow_line(f"[!] Unable to auto-toggle Bluetooth: {e}", 10)

def rainbow_line(text: str, step: int, freq: float = 0.15):
    """Outputs text with dynamic lolcat rainbow colors."""
    for char_idx, char in enumerate(text):
        pos = (step + char_idx) * freq
        r = int((math.sin(pos + 0) * 127) + 128)
        g = int((math.sin(pos + 2 * math.pi / 3) * 127) + 128)
        b = int((math.sin(pos + 4 * math.pi / 3) * 127) + 128)
        sys.stdout.write(f"\033[38;2;{r};{g};{b}m{char}")
    sys.stdout.write("\033[0m\n")
    sys.stdout.flush()

def animated_spinner(text: str, duration: float = 1.0):
    """Displays a smooth spinning loading animation in rainbow colors."""
    chars = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        frame = chars[i % len(chars)]
        sys.stdout.write(f"\r\033[38;2;150;200;255m{frame} {text}\033[0m")
        sys.stdout.flush()
        time.sleep(0.04)
        i += 1
    sys.stdout.write("\r" + " " * (len(text) + 6) + "\r")
    sys.stdout.flush()

def expand_domain():
    """Plays a large 3D hand sign and domain expansion sequence."""
    large_hand_sign = [
        "                         .-----------------.                         ",
        "                        /  .----.     .----.  \\                        ",
        "                       /  /      \\   /      \\  \\                       ",
        "                      |  |   ( ✌ ) | |   ( ✌ )  |  |                      ",
        "                       \\  \\      /   \\      /  /                       ",
        "                        \\  '----'     '----'  /                        ",
        "                         '-----------------'                         ",
        "                              ||       ||                            ",
        "                             /  \\     /  \\                           ",
        "                            /    \\   /    \\                          ",
        "                           (      \\ /      )                         ",
        "                            \\      |      /                          ",
        "                             '-----v-----'                           "
    ]

    print("\n")
    rainbow_line(">>> WEAVING THE LARGE 3D HAND SIGN... <<<", 0)
    time.sleep(0.1)

    for idx, line in enumerate(large_hand_sign):
        rainbow_line(line, idx * 2)
        time.sleep(0.03)

    print()
    rainbow_line("     🌌 DOMAIN EXPANSION: BLUETOOTH JAYMER 🌌", 20)
    time.sleep(0.3)

    expansion_frames = [
        "                 . . : : ★ : : . .                 ",
        "             . : * * * * * * * * * : .             ",
        "         . : * * * * * * * * * * * * * : .         ",
        "     . : * * * * INFINITE VOID * * * * : .         ",
        "  <===============================================> "
    ]

    rainbow_line("\n>>> SEE DOMAIN EXPANDING... <<<", 30)
    for step, ring in enumerate(expansion_frames):
        rainbow_line(ring, step * 4)
        time.sleep(0.05)

    for _ in range(3):
        sys.stdout.write("\033[A\033[A")
        rainbow_line("  <~~~~~~~~~~~~~ [ DOMAIN EXPANDING ] ~~~~~~~~~~~~~> ", 40)
        time.sleep(0.06)
        sys.stdout.write("\033[A")
        rainbow_line("  <===============================================> ", 30)
        time.sleep(0.06)

    print("\n")

def scan_devices():
    animated_spinner("Scanning for Bluetooth devices...", duration=2.0)
    try:
        result = subprocess.check_output("hcitool scan", shell=True).decode()
        devices = []
        for line in result.splitlines()[1:]:
            parts = line.strip().split("\t")
            if len(parts) == 2:
                addr, name = parts
                devices.append((addr.strip(), name.strip()))
        return devices
    except Exception as e:
        rainbow_line(f"[!] Scan failed or bluetooth unavailable: {e}", 15)
        return []

def ping_target(mac, name):
    rainbow_line(f"[+] Engaging target stream on {name} ({mac})...", 20)
    try:
        subprocess.call(f"l2ping -i hci0 -s 600 -f {mac}", shell=True)
    except KeyboardInterrupt:
        rainbow_line(f"[-] Connection to {mac} stopped.", 25)
    except Exception as e:
        rainbow_line(f"[!] Error on {mac}: {e}", 25)

def start_ping(mac, name):
    t = threading.Thread(target=ping_target, args=(mac, name))
    t.daemon = True
    t.start()
    ACTIVE_THREADS.append(t)

def main():
    if os.name == 'posix':
        os.system("clear")
    else:
        os.system("cls")

    expand_domain()
    ensure_bluetooth_on()

    devices = scan_devices()
    target_mac = None
    target_name = "jaym"

    if devices:
        rainbow_line(f"\n[*] Scan complete. Total devices found: {len(devices)}", 35)
        for addr, name in devices:
            if "jaym" in name.lower():
                target_mac = addr
                target_name = name
                break
        
        if not target_mac:
            target_mac, target_name = devices[0]
            rainbow_line(f"[*] 'jaym' not matched explicitly. Auto-selecting first device: {target_name}", 38)
    else:
        rainbow_line("\n[!] No Bluetooth devices found via automatic scan.", 30)
        rainbow_line("[*] Please enter target details manually:", 32)
        target_mac = input("    Enter MAC Address (e.g. XX:XX:XX:XX:XX:XX): ").strip()
        target_name = input("    Enter Target Name [jaym]: ").strip() or "jaym"

    if target_mac:
        rainbow_line(f"[+] Target locked: {target_name} ({target_mac})", 42)
        animated_spinner(f"Synchronizing Bluetooth Jaymer with {target_name}...", duration=1.0)
        
        start_ping(target_mac, target_name)
        rainbow_line(f"\n[*] Active Bluetooth Jaymer stream running on {target_name}. Press CTRL+C to stop.\n", 50)
        
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print()
            rainbow_line(f"\n[!] Bluetooth Jaymer domain collapsed by user.", 50)
    else:
        rainbow_line("[!] Invalid target MAC. Exiting...", 50)

if __name__ == "__main__":
    main()
