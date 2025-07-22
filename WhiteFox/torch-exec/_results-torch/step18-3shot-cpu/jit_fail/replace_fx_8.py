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
        super(model, self).__init__()
        self.a = torch.rand(5)
        self.b = torch.rand(5)

    def forward(self, input):
        y1 = torch.rand_like(input)
        y3 = torch.add(input, y1)
        y2 = torch.dropout(self.a)
        y4 = torch.rand_like(input)
        y = torch.add(y3, y4)
        return y



func = model().to('cpu')


input1 = torch.zeros(5)

test_inputs = [input1]

# JIT_FAIL
'''
direct:
dropout() missing 2 required positional argument: "p", "train"

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpbu6x1ah3/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpbu6x1ah3/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpbu6x1ah3', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''