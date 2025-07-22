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

    def __init__(self, stride):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(8, 8, 3, stride=stride, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 8, 3, stride=stride, padding=1)

    def forward(self, x, flag=0):
        v1 = self.conv1(x)
        v2 = self.conv2(v1)
        v3 = (v2 > 0)
        v4 = (v2 * (- 0.01))
        v5 = torch.where(v3, v2, v4)
        return v5



stride = 1

func = Model(stride).to('cuda')



x1 = torch.randn(1, 8, 256, 256)

x = 1

test_inputs = [x1, x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpq1b8uyfn/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpq1b8uyfn', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpq1b8uyfn/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''