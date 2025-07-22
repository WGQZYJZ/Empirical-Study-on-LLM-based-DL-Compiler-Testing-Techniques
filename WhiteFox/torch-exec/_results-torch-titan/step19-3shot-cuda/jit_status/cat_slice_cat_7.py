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

    def forward(self, input_list):
        x1 = input_list[0]
        x2 = (x1 + 1)
        x3 = (x1 * 0.7071067811865476)
        x4 = torch.erf(x3)
        x5 = (x4 * 0.8412536529812128)
        x6 = (x2 * x5)
        x7 = (x1 + 1)
        x8 = (0.7071067811865476 * x7)
        x9 = torch.erf(x8)
        x10 = (0.8412536529812128 * x9)
        y0 = 1.0
        return [x6, x10]



func = Model().to('cuda')



x1 = torch.randn(1, 1000)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp77wpawrw/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp77wpawrw', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp77wpawrw/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''