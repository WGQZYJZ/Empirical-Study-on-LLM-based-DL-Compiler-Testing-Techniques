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
        self.conv1 = torch.nn.Conv2d(3, 8, (3, 3), stride=1, padding=(1, 1))
        self.conv2 = torch.nn.Conv2d(8, 4, (3, 3), stride=1, padding=(1, 1))
        self.conv3 = torch.nn.Conv2d(4, 8, (3, 3), stride=1, padding=(1, 1))
        self.conv4 = torch.nn.Conv2d(8, 4, (3, 3), stride=1, padding=(1, 1))
        self.conv5 = torch.nn.Conv2d(4, 1, (1, 1), stride=1, padding=(0, 0))

    def forward(self, x1, other):
        x1 = self.conv1(x1)
        x2 = self.conv2(x1)
        x3 = self.conv3(x2)
        x4 = self.conv4(x3)
        x5 = self.conv5(x4)
        x6 = (x5 + other)
        return x6




func = Model().to('cuda')



x1 = torch.randn(1, 3, 32, 32)

other = 1

test_inputs = [x1, other]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpnt49baam/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpnt49baam', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpnt49baam/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''