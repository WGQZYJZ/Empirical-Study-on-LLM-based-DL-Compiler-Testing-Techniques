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



class model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(1, 4)
        self.linear2 = torch.nn.Linear(4, 4)
        self.linear3 = torch.nn.Linear(4, 4)
        self.linear4 = torch.nn.Linear(4, 4)
        self.linear5 = torch.nn.Linear(4, 4)
        self.linear6 = torch.nn.Linear(4, 4)
        self.linear7 = torch.nn.Linear(4, 4)
        self.linear8 = torch.nn.Linear(4, 4)
        self.linear9 = torch.nn.Linear(4, 4)
        self.linear10 = torch.nn.Linear(4, 4)

    def forward(self, x1):
        x2 = self.linear1(x1)
        x3 = self.linear2(x2)
        x4 = self.linear3(x3)
        x5 = self.linear4(x3)
        x6 = self.linear5(x4)
        x7 = self.linear8(x6)
        x8 = self.linear7(x7)
        x9 = self.linear9(x7)
        x10 = self.linear10(x9)
        x11 = (x2 - x4)
        return x11




func = model().to('cuda')



x1 = torch.randn(1, 1)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpduxx61dd/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpduxx61dd', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpduxx61dd/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''