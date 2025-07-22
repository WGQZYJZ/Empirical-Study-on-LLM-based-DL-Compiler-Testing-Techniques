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

    def forward(self, x1):
        b1 = {}
        a = {}
        b1['dtype'] = torch.float32
        b1['layout'] = torch.strided
        b1['device'] = torch.device('cpu')
        a['dtype'] = torch.float32
        a['layout'] = torch.strided
        a['device'] = torch.device('cpu')
        a['dtype_to'] = torch.float32
        a['dtype_from'] = torch.float32
        b1['dtype_to'] = torch.float32
        b1['dtype_from'] = torch.float32
        t1 = torch.full([256, 16], 1, dtype=b1['dtype'], layout=b1['layout'], device=b1['device'], pin_memory=False)
        t2 = torch.cat((torch.transpose(t1, 0, 1), torch.transpose(t1, 0, 1)), 0)
        t3 = t2.to(dtype=a['dtype'])
        t4 = torch.cumsum(t3, 0)
        return t4



func = Model().to('cpu')


x1 = torch.randn(256, 16, device='cpu')

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp2bdb9857/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp2bdb9857/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp2bdb9857', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''