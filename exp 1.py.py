import re
text = "Python is powerful. Python is easy to learn."
search_result = re.search("Python", text)
print("Search result:", search_result.group())
match_result = re.match("Python", text)
print("Match result:", match_result.group())
findall_result = re.findall("Python", text)
print("Find all result:", findall_result)
replaced_text = re.sub("Python", "JAVA", text)
print("Replaced text:", replaced_text)
