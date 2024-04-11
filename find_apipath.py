import os  
import re  
  
# 假设您已经从文件读取了folder变量  
# read a var from text  
with open('/tmp/.api_var', 'r') as f:  
    folder = f.read().strip()  
  
# Define regular expressions  
relist = {  
    "apipath": "\"[/|]api.*?/.*?[/|]\"",  
    "Linkfinder": "(?:\"|')(((?:[a-zA-Z]{1,10}://|//)[^\"'/]{1,}\.[a-zA-Z]{2,}[^\"']{0,})|((?:/|\.\./|\./)[^\"'><,;|*()(%%$^/\\\[\]][^\"'><,;|()]{1,})|([a-zA-Z0-9_\-/]{1,}/[a-zA-Z0-9_\-/]{1,}\.(?:[a-zA-Z]{1,4}|action)(?:[\?|#][^\"|']{0,}|))|([a-zA-Z0-9_\-/]{1,}/[a-zA-Z0-9_\-/]{3,}(?:[\?|#][^\"|']{0,}|))|([a-zA-Z0-9_\-]{1,}\.(?:\w)(?:[\?|#][^\"|']{0,}|)))(?:\"|')",  
}  
  
# Enumerate JS files  
def get_js_files(rootDir):  
    js_files = []  
    for root, _, files in os.walk(rootDir):  
        for file in files:  
            if file.endswith(".js"):  
                js_files.append(os.path.join(root, file))  
    return js_files  
  
# Search for keywords in JS files using regular expressions  
def search_keywords(js_files):  
    search_data = {key: [] for key in relist}  
    for js in js_files:  
        with open(js, "r", encoding="utf-8") as f:  
            txt = f.read()  
            for key, value in relist.items():  
                search_data[key].extend(re.findall(value, txt))  
    return search_data  
  
# Print results directly  
def main():  
    # 直接使用folder变量  
    js_files = get_js_files(folder)  
    search_data = search_keywords(js_files)  
    for key in search_data:  
        print("===" * 5, key, "===" * 5)  
        for match in search_data[key]:  
            if isinstance(match, tuple):  
                for item in match:  
                    print(str(item).strip("\""))  
            else:  
                print(str(match).strip("\""))  
  
if __name__ == "__main__":  
    main()
