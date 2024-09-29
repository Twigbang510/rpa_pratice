# Chapter 7: Pattern Matching with Regular Expressions
import re 

# 1. Finding Patterns in Text with `re.search()`
def find_phone_number(text):
    phone_number_pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
    mo = phone_number_pattern.search(text)
    if mo:
        print(f"Phone number found: {mo.group()}")  # Output: Phone number found: 415-555-4242
        return mo.group()
    return None

# 2. Grouping with Parentheses
def find_phone_number_groups(text):
    phone_number_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
    mo = phone_number_pattern.search(text)
    if mo:
        print(f"Area code: {mo.group(1)}")  # Output: Area code: 415
        print(f"Main number: {mo.group(2)}-{mo.group(3)}")  # Output: Main number: 555-4242
        return mo.groups()
    return None

# 3. Matching Multiple Groups with the Pipe (`|`)
def match_hero(text):
    hero_pattern = re.compile(r'Batman|Superman')
    mo = hero_pattern.search(text)
    if mo:
        print(mo.group())  # Output: Batman
        return mo.group()
    return None

# 4. Optional Matching with the Question Mark (`?`)
def match_batman_optional(text):
    bat_pattern = re.compile(r'Bat(wo)?man')
    mo = bat_pattern.search(text)
    if mo:
        print(mo.group())  # Output: Batman or Batwoman
        return mo.group()
    return None

# 5. Matching Zero or More with the Asterisk (`*`)
def match_batman_zero_or_more(text):
    bat_pattern = re.compile(r'Bat(wo)*man')
    mo = bat_pattern.search(text)
    if mo:
        print(mo.group())  # Output: Batman or Batwowowoman
        return mo.group()
    return None

# 6. Matching One or More with the Plus (`+`)
def match_batman_one_or_more(text):
    bat_pattern = re.compile(r'Bat(wo)+man')
    mo = bat_pattern.search(text)
    if mo:
        print(mo.group())  # Output: Batwoman or Batwowoman
        return mo.group()
    return None

# 7. Matching Specific Repetitions with Braces (`{}`)
def match_repetitions(text):
    ha_pattern = re.compile(r'(Ha){3}')
    mo = ha_pattern.search(text)
    if mo:
        print(mo.group())  # Output: HaHaHa
        return mo.group()
    return None

# 8. `findall()` Method
def find_all_phone_numbers(text):
    phone_number_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
    phone_numbers = phone_number_pattern.findall(text)
    print(phone_numbers)  # Output: [('415', '555', '1234'), ('212', '555', '0000')]
    return phone_numbers

# 9. Character Classes
def find_vowels(text):
    vowel_pattern = re.compile(r'[aeiouAEIOU]')
    vowels = vowel_pattern.findall(text)
    print(vowels)  # Output: ['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']
    return vowels

# 10. Making Your Own Character Classes
def find_consonants(text):
    consonant_pattern = re.compile(r'[^aeiouAEIOU]')
    consonants = consonant_pattern.findall(text)
    print(consonants)  # Output: List of non-vowel characters
    return consonants

# 11. The `^` and `$` Anchors
def check_start_end(text):
    begins_with_hello = re.compile(r'^Hello')
    ends_with_number = re.compile(r'\d$')
    start_match = begins_with_hello.search(text)
    end_match = ends_with_number.search(text)
    print(start_match)  # Output: Match object 
    print(end_match)  # Output: None
    return start_match, end_match

# 12. The Wildcard Character (`.`)
def match_wildcard(text):
    wildcard_pattern = re.compile(r'.at')
    matches = wildcard_pattern.findall(text)
    print(matches)  # Output: ['cat', 'hat', 'sat', 'lat', 'mat']
    return matches

# 13. Case-Insensitive Matching
def case_insensitive_search(text):
    case_insensitive_pattern = re.compile(r'robocop', re.I)
    mo = case_insensitive_pattern.search(text)
    if mo:
        print(mo.group())  # Output: RoboCop
        return mo.group()
    return None

# 14. Substituting Strings with `sub()`
def substitute_names(text):
    names_pattern = re.compile(r'Agent \w+')
    censored_text = names_pattern.sub('REDACTED', text)
    print(censored_text)  # Output: REDACTED gave the documents to REDACTED.
    return censored_text

# 15. Practice Project: Phone Number and Email Extractor
def extract_contact_info(text):
    phone_regex = re.compile(r'\d{3}-\d{3}-\d{4}|\d{4}-\d{3}-\d{3}')
    email_regex = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
    phone_numbers = phone_regex.findall(text)
    emails = email_regex.findall(text)
    print(f"Phone Numbers: {phone_numbers}")  
    print(f"Emails: {emails}")  
    return phone_numbers, emails
