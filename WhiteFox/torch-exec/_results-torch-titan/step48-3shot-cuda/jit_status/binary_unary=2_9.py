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
        self.layers = torch.nn.Sequential(torch.nn.Conv2d(3, 64, 3, stride=2, padding=1, dilation=1), torch.nn.Conv2d(64, 128, 1, stride=1, padding=0, dilation=1), torch.nn.Conv2d(128, 64, 1, stride=1, padding=0, dilation=1))
        self.conv2d = torch.nn.Conv2d(3, 64, 3, stride=2, padding=1)

    def forward(self, x):
        v1 = self.layers(x)
        v2 = self.conv2d(x)
        return (v1 + v2)




func = Model().to('cuda')



x = torch.randn(2, 3, 32, 32)


test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpf6er7tyv/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpf6er7tyv', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpf6er7tyv/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''