#!/bin/bash
# RZY TRACKER - Simple IP Lookup

GREEN="\e[32m"
RED="\e[31m"
YELLOW="\e[33m"
RESET="\e[0m"
BOLD="\e[1m"

clear
echo -e "${RED}"
echo "  ____  _______     _______        _   _   "
echo " |  _ \| ____\ \   / / ____|      | | | |  "
echo " | |_) |  _|  \ \ / /|  _|    ____| |_| |  "
echo " |  _ <| |___  \ V / | |___  |____|  _  |  "
echo " |_| \_\_____|  \_/  |_____|      |_| |_|  "
echo -e "${RESET}"

echo -e "${YELLOW}-------------------------------------------------------------${RESET}"
echo -e "                     ${BOLD}IP Information${RESET}"
echo -e "${YELLOW}-------------------------------------------------------------${RESET}"

read -p "Enter IP Address: " ip

if [ -z "$ip" ]; then
    echo -e "${RED}[!] No IP entered!${RESET}"
    exit 1
fi

# API request
response=$(curl -s "http://ip-api.com/json/$ip")

# Check if response is empty
if [ -z "$response" ]; then
    echo -e "${RED}[!] No response from API!${RESET}"
    exit 1
fi

# Extract fields
ip_address=$(echo $response | grep -oP '(?<="query":")[^"]*')
country=$(echo $response | grep -oP '(?<="country":")[^"]*')
country_code=$(echo $response | grep -oP '(?<="countryCode":")[^"]*')
region=$(echo $response | grep -oP '(?<="regionName":")[^"]*')
city=$(echo $response | grep -oP '(?<="city":")[^"]*')
zip=$(echo $response | grep -oP '(?<="zip":")[^"]*')
timezone=$(echo $response | grep -oP '(?<="timezone":")[^"]*')
isp=$(echo $response | grep -oP '(?<="isp":")[^"]*')
org=$(echo $response | grep -oP '(?<="org":")[^"]*')
asn=$(echo $response | grep -oP '(?<="as":")[^"]*')
lat=$(echo $response | grep -oP '(?<="lat":)[^,]*')
lon=$(echo $response | grep -oP '(?<="lon":)[^,]*')

date_now=$(date +"%B %d, %Y, %I:%M %p")

# Print
echo -e "${YELLOW}IP Address     ${RESET}> ${GREEN}$ip_address${RESET}"
echo -e "${YELLOW}Country code   ${RESET}> ${GREEN}$country_code${RESET}"
echo -e "${YELLOW}Country        ${RESET}> ${GREEN}$country${RESET}"
echo -e "${YELLOW}Date & Time    ${RESET}> ${GREEN}$date_now${RESET}"
echo -e "${YELLOW}Region         ${RESET}> ${GREEN}$region${RESET}"
echo -e "${YELLOW}City           ${RESET}> ${GREEN}$city${RESET}"
echo -e "${YELLOW}Zip code       ${RESET}> ${GREEN}$zip${RESET}"
echo -e "${YELLOW}Time zone      ${RESET}> ${GREEN}$timezone${RESET}"
echo -e "${YELLOW}ISP            ${RESET}> ${GREEN}$isp${RESET}"
echo -e "${YELLOW}Organization   ${RESET}> ${GREEN}$org${RESET}"
echo -e "${YELLOW}ASN            ${RESET}> ${GREEN}$asn${RESET}"
echo -e "${YELLOW}Latitude       ${RESET}> ${GREEN}$lat${RESET}"
echo -e "${YELLOW}Longitude      ${RESET}> ${GREEN}$lon${RESET}"
echo -e "${YELLOW}Location       ${RESET}> ${GREEN}$lat,$lon${RESET}"

echo -e "${YELLOW}-------------------------------------------------------------${RESET}"