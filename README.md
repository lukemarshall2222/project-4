# UOCIS322 - Project 4 

The purpose of this project is to implement an algorithm that acts as a brevet control time calculator. A web page is implemented with HTML, AJAX, and a Flask server to create an interface with the calculator.

# Brevets Time Calculator

The algorithm calculates the open and close time for each control distance entered into the web page. The times are based on this distance, the overall distance of the entire brevet, and the start time of the brevet. Brevets can be 200, 400, 600, or 1000 kilometers in length and within each interval therin lies a maximum and minimum average speed that must be achieved by the rider for continuous riding and not being cut out of the brevet. The control time is calculated by using these interval average times and the intervals themselves, adding the amount of time that can or must be taken to complete each interval or portion of an interval to make a total time, and adding it to the start time of the brevet. The start control opens at start time and ends one hour thereafter. The end control timing is based on the length of the brevet, with the start time being based on the total distance whether it is exactly at that distance or slightly farther; and the close-time is based on specified timing for the end of the race, given by the organization.
