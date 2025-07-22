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
        self.fc = torch.nn.Linear(6, 10)

    def forward(self, x1):
        v1 = x1.view((- 1), 6)
        v2 = torch.addmm(v1, self.fc.weight, self.fc.bias.view(1, (- 1)))
        v3 = torch.cat([v2], dim=1)
        return v3



func = Model().to('cuda')



x1 = torch.randn(1, 6, 10, 10)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (10x6 and 1x10)

jit:
Failed running call_function <built-in method addmm of type object at 0x7dc204e699e0>(*(FakeTensor(..., device='cuda:0', size=(100, 6)), Parameter(FakeTensor(..., device='cuda:0', size=(10, 6), requires_grad=True)), FakeTensor(..., device='cuda:0', size=(1, 10), requires_grad=True)), **{}):
a and b must have same reduction dim, but got [10, 6] X [1, 10].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''