from entropy import password_entropy



def dictionary_attack(password):
    COMMON_PASSWORDS = [
        "password",
        "123456",
        "qwerty",
        "admin",
        "welcome",
        "1111111",
        "abc123",
    ]

    if password in COMMON_PASSWORDS:
        return "Very vulnerable"

    return "Not found"



def brute_force_attack(password):

    entropy = password_entropy(password)

    if entropy < 40:
        return "Very vulnerable to brute_force attack"
    elif entropy < 60:
        return "Moderately resistant"
    else:
        return "Good resistance"
        



def pattern_attack(password):

    password_lower = password.lower()

    YEARS = ["1950", "1951", "1952", "1953", "1954", "1955",
             "1956", "1957", "1958", "1959", "1960",
             "1961", "1962", "1963", "1964", "1965",
             "1966", "1967", "1968", "1969", "1970",
             "1971", "1972", "1973", "1974", "1975", 
             "1976", "1977", "1978", "1979", "1980", 
             "1981", "1982", "1983", "1984", "1985", 
             "1986", "1987", "1988", "1989", "1990", 
             "1991", "1992", "1993", "1994", "1995", 
             "1996", "1997", "1998", "1999", "2000",
             "2001", "2002", "2003", "2004", "2005", 
             "2006", "2007", "2008", "2009", "2010", 
             "2011", "2012", "2013", "2014", "2015", 
             "2016", "2017", "2018", "2019", "2020", 
             "2021", "2022", "2023", "2024", "2025", 
             "2026"]
    COMMON_NAMES= [
            "James", "John", "Robert", "Michael", "William",
            "David", "Richard", "Joseph", "Thomas", "Charles",
            "Christopher", "Daniel", "Matthew", "Anthony", "Mark",
            "Donald", "Steven", "Paul", "Andrew", "Joshua",
            "Kenneth", "Kevin", "Brian", "George", "Edward",
            "Ronald", "Timothy", "Jason", "Jeffrey", "Ryan",
            "Jacob", "Gary", "Nicholas", "Eric", "Jonathan",
            "Stephen", "Larry", "Justin", "Scott", "Brandon",
            "Benjamin", "Samuel", "Alexander", "Henry", "Jack",
            "Oliver", "Harry", "Noah", "Leo", "Oscar",

            "Admin", "qwerty", "user", "gamer", "player"

            "Mary", "Patricia", "Jennifer", "Linda", "Elizabeth",
            "Barbara", "Susan", "Jessica", "Sarah", "Karen",
            "Nancy", "Lisa", "Margaret", "Betty", "Sandra",
            "Ashley", "Kimberly", "Emily", "Donna", "Michelle",
            "Carol", "Amanda", "Dorothy", "Melissa", "Deborah",
            "Stephanie", "Rebecca", "Sharon", "Laura", "Cynthia",
            "Amy", "Angela", "Emma", "Olivia", "Charlotte",
            "Sophia", "Amelia", "Isla", "Grace", "Lily",
            "Ella", "Ava", "Mia", "Chloe", "Sophie",
            "Evie", "Lucy", "Ruby", "Rosie", "Hannah"
            ]
    
    if any(password.endswith(year) for year in YEARS):
        return "Common year pattern detected."
    
    if any(password_lower.startswith(name) for name in COMMON_NAMES):
        return "Common name pattern detected."
    elif any(password_lower.endswith(name) for name in COMMON_NAMES):
        return "Common name pattern detected."

    for name in COMMON_NAMES:
        for year in YEARS:
            if password_lower.startswith(name) and password.endswith(year):
                return "Name + year pattern detected."
            elif password.endswith(year) and password_lower.startswith(name):
                return "Year + name pattern detected."

    
    





def sequential_attack(password):






def repeated_attack(password):




def attack_report(password):