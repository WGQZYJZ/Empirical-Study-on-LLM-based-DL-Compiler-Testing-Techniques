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
        self.conv = torch.nn.Conv2d(3, 16, 4, stride=1)

    def forward(self, input_1):
        v1 = self.conv(input_1)
        v2 = (v1 - 260.39)
        v2 = (v2 - 1)
        v3 = (v2 - 0.5)
        v4 = (v3 - 228)
        v5 = (v4 - (- 0.54))
        v6 = (v5 - 0.9)
        v7 = (v6 - (- 0.377))
        v8 = (v7 - (- 0.78))
        v9 = (v8 - (- 1.23))
        v10 = (v9 - 0.3)
        return v7




func = Model().to('cuda')



input_1 = torch.randn(1, 3, 32, 32)


test_inputs = [input_1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmprqdqq1sc/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmprqdqq1sc', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmprqdqq1sc/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''