if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
    
    
    grades = sorted(set([score for name, score in records]))
    
    second_lowest = grades[1]
    
    second_lowest_std = sorted([name for name, score in records if score == second_lowest])
    
    for name in second_lowest_std:
        print(name)
