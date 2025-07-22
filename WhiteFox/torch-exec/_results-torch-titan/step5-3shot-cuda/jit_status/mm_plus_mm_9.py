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

    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(16, 16)
        self.linear2 = torch.nn.Linear(16, 16)

    def forward(self, input1, input2, input3, input4):
        t1 = self.linear1(input1)
        t2 = self.linear1(input2)
        t3 = self.linear2(input3)
        t4 = self.linear1(input4)
        return (((t1 + t2) + t3) + t4)



func = Model().to('cuda')



input1 = torch.randn(16, 16)



input2 = torch.randn(16, 16)



input3 = torch.randn(16, 16)



input4 = torch.randn(16, 16)


test_inputs = [input1, input2, input3, input4]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpc9ouegyp/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpc9ouegyp', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpc9ouegyp/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''