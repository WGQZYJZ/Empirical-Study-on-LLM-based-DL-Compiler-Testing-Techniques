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

    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        v2 = torch.mm(x1, x2)
        return torch.cat(x1, x2, v1, v2)



func = Model().to('cpu')


x1 = torch.randn(1, 6)

x2 = torch.randn(6, 1)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
cat() received an invalid combination of arguments - got (Tensor, Tensor, Tensor, Tensor), but expected one of:
 * (tuple of Tensors tensors, int dim = 0, *, Tensor out = None)
      didn't match because some of the arguments have invalid types: (!Tensor!, !Tensor!, !Tensor!, !Tensor!)
 * (tuple of Tensors tensors, name dim, *, Tensor out = None)
      didn't match because some of the arguments have invalid types: (!Tensor!, !Tensor!, !Tensor!, !Tensor!)


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpkphtn532/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpkphtn532/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpkphtn532', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''