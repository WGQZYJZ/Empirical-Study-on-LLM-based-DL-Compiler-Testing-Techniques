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
        torch.manual_seed(1)
        self.conv = torch.nn.Conv2d(16, 16, 3)
        torch.manual_seed(2)
        self.bn1 = torch.nn.BatchNorm2d(16)
        torch.manual_seed(3)
        self.bn2 = torch.nn.BatchNorm2d(16)
        torch.manual_seed(4)
        self.bn3 = torch.nn.BatchNorm1d(16)
        torch.manual_seed(1)

    def forward(self, x0):
        v0 = self.bn1(x0)
        v0 = self.bn2(x0)
        v0 = F.relu(v0)
        v0 = self.bn2(v0)
        v0 = self.bn3(v0)
        v0 = F.relu(v0)
        v0 = self.bn2(v0)
        return v0




func = Model().to('cuda')



x0 = torch.randn(1, 16, 3, 3)


test_inputs = [x0]

# JIT_FAIL
'''
direct:
expected 2D or 3D input (got 4D input)

jit:
Failed running call_module L__self___bn3(*(FakeTensor(..., device='cuda:0', size=(1, 16, 3, 3)),), **{}):
expected 2D or 3D input (got 4D input)

from user code:
   File "<string>", line 34, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''