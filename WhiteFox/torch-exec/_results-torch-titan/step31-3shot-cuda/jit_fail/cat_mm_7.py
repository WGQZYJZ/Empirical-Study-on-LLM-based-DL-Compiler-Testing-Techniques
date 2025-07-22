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



class CustomModule(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 2)
        self.linear2 = torch.nn.Linear(2, 2)

    def forward(self, x, z):
        h = self.linear1(x)
        h.add_(self.linear2(x))
        h.sub_(self.linear1(z))
        h.add_(self.linear1(x))
        return h




class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 5)
        self.linear2 = torch.nn.Linear(5, 2)
        self.custom = CustomModule()

    def forward(self, u, v, w):
        x = self.linear1(u)
        y = self.linear1(v)
        z = self.linear1(w)
        return self.custom(x, y)




func = Model().to('cuda')



u = torch.randn(3, 2)



v = torch.randn(3, 2)



w = torch.randn(3, 2)


test_inputs = [u, v, w]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (3x2 and 3x5)

jit:
Failed running call_module L__self___linear1(*(FakeTensor(..., device='cuda:0', size=(3, 2)),), **{}):
a and b must have same reduction dim, but got [3, 2] X [3, 5].

from user code:
   File "<string>", line 41, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''