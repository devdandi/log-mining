# LOG-MINIG
![Capture](https://user-images.githubusercontent.com/45485349/130343653-2826476d-5502-4bff-b483-b5208abba2bc.JPG)


You can use this library to collecting log of application, this library support all application you just adding manualy directory location to the Gather.py file.

# USAGE

1. Clone Repository
2. Setting up the properties file in src/properties/here
3. Run Gather.py using command python3 src/Gather.py
4. Install Mosquitto
5. Open new terminal and run mosquitto_sub -h "app.host" -p "app.port" -t "app.topic"
6. Done
