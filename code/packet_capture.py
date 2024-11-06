import pyshark
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

def analyze_pcap(pcap_file):
    data = []
    capture = pyshark.FileCapture(pcap_file)
    for packet in capture:
        try:
            if 'IP' in packet:
                src_ip = packet.ip.src
                dst_ip = packet.ip.dst
                packet_length = int(packet.length)
                protocol = packet.transport_layer 

                data.append({
                    'Source IP': src_ip,
                    'Destination IP': dst_ip,
                    'Length': packet_length,
                    'Protocol': protocol
                })
        except AttributeError:   
            pass

    df = pd.DataFrame(data)
    analyze_top_communicating_ips(df)
    analyze_protocol_distribution(df)

def analyze_top_communicating_ips(df):
    ip_counter = Counter(df['Source IP'].tolist() + df['Destination IP'].tolist())
    top_communicating_ips = pd.DataFrame(ip_counter.most_common(10), columns=['IP', 'Count'])

    plt.figure(figsize=(10, 6))
    plt.bar(top_communicating_ips['IP'], top_communicating_ips['Count'])
    plt.title("Top 10 Communicating IPs")
    plt.xlabel("IP Address")
    plt.ylabel("Packet Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def analyze_protocol_distribution(df):
    protocol_distribution = df['Protocol'].value_counts()
    plt.figure(figsize=(10, 6))
    protocol_distribution.plot(kind='bar')
    plt.title("Traffic by Protocol")
    plt.xlabel("Protocol")
    plt.ylabel("Packet Count")
    plt.tight_layout()
    plt.show()

pcap_file = "PCAP.pcap"
analyze_pcap(pcap_file)

