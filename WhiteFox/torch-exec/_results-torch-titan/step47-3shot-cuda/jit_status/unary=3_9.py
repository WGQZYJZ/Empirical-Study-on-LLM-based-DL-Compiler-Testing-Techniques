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
        self.conv = torch.nn.Conv2d(1, 48, 3, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(48, 4, 3, stride=2, padding=1)
        self.conv3 = torch.nn.Conv2d(4, 16, 3, stride=1, padding=0)
        self.conv4 = torch.nn.Conv2d(16, 7, 3, stride=2, padding=1)
        self.conv5 = torch.nn.Conv2d(7, 4, 3, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 * 0.5)
        v3 = (v1 * 0.7071067811865476)
        v4 = torch.erf(v3)
        v5 = (v4 + 1)
        v6 = (v2 * v5)
        v7 = self.conv2(v6)
        v8 = (v7 * 0.5)
        v9 = (v7 * 0.7071067811865476)
        v10 = torch.erf(v9)
        v11 = (v10 + 1)
        v12 = (v8 * v11)
        v13 = self.conv3(v12)
        v14 = (v13 * 0.5)
        v15 = (v13 * 0.7071067811865476)
        v16 = torch.erf(v15)
        v17 = (v16 + 1)
        v18 = (v14 * v17)
        v19 = self.conv4(v18)
        v20 = (v19 * 0.5)
        v21 = (v19 * 0.7071067811865476)
        v22 = torch.erf(v21)
        v23 = (v22 + 1)
        v24 = (v20 * v23)
        v25 = self.conv5(v24)
        return v25




func = Model().to('cuda')



x1 = torch.randn(1, 1, 58, 60)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp0q_3ja9a/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp0q_3ja9a', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp0q_3ja9a/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''