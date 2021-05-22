import gpxpy
import gpxpy.gpx
import xml.etree.cElementTree as ET
import argparse
import os


parser = argparse.ArgumentParser(description='Convert a GPX to KML for using in Route Viewer in Bangle.js (smartwatch).')
parser.add_argument("-f", "--file", type=str,help="gpx file to be converted", required=True)
args = parser.parse_args()

gpx_file = open(args.file, 'r')
gpx = gpxpy.parse(gpx_file)

coordinates = ""

for track in gpx.tracks:
    for segment in track.segments:
        for point in segment.points:
            coordinates+="{},{} ".format(point.latitude,point.longitude)

#Export xml
root = ET.Element("kml")
ET.SubElement(root, "coordinates").text=coordinates
tree = ET.ElementTree(root)
tree.write(os.path.splitext(args.file)[0]+'.kml')