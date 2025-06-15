import threading
import requests  

def download_file(url, filename):
    print(f"Starting download: {filename}")
    response = requests.get(url)
    with open(filename, "wb") as f:
        f.write(response.content)
    print(f"Finished download: {filename}")

downloads = [
    ("https://upload.wikimedia.org/wikipedia/commons/6/6e/Golde33443.jpg", "dog.jpg"),
    ("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Beacon_Stawa_M%C5%82yny%2C_%C5%9Awinouj%C5%9Bcie.jpg/1280px-Beacon_Stawa_M%C5%82yny%2C_%C5%9Awinouj%C5%9Bcie.jpg", "Stawa Młyny.jpg")
]


t1 = threading.Thread(target=download_file, args=(downloads[0]))


t2 = threading.Thread(target=download_file,args=(downloads[1]))


t1.start()
t2.start()

t1.join()
t2.join()

print("All downloads completed.")




# CODE LOGIC

'''

1. We import 'threading' and 'requests':
   - 'threading' lets us run tasks in parallel.
   - 'requests' handles the HTTP GET calls to fetch each image.

2. We define a helper function 'download_file(url, filename)':
   - Prints a 'Starting download' message so we can see progress.
   - Uses 'requests.get(url)' to fetch the raw file bytes.
   - Opens (or creates) 'filename' in binary-write mode ('wb') and writes the bytes.
   - Prints a 'Finished download' confirmation once the file is saved.

3. We create a list called 'downloads':
   - Each entry is a 2-item tuple: (direct_image_url, destination_filename).
   - In this example we download a dog image and a lighthouse image.

4. We create two Thread objects manually (no loops):
   - 't1' handles the first tuple in 'downloads'.
   - 't2' handles the second tuple.
   - Each thread calls 'download_file' with its own (url, filename) pair via the 'args' parameter.

5. We start the threads:
   - 't1.start()' and 't2.start()' begin both downloads concurrently.

6. We wait for both to finish:
   - 't1.join()' pauses the main program until 't1' completes.
   - 't2.join()' does the same for the second thread.
   - This guarantees the program doesn't exit early.

7. After both joins return, we print 'All downloads completed.' to signal success.

8. Result:
   - Two image files ('dog.jpg' and 'Stawa Młyny.jpg') appear in the same directory as the script.
   - The downloads run in parallel, so total runtime is roughly the longest individual download instead of the sum of both.

'''
