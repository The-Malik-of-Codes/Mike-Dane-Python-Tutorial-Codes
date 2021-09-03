monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "sep": "september",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions["Dec"])
print(monthConversions["Oct"])
print(monthConversions.get("Jan"))
print(monthConversions.get("Love"))
print(monthConversions.get("Love", "Not a valid key"))