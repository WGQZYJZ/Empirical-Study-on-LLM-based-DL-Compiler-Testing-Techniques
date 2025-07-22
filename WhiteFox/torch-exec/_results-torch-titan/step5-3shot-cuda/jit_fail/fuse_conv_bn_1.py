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
        self.bn1 = torch.nn.BatchNorm2d(5)
        self.bn2 = torch.nn.BatchNorm2d(3)

    def forward(self, input_t):
        y = self.bn1(input_t)
        z = self.bn2(y)
        q = self.bn1(z)
        return q




func = Model().to('cuda')



x = torch.randn(1, 5, 5, 5)


test_inputs = [x]

# JIT_FAIL
'''
direct:
running_mean should contain 5 elements not 3

jit:
Failed running call_module L__self___bn2(*(FakeTensor(..., device='cuda:0', size=(1, 5, 5, 5)),), **{}):
running_mean should contain 5 elements not 3

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''