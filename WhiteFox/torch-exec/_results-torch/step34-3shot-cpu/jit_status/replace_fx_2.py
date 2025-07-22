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

class model(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, x):
        b1 = torch.nn.functional.dropout(x)
        b2 = torch.nn.functional.dropout(x, p=0.4)
        b3 = torch.nn.functional.dropout(x, p=0.5)
        b4 = torch.nn.functional.dropout(x, p=0.2)
        b5 = torch.nn.functional.dropout(x, inplace=True)
        b6 = torch.nn.functional.dropout(x, p=0.4, inplace=True)
        b7 = torch.nn.functional.dropout(x, p=0.5, inplace=True)
        b8 = torch.nn.functional.dropout(x, p=0.2, inplace=True)
        return 1



func = model().to('cpu')


x = torch.randn(1)

test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpxrzbcxno/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpxrzbcxno/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpxrzbcxno', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''