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
        self.lin1 = torch.nn.Linear(128, 256)
        self.lin2 = torch.nn.Linear(128, 256)
        self.lin3 = torch.nn.Linear(128, 256)
        self.lin4 = torch.nn.Linear(256, 256)
        self.lin5 = torch.nn.Linear(256, 25)

    def forward(self, x1, x2):
        v1 = self.lin1(x1)
        v2 = torch.nn.functional.relu(v1)
        v3 = self.lin2(x2)
        v4 = torch.nn.functional.relu(v3)
        v5 = self.lin3(v2)
        v6 = torch.nn.functional.relu(v5)
        v7 = self.lin4(v4)
        v8 = torch.nn.functional.relu(v7)
        v9 = (v6 + v8)
        v10 = self.lin5(v9)
        return v10



func = Model().to('cuda')



x1 = torch.randn(4, 128)



x2 = torch.randn(4, 128)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (4x256 and 128x256)

jit:
Failed running call_module L__self___lin3(*(FakeTensor(..., device='cuda:0', size=(4, 256)),), **{}):
a and b must have same reduction dim, but got [4, 256] X [128, 256].

from user code:
   File "<string>", line 30, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''