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
        self.conv1 = torch.nn.Conv2d(3, 4, 8, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(3, 4, 8, stride=1, padding=0)
        self.conv3 = torch.nn.Conv2d(3, 4, 8, stride=1, padding=0)
        self.conv4 = torch.nn.Conv2d(3, 4, 8, stride=1, padding=0)
        self.conv5 = torch.nn.Conv2d(3, 4, 8, stride=1, padding=0)
        self.conv6 = torch.nn.Conv2d(3, 4, 8, stride=1, padding=0)
        self.conv7 = torch.nn.Conv2d(3, 4, 8, stride=1, padding=0)
        self.conv8 = torch.nn.Conv2d(3, 4, 8, stride=1, padding=0)

    def forward(self, x1):
        v1 = (self.conv1(x1) * 1)
        v2 = (self.conv2(x1) + 1)
        v3 = (self.conv3(x1) - 1)
        v4 = (self.conv4(x1) * 0)
        v5 = (self.conv5(x1) * 1)
        v6 = (self.conv6(x1) + 1)
        v7 = (self.conv7(x1) - 1)
        v8 = (self.conv8(x1) * 0)
        v9 = (v4 + v5)
        v10 = (v5 + v6)
        v11 = (v6 + v7)
        v12 = (v7 + v8)
        v13 = (v3 + v12)
        v14 = (v4 + v9)
        v15 = (v5 + v10)
        v16 = (v6 + v11)
        v17 = (v7 + v12)
        v18 = (v8 + v9)
        v19 = (v3 + v18)
        v20 = (v14 + v16)
        v21 = (v16 + v18)
        v22 = (v18 + v21)
        return (v22 * v19)




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpg8prdkqh/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpg8prdkqh', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpg8prdkqh/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''