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

    def __init__(self, min_value=0, max_value=1):
        super().__init__()

    def forward(self, x1):
        v0 = x1 * 0.8959889827464012
        v1 = x1 + x1
        v2 = torch.mean(v1, dim=[-2, -1], keepdim=True)
        v3 = v1 / v2
        v4 = v3 * 0.3452390219632011
        v5 = torch.min(v4, torch.tensor(0.760402547351158, requires_grad=True), dim=[-2, -1], keepdim=True)
        v6 = torch.max(v5, torch.tensor(-0.42610920540287, requires_grad=True), dim=[-2, -1], keepdim=True)
        return v6


func = Model().to('cpu')


x1 = torch.randn(1, 3, 48, 48)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
min() received an invalid combination of arguments - got (Tensor, Tensor, keepdim=bool, dim=list), but expected one of:
 * (Tensor input, *, Tensor out = None)
 * (Tensor input, Tensor other, *, Tensor out = None)
      didn't match because some of the keywords were incorrect: keepdim, dim
 * (Tensor input, int dim, bool keepdim = False, *, tuple of Tensors out = None)
 * (Tensor input, name dim, bool keepdim = False, *, tuple of Tensors out = None)


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpdw1s8gdn/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpdw1s8gdn/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpdw1s8gdn', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''