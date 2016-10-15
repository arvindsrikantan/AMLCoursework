from myhmm_log import *

def fun(filename):
    f=open(filename,"r")
    li=f.read().split("\n")
    l=[li[i:i+9] for i in range(0,len(li)/10)]
    return l

model1 = MyHmmLog("debate_initial.txt")
model2 = MyHmmLog("debate_initial.txt")
model3 = MyHmmLog("debate_initial.txt")

model1.forward_backward_multi(fun("./VQFiles for Experiment-1/single_1_trg_vq.txt"))
model2.forward_backward_multi(fun("./VQFiles for Experiment-1/multi_1_trg_vq.txt"))
model3.forward_backward_multi(fun("./VQFiles for Experiment-1/silent_1_trg_vq.txt"))

#-------------- TEST -------------------#
obs = fun("./VQFiles for Experiment-1/c1_test_vq.txt")
