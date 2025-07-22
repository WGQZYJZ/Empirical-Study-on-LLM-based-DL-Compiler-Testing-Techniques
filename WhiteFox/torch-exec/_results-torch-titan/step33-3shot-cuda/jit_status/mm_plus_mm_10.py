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

    def forward(self, input1, input2, input3):
        t1 = torch.mm(input1, input1)
        t2 = torch.mm(input2, input3)
        x1 = (t1 + t2)
        t3 = torch.mm(input2, input3)
        x2 = (t1 + t3)
        t4 = torch.mm(torch.relu(input1), torch.relu(input2))
        t5 = torch.mm(input2, torch.tanh(input3))
        x3 = (t4 + t5)
        return ((x1 + x2) + x3)




func = Model().to('cuda')



input1 = torch.randn(5, 5, requires_grad=True)



input2 = torch.randn(5, 5, requires_grad=True)



input3 = torch.randn(5, 5, requires_grad=True)


test_inputs = [input1, input2, input3]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp8hzjclvu/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp8hzjclvu', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp8hzjclvu/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''