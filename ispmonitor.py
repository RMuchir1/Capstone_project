# Creating a network monitor using python
import os
import csv
import datetime
import time
import speedtest

def check_connectivity():
    """Checks the connectivity to return true boolean when internet is up by pinging google's DNS"""
    host_IP = "8.8.8.8" # This is google's public DNS
    system_responce = os.system(f"ping -n 1 {host_IP} >nul")
    return system_responce == 0

if __name__ == "__main__":
    internet_status = check_connectivity()
    print("internet is up") if internet_status else print ("internet is down")

def speed_test():
    """runs a speedtest to measure the upload and download time"""
    st = speedtest.Speedtest() #creating a speed test object
    st.get_best_server()
    download_speed = st.download() / 1_000_000 # shows result in mbps
    upload_speed = st.upload() / 1_000_000
    print (f"Download Speed: {download_speed: .2f} mbps")
    print (f"Upload Speed: {upload_speed: .2f} mbps")
    timestamp = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") #current time

    print (f"[{timestamp}] Download: {download_speed: .2f} mbps | {upload_speed: .2f} mbps")

    # save results to a csv file
    with open("test_results.csv", "a", newline="") as file:
        writer = csv.writer(file)
        # if file is empty, write header first
        if not file.read(0):
                writer.writerow(["timestamp", "download_speed", "upload_speed"]) 

    

def continous_testing(interval = 60):
    """runs a speed test at predetermined intervals"""
    try:
        while True:
            speed_test() 
            print(f"waiting {interval} seconds before next test..\n")
            time.sleep(interval) # pauses for a predetermined duration
    except KeyboardInterrupt:
        print("\n Speed test stopped by user. Exitting gracefully...")

def set_csv():
    """creates CSV file with headers if it doesn't exist"""
    
    with open("test_results.csv", "a+", newline="") as file:
            writer = csv.writer(file)

            # if file is empty, write header first
            file.seek(0)
            if file.read(1) == "": #if file is empty, write header
                writer.writerow(["timestamp", "download_speed", "upload_speed"]) 
writer.writerow(timestamp, download_speed, upload_speed]) 

if __name__ == "__main__":
    interval = int(input("Enter time interval in seconds"))
    continous_testing(interval)








