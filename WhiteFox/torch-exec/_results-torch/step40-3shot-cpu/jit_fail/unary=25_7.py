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
        self.linear = torch.nn.Linear(3, 8, bias=False)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1.detach().numpy().reshape(-1)
        v3 = v2 > 0
        v4 = v2 * 0.1
        v5 = torch.where(v3, v2, v4)
        v6 = torch.from_numpy(v5.reshape(v1.shape)).to(torch.float32)
        return v6


func = Model().to('cpu')


x1 = torch.randn(1, 3)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
where() received an invalid combination of arguments - got (numpy.ndarray, numpy.ndarray, numpy.ndarray), but expected one of:
 * (Tensor condition)
 * (Tensor condition, Tensor input, Tensor other, *, Tensor out = None)
 * (Tensor condition, Number self, Tensor other)
      didn't match because some of the arguments have invalid types: (!numpy.ndarray!, !numpy.ndarray!, !numpy.ndarray!)
 * (Tensor condition, Tensor input, Number other)
      didn't match because some of the arguments have invalid types: (!numpy.ndarray!, !numpy.ndarray!, !numpy.ndarray!)
 * (Tensor condition, Number self, Number other)
      didn't match because some of the arguments have invalid types: (!numpy.ndarray!, !numpy.ndarray!, !numpy.ndarray!)


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpwe1fa_gy/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpwe1fa_gy/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpwe1fa_gy', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''