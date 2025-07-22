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
        self.conv1 = torch.nn.Conv2d(16, 16, 2)
        self.bn1 = torch.nn.BatchNorm2d(16)
        self.conv2 = torch.nn.Conv2d(16, 16, 2)
        self.bn2 = torch.nn.BatchNorm2d(16)

    def forward(self, x):
        x1 = self.conv1(x)
        x2 = self.bn1(x1)
        x4 = self.bn1(x2)
        x3 = self.conv2(x4)
        x5 = self.bn2(x3)
        x6 = self.bn2(x4)
        m = []
        for _ in range(torch.randint(1, 5, (1,)).item()):
            m.append(x5)
        x7 = (((((m[0] + m[1]) + x1) + x3) + (x5 * x6)) + torch.cat([x1, x3], dim=1))
        return x7




func = Model().to('cuda')



x = torch.randn(1, 16, 4, 4)


test_inputs = [x]

# JIT_FAIL
'''
direct:
The size of tensor a (2) must match the size of tensor b (3) at non-singleton dimension 3

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpqpil4zjm/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpqpil4zjm', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpqpil4zjm/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''