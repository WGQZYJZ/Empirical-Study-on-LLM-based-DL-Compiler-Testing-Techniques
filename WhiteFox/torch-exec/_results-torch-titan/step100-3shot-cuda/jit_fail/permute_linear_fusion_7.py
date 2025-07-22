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
        self.linear1 = torch.nn.Linear(2, 1)
        self.linear2 = torch.nn.Linear(1, 1)

    def forward(self, x1):
        v1 = x1.squeeze()
        v2 = v1.permute(1, 0)
        v3 = torch.nn.functional.linear(v2, self.linear1.weight, self.linear1.bias)
        v4 = v3.permute(1, 0)
        v5 = self.linear2(v4)
        v6 = v5.permute(1, 0)
        return v6




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x2 and 1x1)

jit:
Failed running call_module L__self___linear2(*(FakeTensor(..., device='cuda:0', size=(1, 2)),), **{}):
a and b must have same reduction dim, but got [1, 2] X [1, 1].

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''