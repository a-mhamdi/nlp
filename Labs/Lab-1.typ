#import "Class.typ": *

#show: ieee.with(
  title: [#text(smallcaps("Lab #1: Regular Expressions in Python and grep"))],

  abstract: [
    This lab introduces regular expressions in Python and the grep command. You will learn how to use regular expressions to search for patterns in text and how to use grep to search for patterns in files. By the end, you will be able to use regular expressions and grep to search for patterns in text and files.
  ],

  authors:
  (
    (
      name: "Abdelbacet Mhamdi",
      department: [Senior-lecturer, Dept. of EE],
      organization: [ISET Bizerte --- Tunisia],
      profile: "a-mhamdi",
    ),

    /*
    (
      name: "Student 1",
      department: [Dept. of EE],
      organization: [ISET Bizerte --- Tunisia],
      profile: "abc",
    ),
    (
      name: "Student 2",
      department: [Dept. of EE],
      organization: [ISET Bizerte --- Tunisia],
      profile: "abc",
    ),
  */

  )
  // index-terms: (""),
  // bibliography-file: "Biblio.bib",
)

= Introduction
*Regular expressions* _(regex)_ are a powerful and widely used tool for pattern matching and text processing. They are essential in many domains such as data cleaning, log analysis, web scraping, cybersecurity, and natural language processing. In Python, regex is supported through the built-in re module, which provides flexible and efficient functions for searching, matching, extracting, and transforming text.

At the end of this lab, you should be able to:
  - Understand the basic syntax and structure of regular expressions
  - Use Python’s re module to search, match, and extract patterns from text
  - Validate structured data such as emails, phone numbers, and dates using regex
  - Perform text substitution and cleaning operations
  - Apply regex concepts using the grep command in a Linux terminal
  - Develop confidence in using regex for practical data processing tasks

#colbreak()

= Exercises

#exo[Basic pattern matching][Using Python and the re module, write a script that reads sample.txt and prints all email addresses found in the file.]

#exo[Structured data extraction][Write a Python script that identifies and prints all IPv4 addresses from the file.]

#exo[Substitution and Data Masking][Using re.sub(), replace:
  + All phone numbers with [PHONE_HIDDEN]
  + All credit card numbers with [CARD_HIDDEN]
The modified text should then be printed or saved into a new file named masked.txt.]

#exo[Searching with grep][Using the Linux terminal, apply grep to find all lines that contain dates in MM/DD/YYYY or in YYYY-MM-DD format.]

#exo[Advanced grep usage][Identify and analyze phone numbers in the file.
  + Use grep to display all lines containing US phone numbers.
  + Use grep -c to count how many phone numbers appear.
  + Use grep -o to print only the phone numbers, not the full lines.]

#colbreak()

#exo[Log file analysis][You're a system administrator investigating suspicious activity on a web server. You've been given a log file (server.log) containing thousands of entries. Your task is to extract specific patterns and identify potential security issues.
  + Find all log entries with exactly 403 status codes (Forbidden).
  + Find all lines containing valid IPv4 addresses that start with 192.168. Note: Focus on the standard format (no leading zeros like 192.168.001.050).
  + Extract all entries that occurred between 08:25:00 and 08:30:00 (inclusive).
  + Find all POST requests to /login that resulted in a 401 status AND have an attempts parameter with a value of 4 or higher.
  + Identify lines where the request path contains two or more consecutive dots (..) which might indicate directory traversal attacks.
  + Find all requests that took longer than 1 second to process (response time >= 1.000s). The time format is always X.XXXs.
  + Find POST or DELETE requests to /api/\* endpoints that resulted in either 500 or 204 status codes AND took more than 0.3 seconds.
]
