f1 = eval(open('mfcc_files/Testing Dataset/host5_mfcc.txt.out').read().strip())
f2 = eval(open('mfcc_files/Testing Dataset/host5_mfcc.txt.out2').read().strip())
count = 0
for i in range(len(f1)):
	if(f1[i]==2):
		if(f2[i]==0):
			count+=1
print float(count)/len(f2)*100