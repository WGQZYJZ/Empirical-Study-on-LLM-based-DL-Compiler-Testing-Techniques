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
        self.conv = torch.nn.Conv2d(2, 3, 3)
        torch.manual_seed(1)
        self.bn = torch.nn.BatchNorm2d(4)

    def forward(self, x1):
        v1 = self.bn(x1)
        v2 = self.conv(v1)
        v2 = self.bn(v2)
        return v2




func = Model().to('cuda')



x1 = torch.randn(1, 2, 3, 3)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
running_mean should contain 2 elements not 4

jit:
Failed running call_module L__self___bn(*(FakeTensor(..., device='cuda:0', size=(1, 2, 3, 3)),), **{}):
running_mean should contain 2 elements not 4

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''