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
        self.conv = torch.nn.Conv2d(1, 8, 1, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(8, 1, 1, stride=1, padding=0)
        self.conv3 = torch.nn.Conv2d(1, 1, 3, stride=1, padding=1)
        self.conv4 = torch.nn.Conv2d(1, 8, 1, stride=1, padding=0)
        self.conv5 = torch.nn.Conv2d(1, 1, 3, stride=1, padding=1)
        self.conv6 = torch.nn.Conv2d(1, 7, 1, stride=1, padding=0)
        self.conv8 = torch.nn.Conv2d(7, 8, 1, stride=1, padding=0)
        self.conv9 = torch.nn.ConvTranspose2d(8, 1, 1, stride=2, padding=0)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 * 0.5)
        v3 = (v1 * 0.7071067811865476)
        v4 = torch.erf(v3)
        v5 = (v4 + 0.9993292997390671)
        v6 = (v2 * v5)
        v7 = self.conv2(v6)
        v8 = self.conv3(x1)
        v9 = (v8 * 0.5)
        v10 = (v8 * 0.7071067811865476)
        v11 = torch.erf(v10)
        v12 = (v11 + 0.9993292997390671)
        v13 = (v9 * v12)
        v14 = self.conv4(x1)
        v15 = self.conv5(x1)
        v16 = (v15 * 0.5)
        v17 = (v15 * 0.7071067811865476)
        v18 = torch.erf(v17)
        v19 = (v18 + 0.9993292997390671)
        v20 = (v16 * v19)
        v21 = self.conv6(x1)
        v22 = self.conv8(v21)
        v23 = (v22 * 0.5)
        v24 = (v22 * 0.7071067811865476)
        v25 = torch.erf(v24)
        v26 = (v25 + 0.9993292997390671)
        v27 = (v23 * v26)
        v28 = self.conv9(v27)
        return v28




func = Model().to('cuda')



x1 = torch.randn(1, 1, 53, 50)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpr80ciqxg/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpr80ciqxg', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpr80ciqxg/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''