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

    def forward(self, x):
        v1 = torch.nn.functional.conv2d(x, torch.randn(16, 16, 1, 1))
        v2 = torch.nn.functional.conv2d(x, torch.randn(16, 16, 1, 1))
        v3 = (v1 + v2)
        v4 = (x + v3)
        v5 = torch.relu(v1)
        v6 = torch.nn.functional.conv2d(x, torch.randn(16, 16, 1, 1))
        v7 = (v6 + x)
        v8 = torch.nn.functional.conv2d(x, torch.randn(16, 16, 1, 1))
        v9 = (v7 + v8)
        v10 = torch.sigmoid(v10)
        return v9




func = Model().to('cuda')



x = torch.randn(1, 16, 64, 64)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Input type (torch.cuda.FloatTensor) and weight type (torch.FloatTensor) should be the same

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpw38gidcy/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpw38gidcy', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpw38gidcy/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''