#!/usr/bin/python3
import sys

inputFile = sys.argv[1]
outputFile = sys.argv[2]

genreCnt = {} #딕셔너리

with open(inputFile,"rt") as f:
    
    for line in f:
        movie_array = line.strip().split('::') #::기준으로 자르기 
        gen_arr = movie_array[2].strip().split("|") #장르 부분 | 나누기

        for genre in gen_arr:
            if genre in genreCnt:
                genreCnt[genre] +=1
            else:
                genreCnt[genre] =1
        # print(f"Processed line: {line.strip()}")

with open(outputFile,"wt") as output:
    for genre, count in genreCnt.items():
        output.write("%s %d\n" %(genre,count))