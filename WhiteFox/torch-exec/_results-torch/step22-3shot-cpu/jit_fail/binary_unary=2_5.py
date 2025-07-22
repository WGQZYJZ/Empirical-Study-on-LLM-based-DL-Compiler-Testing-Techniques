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
        self.conv2 = torch.nn.Conv2d(4, 1, 2, stride=1)

    def forward(self, x1):
        v1 = torch.transpose(x1, 2, 3)
        v2 = x1.size()
        v3 = v2[2]
        v4 = x1.size()
        v5 = v4[3]
        v6 = torch.add(v3, -v5)
        v7 = torch.div(v6, 2)
        v8 = v2[3]
        v9 = torch.div(v8, 2)
        v10 = torch.zeros(1, 1, v7, v9, dtype=torch.float)
        v11 = torch.add(v1, v10)
        v12 = self.conv2(v10)
        v13 = torch.transpose(v11, 2, 3)
        v14 = torch.squeeze(v12, 0)
        v15 = torch.squeeze(v13, 0)
        v16 = torch.add(v15, v14)
        return v16



func = Model().to('cpu')


x1 = torch.randn(1, 4, 10, 10)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
zeros(): argument 'size' failed to unpack the object at pos 3 with error "type must be tuple of ints,but got Tensor"

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmplkl9bssk/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmplkl9bssk/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmplkl9bssk', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''