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

    def forward(self, x1, x2, x3):
        b = {}
        a = {}
        c = {}
        b['dtype'] = torch.float32
        b['layout'] = torch.strided
        b['device'] = torch.device('cuda:0')
        a['dtype'] = torch.float64
        a['layout'] = torch.strided
        a['device'] = torch.device('cuda:0')
        c['dtype'] = torch.float64
        c['layout'] = torch.strided
        c['device'] = torch.device('cuda:0')
        a['dtype_to'] = torch.float32
        a['dtype_from'] = torch.float64
        b['dtype_to'] = torch.float32
        b['dtype_from'] = torch.float64
        c['dtype_to'] = torch.float32
        c['dtype_from'] = torch.float64
        t1 = x1.to(dtype=b['dtype'])
        t2 = torch.full([4096, 4096], 1, dtype=c['dtype'], layout=c['layout'], device=c['device'], pin_memory=False)
        t3 = torch.full([4096, 4096], 1, dtype=c['dtype'], layout=c['layout'], device=c['device'], pin_memory=False)
        t1 = t2.to(dtype=c['dtype'])
        t1 = (t3 - t2)
        t1 = t1.to(dtype=b['dtype'])
        return t1




func = Model().to('cuda')



x1 = torch.randn(4096, 4096, device='cuda:0')



x2 = torch.randn(4096, 4096, device='cuda:0')



x3 = torch.randn(4096, 4096, device='cuda:0')


test_inputs = [x1, x2, x3]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp3hl2g1v1/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp3hl2g1v1', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp3hl2g1v1/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''