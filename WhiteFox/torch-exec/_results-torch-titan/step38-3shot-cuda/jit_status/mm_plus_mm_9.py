import os
import torch
import torch.nn.functional as F
import torch.nn as nn
import numpy as np
from torch.autograd import Variable
import math
import torch as th
import torch.linalg as la
from torch.nn import Parameter
import torch.linalg as linalg



class Model(torch.nn.Module):

    def forward(self, input1, input2, input3, input4, input5, input6, input7, input8):
        t1 = torch.mm(input1, input2)
        t2 = torch.mm(input3, input4)
        t3 = (t1 + t2)
        t4 = torch.mm(input5, input6)
        t5 = torch.mm(input7, input8)
        t6 = (t4 + t5)
        return (t3 + t6)




func = Model().to('cuda')



input1 = torch.randn(6, 6)



input2 = torch.randn(6, 6)



input3 = torch.randn(6, 6)



input4 = torch.randn(6, 6)



input5 = torch.randn(6, 6)



input6 = torch.randn(6, 6)



input7 = torch.randn(6, 6)



input8 = torch.randn(6, 6)


test_inputs = [input1, input2, input3, input4, input5, input6, input7, input8]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpq9ucm8j4/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpq9ucm8j4', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpq9ucm8j4/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''