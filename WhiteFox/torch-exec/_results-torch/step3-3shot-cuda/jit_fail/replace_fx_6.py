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
        self.dropout = torch.nn.Dropout(0.8)
        z1 = self.dropout(x1)
        t1 = torch.rand_like(z1)
        h1 = z1 * t1
        j1 = torch.nn.functional.upsample_nearest(h1, size=32)
        k1 = torch.nn.functional.softmax(j1, dim=-1)
        l1 = torch.nn.functional.batch_norm(h1, track_running_stats=True)
        m1 = torch.nn.functional.pad(k1, (1, 1, 1, 1, 1, 2))
        return torch.nn.functional.max_pool1d(m1, kernel_size=2, stride=1, padding=1)



func = Model().to('cuda')


x1 = torch.randn(10, 16, 16)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
batch_norm() got an unexpected keyword argument 'track_running_stats'

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpoqtia464/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpoqtia464/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpoqtia464', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''