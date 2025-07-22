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
        self.linear = torch.nn.Linear(4, 1025)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        x2 = v2.transpose(1, 2)
        x3 = x2
        x4 = x2.transpose(2, 3)
        v4 = torch.clamp(x4, 0, 1)
        v5 = (x2 + v4)
        x4 = x2.transpose(1, 2)
        v5 = x4.transpose(0, 2).transpose(2, 3)
        return x2




func = Model().to('cuda')



x1 = torch.randn(1, 4, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Dimension out of range (expected to be in range of [-3, 2], but got 3)

jit:
Failed running call_method transpose(*(FakeTensor(..., device='cuda:0', size=(1, 1025, 2)), 2, 3), **{}):
Dimension out of range (expected to be in range of [-3, 2], but got 3)

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''