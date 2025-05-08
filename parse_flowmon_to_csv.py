import xml.etree.ElementTree as ET
import csv
import sys

if len(sys.argv) != 3:
    print("Usage: python3 parse_flowmon_to_csv.py input.xml output.csv")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

tree = ET.parse(input_file)
root = tree.getroot()

# 获取 flowId → 地址映射
flow_id_to_addr = {}
for flow in root.findall(".//Flow"):
    fid = flow.attrib.get("flowId")
    src = flow.attrib.get("sourceAddress")
    dst = flow.attrib.get("destinationAddress")
    if fid:
        flow_id_to_addr[fid] = (src, dst)

with open(output_file, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['FlowId', 'Src', 'Dst', 'Bytes', 'Packets'])
    writer.writeheader()

    for flow in root.findall(".//FlowStats"):
        fid = flow.attrib.get("flowId")
        bytes_received = int(flow.attrib.get("bytes", 0))
        packets = int(flow.attrib.get("packets", 0))

        src, dst = flow_id_to_addr.get(fid, ("?", "?"))

        writer.writerow({
            'FlowId': fid,
            'Src': src,
            'Dst': dst,
            'Bytes': bytes_received,
            'Packets': packets
        })
