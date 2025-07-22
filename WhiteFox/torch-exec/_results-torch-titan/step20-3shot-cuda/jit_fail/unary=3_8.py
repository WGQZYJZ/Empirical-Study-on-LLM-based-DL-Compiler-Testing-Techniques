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
        v1 = (torch.conv2d(input=x1, weight=torch.nn.Parameter(torch.ones(5, 3, 3, 3)), bias=None, stride=(2, 2), padding=(0, 0), dilation=1, groups=1) * 0.5)
        v2 = (torch.conv2d(input=x1, weight=torch.nn.Parameter(torch.ones(5, 3, 3, 3)), bias=None, stride=(2, 2), padding=(0, 0), dilation=1, groups=1) * 0.7071067811865476)
        v3 = torch.erf(input=v2)
        v4 = (v3 + 1)
        v5 = (v1 * v4)
        return v5




func = Model().to('cuda')



x1 = torch.randn(1, 3, 28, 28)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Input type (torch.cuda.FloatTensor) and weight type (torch.FloatTensor) should be the same

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpvua_1ku3/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpvua_1ku3', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpvua_1ku3/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''