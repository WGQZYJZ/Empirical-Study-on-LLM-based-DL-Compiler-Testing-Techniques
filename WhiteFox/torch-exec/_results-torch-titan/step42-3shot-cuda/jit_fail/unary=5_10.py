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
        v1 = torch.transpose(x1, 1, 2).contiguous()
        v2 = torch.conv_transpose2d(v1, torch.zeros([32, 32, 4, 4], dtype=torch.float32), stride=[1, 1], padding=[0, 0], groups=32, bias=None)
        v3 = (v2 * 0.5)
        v4 = (v2 * 0.7071067811865476)
        v5 = torch.erf(v4)
        v6 = (v5 + 1)
        v7 = (v3 * v6)
        return v7




func = Model().to('cuda')



x1 = torch.randn(1, 16, 32, 32)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Input type (torch.cuda.FloatTensor) and weight type (torch.FloatTensor) should be the same

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp8vwcufh0/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp8vwcufh0', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp8vwcufh0/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''