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
        self.conv = torch.nn.Conv2d(96, 13, 3, stride=2, padding=1)
        self.conv2 = torch.nn.Conv2d(13, 6, 1, stride=2, padding=0)
        self.conv3 = torch.nn.Conv2d(6, 57, 1, stride=1, padding=0)
        self.conv4 = torch.nn.Conv2d(57, 38, 3, stride=2, padding=1)
        self.conv5 = torch.nn.Conv2d(38, 13, 3, stride=2, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.tanh(v1)
        v3 = self.conv2(v2)
        v4 = torch.abs(v3)
        v5 = torch.sigmoid(v4)
        v6 = self.conv3(v5)
        v7 = (v6 * 0.5)
        v8 = (v6 * 0.7071067811865476)
        v9 = torch.erf(v8)
        v10 = (v9 + 1)
        v11 = (v7 * v10)
        v12 = self.conv4(v11)
        v13 = (v12 * 0.5)
        v14 = (v12 * 0.7071067811865476)
        v15 = torch.erf(v14)
        v16 = (v15 + 1)
        v17 = (v13 * v16)
        v18 = self.conv5(v17)
        v19 = (v18 * 0.5)
        v20 = (v18 * 0.7071067811865476)
        v21 = torch.erf(v20)
        v22 = (v21 + 1)
        v23 = (v19 * v22)
        return v23




func = Model().to('cuda')



x1 = torch.randn(1, 96, 1, 1)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpocgzd0up/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpocgzd0up', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpocgzd0up/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''