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

    def forward(self, x11, x12, x13):
        v7 = torch.cat([x11, x12, x13], dim=1)
        v8 = v7[:, 0:9223372036854775807]
        v9 = v8[:, (- (v7.size(1) - 1)):]
        v10 = torch.cat([v7, v9], dim=1)
        return v10



func = Model().to('cuda')



x11 = torch.randn(1, 48, 1, 1)



x12 = torch.randn(1, 120, 1, 1)



x13 = torch.randn(1, 224, 1, 1)


test_inputs = [x11, x12, x13]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpooie14qu/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpooie14qu', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpooie14qu/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''