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

    def forward(self, input1, input2):
        t1 = torch.mm(input1, input2)
        t2 = torch.cat([t1, t1], 1)
        t3 = torch.cat([t2, t2], 1)
        t4 = torch.cat([t3, t3], 1)
        t5 = torch.cat([t4, t4], 1)
        t6 = torch.cat([t5, t5], 1)
        t7 = torch.cat([t6, t6], 1)
        t8 = torch.cat([t7, t7], 1)
        t9 = torch.cat([t8, t8], 1)
        return torch.cat([t9, t9], 1)




func = Model().to('cuda')



input1 = torch.randn(32, 8)



input2 = torch.randn(8, 32)


test_inputs = [input1, input2]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp37oxf0no/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp37oxf0no', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp37oxf0no/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''