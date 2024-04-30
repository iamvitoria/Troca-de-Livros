from flask import Flask, render_template
import pyshark
import asyncio

def extract_ips_from_pcapng(file_path):
    ips = []
    asyncio.set_event_loop(asyncio.new_event_loop())  # Definindo uma nova política de evento
    cap = pyshark.FileCapture(file_path)
    for packet in cap:
        try:
            ip_src = packet.ip.src
            ip_dst = packet.ip.dst
            if ip_src not in ips:
                ips.append(ip_src)
            if ip_dst not in ips:
                ips.append(ip_dst)
        except AttributeError:
            # Ignore packets that don't have IP addresses
            pass
    return ips


app = Flask(__name__)

def extract_ips_from_pcapng(file_path):
    ips = []
    cap = pyshark.FileCapture(file_path)
    for packet in cap:
        try:
            ip_src = packet.ip.src
            ip_dst = packet.ip.dst
            if ip_src not in ips:
                ips.append(ip_src)
            if ip_dst not in ips:
                ips.append(ip_dst)
        except AttributeError:
            # Ignore packets that don't have IP addresses
            pass
    return ips

@app.route('/')
def index():
    # Substitua 'caminho/para/arquivo.pcapng' pelo caminho do seu arquivo .pcapng
    ips = extract_ips_from_pcapng('caminho/para/arquivo.pcapng')

    return render_template('index.html', ips=ips)

if __name__ == '__main__':
    app.run(debug=True, port=5001)

