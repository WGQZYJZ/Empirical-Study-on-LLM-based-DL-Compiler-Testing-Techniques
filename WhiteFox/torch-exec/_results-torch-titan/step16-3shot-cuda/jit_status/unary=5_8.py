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
        self.conv_transpose1 = torch.nn.ConvTranspose2d(10, 6, 1, stride=3, padding=2)
        self.conv_transpose2 = torch.nn.ConvTranspose2d(6, 3, 5, stride=2, padding=1)

    def forward(self, x1):
        v1 = self.conv_transpose1(x1)
        v2 = (v1 * 0.5)
        v3 = (v1 * 0.7071067811865476)
        v4 = torch.erf(v3)
        v5 = (v4 + 1)
        v6 = (v2 * v5)
        v7 = self.conv_transpose2(v6)
        v8 = (v7 * 0.5)
        v9 = (v7 * 0.7071067811865476)
        v10 = torch.erf(v9)
        v11 = (v10 + 1)
        v12 = (v8 * v11)
        return v12




func = Model().to('cuda')



x1 = torch.randn(1, 10, 3, 3)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpo5q8iujy/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpo5q8iujy', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpo5q8iujy/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''