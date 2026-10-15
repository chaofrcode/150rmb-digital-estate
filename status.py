#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
150 RMB Digital Real Estate - Traffic & Status Automator
Author: Chao Wang (@Chaolzyy)
Description: Parses vnStat network traffic statistics and outputs a lightweight state.json 
             for Caddy HTTPS static distribution.
"""

import subprocess
import json
import datetime

def get_vnstat_data():
    """Execute vnstat json command to get network interface traffic stats."""
    try:
        # Assuming interface is eth0, matching our architectural diagram
        result = subprocess.run(['vnstat', '-i', 'eth0', '--json'], 
                                capture_output=True, text=True, check=True)
        return json.loads(result.stdout)
    except Exception as e:
        print(f"Error fetching vnstat data: {e}")
        return None

def generate_state_json():
    data = get_vnstat_data()
    if not data:
        return
    
    state_info = {
        "project": "150RMB Digital Real Estate",
        "author": "Chao Wang (@Chaolzyy)",
        "interface": "eth0",
        "status": "online",
        "security": "VLESS + REALITY + ML-KEM-768",
        "last_updated": datetime.datetime.utcnow().isoformat() + "Z",
        "note": "Configured with Caddy automatic HTTPS distribution."
    }
    
    with open('state.json', 'w', encoding='utf-8') as f:
        json.dump(state_info, f, indent=4, ensure_ascii=False)
    print("Successfully generated state.json!")

if __name__ == "__main__":
    generate_state_json()
