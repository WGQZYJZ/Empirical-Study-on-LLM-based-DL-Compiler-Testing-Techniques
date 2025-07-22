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



class Model1(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 3, 1, stride=2, padding=0)
        self.conv2 = torch.nn.Conv2d(3, 5, 3, stride=1, padding=6)

    def forward(self, x1, x2, other1=1, other2=1):
        v1 = self.conv1(x1)
        v2 = torch.max_pool2d(v1, 3, stride=1, padding=5)
        v3 = self.conv2(v2)
        v4 = torch.mean(v3, dim=1, keepdim=True)
        return v4




class Model2(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 3, 3, stride=3, padding=4)
        self.conv2 = torch.nn.Conv2d(3, 5, 1, stride=1, padding=0)

    def forward(self, x1, x2, other1=1, other2=1):
        v1 = (x1 + other2)
        v2 = self.conv1(v1)
        v3 = (v2 + other1)
        v4 = torch.max_pool2d(v3, 3, stride=1, padding=5)
        v5 = self.conv2(v4)
        v6 = torch.mean(v5, dim=1, keepdim=True)
        return v6




func = Model2().to('cuda')



x1 = torch.randn(1, 3, 16, 16)



x2 = torch.randn(1, 3, 10, 10)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
pad should be at most half of kernel size, but got pad=5 and kernel_size=3

jit:
Failed running call_function <built-in method max_pool2d of type object at 0x729671a699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 3, 8, 8)), 3), **{'stride': 1, 'padding': 5}):
pad should be at most half of kernel size, but got pad=5 and kernel_size=3

from user code:
   File "<string>", line 43, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''