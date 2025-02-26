import os
import csv
import datetime
import time
import speedtest

def check_connectivity():
    """Checks the connectivity to return true boolean when internet is up by pinging google's DNS"""
    host_IP = "8.8.8.8"  # This is google's public DNS
    system_response = os.system(f"ping -n 1 {host_IP} >nul")
    return system_response == 0

def speed_test():
    """Runs a speedtest to measure the upload and download time"""
    st = speedtest.Speedtest()  # Creating a speed test object
    st.get_best_server()
    download_speed = st.download() / 1_000_000  # Shows result in mbps
    upload_speed = st.upload() / 1_000_000
    print(f"Download Speed: {download_speed:.2f} mbps")
    print(f"Upload Speed: {upload_speed:.2f} mbps")
    timestamp = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")  # Current time

    print(f"[{timestamp}] Download: {download_speed:.2f} mbps | Upload: {upload_speed:.2f} mbps")

    # Save results to a CSV file
    with open("test_results.csv", "a", newline="") as file:
        writer = csv.writer(file)
        # If file is empty, write header first
        if file.tell() == 0:
            writer.writerow(["timestamp", "download_speed", "upload_speed"])
        writer.writerow([timestamp, download_speed, upload_speed])

def continuous_testing(interval=60):
    """Runs a speed test at predetermined intervals"""
    try:
        while True:
            speed_test()
            print(f"Waiting {interval} seconds before next test..\n")
            time.sleep(interval)  # Pauses for a predetermined duration
    except KeyboardInterrupt:
        print("\nSpeed test stopped by user. Exiting gracefully...")

def set_csv():
    """Creates CSV file with headers if it doesn't exist"""
    with open("test_results.csv", "a+", newline="") as file:
        writer = csv.writer(file)
        # If file is empty, write header first
        file.seek(0)
        if file.read(1) == "":  # If file is empty, write header
            writer.writerow(["timestamp", "download_speed", "upload_speed"])

if __name__ == "__main__":
    set_csv()  # Ensure CSV file is set up correctly
    interval = int(input("Enter time interval in seconds: "))
    continuous_testing(interval)