from google.cloud import storage
import xml.etree.ElementTree as etree
import re
import os.path

def print_sample_info(blob):
    if blob.name.endswith(".metadata.xml") and not blob.name.endswith(".run.metadata.xml"):
        lines = blob.download_as_string()
        a = etree.fromstring(lines)

        info = {'desc': None, 'set': None, 'name': None, 'ccs': None, 'xml': f'gs://broad-gp-pacbio/{blob.name}'}
        for e in a.iter():
            tag = re.sub(r"{.+}", "", e.tag)
            tag = re.sub("-", "_", tag)

            if tag == 'Run' and 'Description' in e.attrib:
                info['desc'] = e.attrib['Description']
            elif tag == 'SubreadSet' and 'Name' in e.attrib:
                info['set'] = e.attrib['Name']
            elif tag == 'WellSample' and 'Name' in e.attrib:
                info['name'] = e.attrib['Name']
            elif tag == 'IsCCS':
                info['ccs'] = e.text

        print(f'{info["name"]}\t{info["ccs"]}\t{os.path.dirname(info["xml"])}\t{info["desc"]}')

    elif blob.name.endswith("final_summary.txt"):
        info = {}
        md = {}

        lines = blob.download_as_string().decode("utf-8").split('\n')
        for l in lines:
            if "=" in l:
                (k, v) = l.split('=')
                md[k] = v

        info['run_id'] = md['protocol_run_id']
        info['center'] = "BI"
        info['date'] = md['started']
        info['project'] = md['protocol_group_id']
        info['platform'] = "ONT"
        info['instrument'] = md['instrument']
        info['flowcell'] = md['flow_cell_id']
        info['slot'] = md['position']
        info['sample'] = md['sample_id']

        print(f'{info["sample"]}\tfalse\tgs://broad-gp-oxfordnano/{blob.name}\t{info["flowcell"]}')


storage_client = storage.Client()

for bucket in ['broad-gp-pacbio', 'broad-gp-oxfordnano', 'broad-dsde-methods-long-reads-deepseq']:
    blobs = storage_client.list_blobs(bucket, prefix='')

    for blob in blobs:
        print_sample_info(blob)
