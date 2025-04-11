import matplotlib
matplotlib.rcParams['font.family']='AppleGothic'
import matplotlib.pyplot as plt

word_dict = {}


with open('/Users/linyixuan/Downloads/hw2_data.txt', 'r', encoding='utf-8') as file:
    for line in file:
        word = line.strip().lower()
        if word in word_dict:
            word_dict[word] += 1 
        else:
            word_dict[word] = 1


print(f"總共有 {len(word_dict)} 個不重複的英文字")


print("\n每個英文字的出現次數：")
for word, count in word_dict.items():
    print(f"{word}: {count}")


sorted_items = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)


labels = [item[0] for item in sorted_items]
counts = [item[1] for item in sorted_items]


plt.figure(figsize=(12, 6))
plt.bar(labels, counts)
plt.xticks(rotation=90)
plt.xlabel('英文字')
plt.ylabel('出現次數')
plt.title('各英文字出現次數直方圖')
plt.tight_layout()
plt.show()