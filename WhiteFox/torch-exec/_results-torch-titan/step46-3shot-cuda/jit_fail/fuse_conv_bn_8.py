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
        self.conv1 = torch.nn.Conv2d(100, 16, 5, stride=1, padding=1, bias=False)
        torch.manual_seed(50)
        self.bn1 = torch.nn.BatchNorm2d(1)
        torch.manual_seed(50)
        self.bn2 = torch.nn.BatchNorm2d(16)

    def forward(self, x):
        y = self.conv1(x)
        y = self.bn1(y)
        y = (y * y)
        y = self.bn2(y)
        return y




func = Model().to('cuda')



x = torch.randn(1, 100, 30, 30)


test_inputs = [x]

# JIT_FAIL
'''
direct:
running_mean should contain 16 elements not 1

jit:
Failed running call_module L__self___bn1(*(FakeTensor(..., device='cuda:0', size=(1, 16, 28, 28)),), **{}):
running_mean should contain 16 elements not 1

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''