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

    def forward(self, input1, input2, input3, input4, input5, input6, input7):
        t1 = input1.clone()
        t1[(1, 1)] = 3.1415926
        t2 = torch.mm(input2, t1)
        t7 = torch.mm(input3, input4)
        t8 = torch.mm(input5, input6)
        t9 = (t2 + t7)
        t10 = (t8 + t9)
        t12 = torch.mm(input7, input4)
        t13 = torch.mm(input6, input3)
        t14 = (t12 + t13)
        t15 = (t10 + t14)
        return t15




func = Model().to('cuda')



input1 = (torch.randn(7, 7) + 1).clamp(0, 1)



input2 = (torch.randn(7, 7) + 1).clamp(0, 1)



input3 = (torch.randn(7, 7) + 1).clamp(0, 1)



input4 = (torch.randn(7, 7) + 1).clamp(0, 1)



input5 = (torch.randn(7, 7) + 1).clamp(0, 1)



input6 = (torch.randn(7, 7) + 1).clamp(0, 1)



input7 = (torch.randn(7, 7) + 1).clamp(0, 1)


test_inputs = [input1, input2, input3, input4, input5, input6, input7]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp5lltinh6/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp5lltinh6', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp5lltinh6/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''