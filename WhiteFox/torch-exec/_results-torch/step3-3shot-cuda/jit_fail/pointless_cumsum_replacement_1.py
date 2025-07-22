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
        b = {}
        a = {}
        a['size'] = torch.Size([1024, 256])
        a['dtype'] = torch.float16
        a['layout'] = torch.strided
        a['device'] = torch.device('cuda:0')
        b['size'] = torch.Size([1024, 256])
        b['dtype'] = torch.float16
        b['layout'] = torch.strided
        b['device'] = torch.device('cuda:0')
        t1 = torch.randn(a['size'], dtype=a['dtype'], layout=a['layout'], device=a['device'])
        t2 = t1.to(dtype=b['dtype'], size=b['size'], layout=b['layout'], device=b['device'])
        t3 = torch.full(2, 1, dtype=t1.dtype, layout=t1.layout, device=t1.device, pin_memory=False)
        t4 = torch.cumsum(t3, 0)
        return t4



func = Model().to('cuda')



x1 = torch.randn(1024, 256, dtype=torch.float16, device='cuda:0')

test_inputs = [x1]

# JIT_FAIL
'''
direct:
to() received an invalid combination of arguments - got (device=torch.device, layout=torch.layout, size=torch.Size, dtype=torch.dtype, ), but expected one of:
 * (torch.device device = None, torch.dtype dtype = None, bool non_blocking = False, bool copy = False, *, torch.memory_format memory_format = None)
 * (torch.dtype dtype, bool non_blocking = False, bool copy = False, *, torch.memory_format memory_format = None)
 * (Tensor tensor, bool non_blocking = False, bool copy = False, *, torch.memory_format memory_format = None)


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmphn2byo84/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmphn2byo84/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmphn2byo84', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''