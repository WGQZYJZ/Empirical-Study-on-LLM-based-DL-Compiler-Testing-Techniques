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
        self.avg_pool2d = torch.nn.AvgPool2d(kernel_size=11, stride=1, padding=5)
        self.conv2d = torch.nn.Conv2d(8, 5, 5, stride=1, padding=2)

    def forward(self, x1):
        v1 = self.avg_pool2d(x1)
        v2 = self.conv2d(v1)
        v3 = (v2 * 0.5)
        v4 = (v2 * 0.7071067811865476)
        v5 = torch.erf(v4)
        v6 = (v5 + 1)
        v7 = (v3 * v6)
        return v7




func = Model().to('cuda')



x1 = torch.randn(1, 8, 32, 32)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpeutkskp6/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpeutkskp6', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpeutkskp6/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''