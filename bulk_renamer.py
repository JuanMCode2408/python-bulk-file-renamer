import os

folder_path = input("Enter folder path: ")
base_name = input("Enter new base name (e.g. file): ")

counter = 1

for filename in os.listdir(folder_path):

    file_path = os.path.join(folder_path, filename)

    if os.path.isfile(file_path):

        extension = os.path.splitext(filename)[1]

        new_name = f"{base_name}_{counter}{extension}"
        new_path = os.path.join(folder_path, new_name)

        # evitar sobreescritura
        while os.path.exists(new_path):
            counter += 1
            new_name = f"{base_name}_{counter}{extension}"
            new_path = os.path.join(folder_path, new_name)

        os.rename(file_path, new_path)

        print(f"Renamed: {filename} → {new_name}")

        counter += 1

print("Renaming completed!")