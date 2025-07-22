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
        self.t1 = torch.nn.Conv2d(in_channels=3, out_channels=3, kernel_size=1, stride=1, padding=0, dilation=2)
        self.t2 = torch.nn.Conv2d(in_channels=3, out_channels=3, kernel_size=3, stride=2, padding=1, dilation=1)
        self.t3 = torch.nn.Conv2d(in_channels=3, out_channels=3, kernel_size=3, stride=2, padding=1, dilation=1)

    def forward(self, x1):
        v1 = self.t1(x1)
        v2 = torch.sigmoid(v1)
        v3 = self.t2(v2)
        v4 = torch.sigmoid(v3)
        v5 = self.t3(v4)
        v6 = torch.sigmoid(v5)
        return v6




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpv64bpzhw/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpv64bpzhw', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpv64bpzhw/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''