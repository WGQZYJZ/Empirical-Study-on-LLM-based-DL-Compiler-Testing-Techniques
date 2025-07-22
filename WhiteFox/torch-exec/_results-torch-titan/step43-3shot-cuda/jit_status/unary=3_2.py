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
        self.conv1 = torch.nn.Conv2d(128, 293, 43, stride=20, padding=30)
        self.conv2 = torch.nn.Conv2d(293, 7192, 2, stride=2, padding=2)
        self.conv3 = torch.nn.Conv2d(7192, 120, 31, stride=13, padding=23)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = (v1 * (- 0.8))
        v3 = (v1 * 0.2)
        v4 = torch.relu(v3)
        v5 = self.conv2(v4)
        v6 = (v5 * 0.6)
        v7 = (v5 * 0.4)
        v8 = torch.erf(v7)
        v9 = (v8 + 1)
        v10 = (v6 * v9)
        v11 = self.conv3(v10)
        v12 = (v11 * 0.5)
        v13 = (v11 * 0.7071067811865476)
        v14 = torch.erf(v13)
        v15 = (v14 + 1)
        v16 = (v12 * v15)
        return v16




func = Model().to('cuda')



x1 = torch.randn(1, 128, 54, 83)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpi9td4_d4/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpi9td4_d4', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpi9td4_d4/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''