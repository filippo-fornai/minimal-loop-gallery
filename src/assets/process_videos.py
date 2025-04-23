# This script processes video files in the loopSrc folder, renames them, creates a preview and GIF, and organizes them into a structured output folder.

import os
import subprocess
import json
import shutil
import zipfile

script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_directory)
print(f"Changed current working directory to: {os.getcwd()}")

source_folder = "loopSrc"
base_output_name = "0"
counter = 0
sub_folder_name = "sections_media"
output_root_folder = "loops"
ffmpeg_path = "ffmpeg"  # Make sure ffmpeg is in your system's PATH
blender_output_folder = "../../public/blender_files" # Changed output folder name

if not os.path.exists(source_folder):
    print(f"Error: Source folder '{source_folder}' not found in '{os.getcwd()}'.")
    exit()

os.makedirs(output_root_folder, exist_ok=True)  # Create the 'loops' folder if it doesn't exist in the script's directory
os.makedirs(blender_output_folder, exist_ok=True) # Create the blender output folder if it doesn't exist

# if os.path.exists("../../public/blender_files/"):
#     print("Removing existing blender_files directory...")
#     shutil.rmtree("../../public/blender_files/")
#     os.makedirs("../../public/blender_files/")

for original_filename in os.listdir(source_folder):
    if original_filename.endswith(".mp4"):

        original_input_path = os.path.join(source_folder, original_filename)
        original_blender_path = os.path.join(source_folder, original_filename.replace(".mp4", ".blend"))
        folder_name = os.path.splitext(original_filename)[0]  # Use the original filename (without extension) as the output folder name
        output_folder_path = os.path.join(output_root_folder, folder_name)
        sections_media_path = os.path.join(output_folder_path, sub_folder_name)
        renamed_output_path = os.path.join(output_folder_path, f"{base_output_name}.mp4")

        preview_output_path = os.path.join(output_folder_path, f"{base_output_name}-preview.mp4")
        gif_output_path = os.path.join(output_folder_path, f"{base_output_name}.gif")
        zipped_blender_path = os.path.join(blender_output_folder, original_filename.replace(".mp4", ".zip"))

        os.makedirs(output_folder_path, exist_ok=True)
        os.makedirs(sections_media_path, exist_ok=True)  # Create the sections_media subfolder
        print(f"Created folder: {output_folder_path} and {sections_media_path}")

        counter += 1  # Increment the counter for each processed file

        # Move and rename the original file
        try:
            if os.path.exists(renamed_output_path):
                os.remove(renamed_output_path)
            shutil.move(original_input_path, renamed_output_path)

            # Create a zip archive of the Blender file
            if os.path.exists(original_blender_path):
                with zipfile.ZipFile(zipped_blender_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                    zipf.write(original_blender_path, os.path.basename(original_blender_path))
                print(f"Zipped '{os.path.basename(original_blender_path)}' to '{os.path.basename(zipped_blender_path)}'")
                os.remove(original_blender_path) # Optionally remove the original .blend file
            else:
                print(f"Warning: Blender file '{original_blender_path}' not found.")

            print(f"Moved and renamed '{original_filename}' to '{base_output_name}.mp4' in '{output_folder_path}'")
        except Exception as e:
            print(f"Error moving and renaming '{original_filename}': {e}")
            continue  # Skip to the next file if renaming fails

        ffmpeg_preview_cmd = [
            ffmpeg_path,
            "-n",  # Add the no-overwrite option
            # "-y",  # Add the overwrite option
            "-i", renamed_output_path,
            "-vf", "scale=960:-1",
            preview_output_path
        ]

        print(f"Running command: {' '.join(ffmpeg_preview_cmd)}")
        subprocess.run(ffmpeg_preview_cmd, check=False)
        if os.path.exists(preview_output_path):
            print(f"Created preview: {preview_output_path}")
        else:
            print(f"Error creating preview for {renamed_output_path}.")

        ffmpeg_gif_cmd = [
            ffmpeg_path,
            "-n",  # Add the no-overwrite option
            # "-y",  # Add the overwrite option
            "-i", renamed_output_path,
            gif_output_path
        ]

        print(f"Running command: {' '.join(ffmpeg_gif_cmd)}")
        # subprocess.run(ffmpeg_gif_cmd, check=False)
        # if os.path.exists(gif_output_path):
        #     print(f"Created GIF: {gif_output_path}")
        # else:
        #     print(f"Error creating GIF for {renamed_output_path}.")


with open('loops/counter.json', 'r') as json_file:
    data = json.load(json_file)
    print(f"Current counter value: {data['counter']}")
    data['counter'] = counter  # Update the counter in the JSON data
    with open('loops/counter.json', 'w') as file:
        json.dump(data, file, indent=4)  # Save the updated JSON data back to the file

print("Processing from loopSrc complete.")