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
        torch.manual_seed(7)
        self.bn = torch.nn.BatchNorm2d(3)
        self.conv = torch.nn.Conv2d(16, 32, 3, padding=1)

    def forward(self, x3):
        y1 = self.conv(x3)
        t1 = self.bn(y1)
        t2 = self.conv(t1)
        return None




func = Model().to('cuda')



x3 = torch.randn(2, 16, 10, 10)


test_inputs = [x3]

# JIT_FAIL
'''
direct:
running_mean should contain 32 elements not 3

jit:
Failed running call_module L__self___bn(*(FakeTensor(..., device='cuda:0', size=(2, 32, 10, 10)),), **{}):
running_mean should contain 32 elements not 3

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''