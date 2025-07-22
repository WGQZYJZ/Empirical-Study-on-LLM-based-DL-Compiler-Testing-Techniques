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
        self.linear = torch.nn.Linear(144, 512)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 * torch.max(torch.min((v1 + 3), 6), 0))
        v3 = (v2 / 6)
        return v3



func = Model().to('cuda')



x1 = torch.randn(1, 144)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Dimension out of range (expected to be in range of [-2, 1], but got 6)

jit:
Failed running call_function <built-in method min of type object at 0x79d7c2c699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 512)), 6), **{}):
Dimension out of range (expected to be in range of [-2, 1], but got 6)

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''