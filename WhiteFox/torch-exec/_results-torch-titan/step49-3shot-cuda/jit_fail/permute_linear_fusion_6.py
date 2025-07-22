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
        self.linear0 = torch.nn.Linear(2, 120)
        self.linear1 = torch.nn.Linear(120, 84)
        self.linear2 = torch.nn.Linear(84, 10)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = self.linear0(x1)
        v3 = self.linear1(v2)
        v4 = self.linear2(v2)
        return x1




func = Model().to('cuda')



x1 = torch.randn(2, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (4x120 and 84x10)

jit:
Failed running call_module L__self___linear2(*(FakeTensor(..., device='cuda:0', size=(2, 2, 120)),), **{}):
a and b must have same reduction dim, but got [4, 120] X [84, 10].

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''