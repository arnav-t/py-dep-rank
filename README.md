# py-dep-rank
Get your department rank
## Installation
```sh
git clone https://github.com/arnav-t/py-dep-rank.git
cd py-dep-rank
sh install.sh
```
## Usage 
```sh
python3 main.py 
```
Now enter your roll number and wait for the results to load.     
The data will also be stored as a `.csv` file in the same directory.    
For example, if your roll number is '12CS10001' then the results will also be stored in `12CS1.csv`
### Throttling
The server will throttle your connection if you make a large number of requests within a short period of time. To overcome this, use WiFi instead of ethernet cable. If the script seems to be going much slower than before, just type this in a different terminal window:
```sh
sudo dhclient -v -r [wireless interface]
```
Where `[wireless interface]` is your default wireless interface (e.g `wlan0`). You can check your default wireless interface by typing:
```sh
iwconfig
```
Which will lead to an output similar to this:
```sh
enp3s0f1  no wireless extensions.

lo        no wireless extensions.

virbr0    no wireless extensions.

virbr0-nic  no wireless extensions.

wlp2s0    IEEE 802.11  ESSID:"STUDENT"  
          Mode:Managed  Frequency:2.437 GHz  Access Point: 58:AC:78:28:F0:30   
          Bit Rate=1 Mb/s   Tx-Power=20 dBm   
          Retry short limit:7   RTS thr:off   Fragment thr:off
          Power Management:on
          Link Quality=61/70  Signal level=-49 dBm  
          Rx invalid nwid:0  Rx invalid crypt:0  Rx invalid frag:0
          Tx excessive retries:0  Invalid misc:0   Missed beacon:0
```
Here, `wlp2s0` is the default wireless interface.