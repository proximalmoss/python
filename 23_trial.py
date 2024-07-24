def remove_split(string,word):
    newstr=string.replace(word,"")
    return newstr.strip()
str="   HANAN IS GOOD   "
n=remove_split(str, "HANAN")
print(n)
#RETURNS LIST??? #I WROTE SPLIT IN PLACE OF SPLIT (ps corrected now)
def remove_split(string, word):
  newstr = string.replace(word, "").strip()  # Combine replace and strip
  return newstr

this = "  HANAN IS GOOD  "
n = remove_split(this, "HANAN")
print(n) 
