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
        self.a = torch.nn.Conv3d(1, 1, 1, bias=False, padding=2, dilation=2)
        self.b = torch.nn.BatchNorm3d(1, affine=True, track_running_stats=True)

    def forward(self, x):
        y = self.b(self.a(x))
        z = self.b(self.a(x))
        return (y, z)




func = Model().to('cuda')



x = torch.randn(1, 1, 1, 5, 5)


test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmptg3rx86m/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmptg3rx86m', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmptg3rx86m/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''