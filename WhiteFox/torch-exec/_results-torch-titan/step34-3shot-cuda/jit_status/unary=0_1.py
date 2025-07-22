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
        self.conv1 = torch.nn.Conv3d(8, 23, 5, stride=1, padding=2)
        self.bn1 = torch.nn.BatchNorm3d(23)
        self.conv2 = torch.nn.Conv3d(23, 17, 7, stride=1, padding=1)
        self.bn2 = torch.nn.BatchNorm3d(17)

    def forward(self, x6):
        v1 = self.conv1(x6)
        v2 = self.bn1(v1)
        v3 = torch.sinh(v2)
        v4 = self.conv2(v3)
        v5 = self.bn2(v4)
        v6 = (v5 * 0.5)
        v7 = (v5 * v5)
        v8 = (v7 * v5)
        v9 = (v8 * 0.044715)
        v10 = (v5 + v9)
        v11 = (v10 * 0.7978845608028654)
        v12 = torch.tanh(v11)
        v13 = (v12 + 1)
        v14 = (v6 * v13)
        return v14




func = Model().to('cuda')



x6 = torch.randn(4, 8, 23, 23, 23)


test_inputs = [x6]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpyn85c0pb/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpyn85c0pb', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpyn85c0pb/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''