import yaml
import os

# Boilerplate is so annoying to write :3

def process_data(data):
    # Swap Y with Z, and negate Y for the new Z value
    modified_data = []
    for entry in data:
        # Ignore entries with BoneID 255, 1, 2, 3
        if entry['BoneID'] in [255, 1, 2, 3]:
            continue
        # Skip localscale
        if entry['TrackType'] == 'localscale':
            continue

        # Skip localposition
        if entry['TrackType'] == 'localposition':
            continue

        # Check if BoneID is 8, 12, or 115 and set the localrotation and adjust
        if entry['BoneID'] in [8, 12, 115] and entry['TrackType'] == 'localrotation':
            entry['data'] = {
                'W': 1,
                'X': 0,
                'Y': 0,
                'Z': 0
            }

        # Check if BoneID is 16 or 20 and apply specific transformations
        if entry['BoneID'] in [16, 20] and entry['TrackType'] == 'localrotation':
            x = entry['data']['X']
            y = entry['data']['Y']
            z = entry['data']['Z']
            w = entry['data']['W']

            entry['data'] = {
                'W': -y,
                'X': z,
                'Y': w,
                'Z': -x
            }

        
        # Extract X, Y, Z, W values
        x = entry['data']['X']
        y = entry['data']['Y']
        z = entry['data']['Z']
        w = entry['data']['W']

        # Add other values
        modified_entry = {
            'Frame': entry['Frame'],
            'BoneID': entry['BoneID'],
            'TrackType': entry['TrackType'],
            'data': entry['data']
        }
        
        modified_data.append(modified_entry)
    
    return modified_data


def read_and_process_yml(input_file_path, output_file_path):
    base_name = os.path.splitext(os.path.basename(input_file_path))[0]

    # Some preamble to skip the first 6 lines so python doesnt scream at me :VVVVV
    with open(input_file_path, 'r') as file:
        lines = file.readlines()
    
    yaml_content = ''.join(lines[6:])
    
    # Parse the YAML data
    data = yaml.safe_load(yaml_content)
    
    # Find the maximum Frame value for the tags
    max_frame = max(entry['Frame'] for entry in data)

    modified_data = process_data(data)

    # Write the header and modified data to a new YAML file
    with open(output_file_path, 'w') as file:
        # Writing the header and shit
        file.write("!LMTM3AEntry\n")
        file.write("version: 1\n")
        file.write(f"Name: AnimationID{base_name}\n")
        file.write(f"FrameCount: {max_frame}\n") 
        file.write("LoopFrame: -1\n")
        file.write("KeyFrames:\n")
        
        # Write the modified data
        for entry in modified_data:
            file.write(f"  - Frame: {entry['Frame']}\n")
            file.write(f"    TrackType: {entry['TrackType']}\n")
            file.write(f"    BoneID: {entry['BoneID']}\n")
            file.write("    data:\n")
            file.write(f"      X: {entry['data']['X']}\n")
            file.write(f"      Y: {entry['data']['Y']}\n")
            file.write(f"      Z: {entry['data']['Z']}\n")
            file.write(f"      W: {entry['data']['W']}\n")

if __name__ == "__main__":
    input_file_path = "C:\\Users\\hadif\\Desktop\\Spencer Anims\\Spencer_l0\\1.yml"    # Path to the original YAML file
    output_file_path = "C:\\Users\\hadif\\Desktop\\Spencer Anims\\Spencer_l0\\1suck.yml" # Path to save the new YAML file
    read_and_process_yml(input_file_path, output_file_path)
