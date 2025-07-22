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
        self.conv2 = torch.nn.Conv2d(16, 8, 16, stride=16)

    def forward(self, x1):
        v1 = self.conv2(x1)
        v1_0 = (0.0001 + v1)
        v1_1 = ((- 0.0001) + v1_0)
        v1_2 = ((- 0.0001) + v1_1)
        v2 = ((- 0.0001) + v1_2)
        v3 = (3.14 + v2)
        v4 = (v3 - 3.14)
        v5 = (v4 + 3.14)
        v6 = (v5 + v5)
        v7 = (v6 - (2 * v4))
        v8 = (v7 / 2)
        v9 = v8.div(3)
        v10 = ((- 0.1) + v9)
        v11 = v10.clamp(min=0, max=6)
        v12 = (v11 / 6)
        return v12




func = Model().to('cuda')



x1 = torch.randn(15, 16, 128, 128)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpva10uxvh/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpva10uxvh', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpva10uxvh/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''