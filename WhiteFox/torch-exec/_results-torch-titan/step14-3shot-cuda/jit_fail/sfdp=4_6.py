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
        self.query = torch.nn.Linear(64, 32)
        self.key = torch.nn.Linear(32, 16)
        self.weight = torch.tensor([((32 / 32) / 32), ((16 / 32) / 16)])
        self.weight.requires_grad = False
        self.value = torch.nn.Linear(32, 32)
        self.mask = torch.tensor([[0], [0], [0], [1], [1]], dtype=torch.float32)

    def forward(self, x1):
        q1 = self.query(x1)
        k1 = self.key(q1)
        qk1 = ((self.weight.view((- 1)) * q1) * k1)
        p = (qk1 + self.mask)
        return (torch.softmax(p, dim=(- 1)) @ self.value(q1))



func = Model().to('cuda')



x1 = torch.randn(5, 32)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (5x32 and 64x32)

jit:
Failed running call_module L__self___query(*(FakeTensor(..., device='cuda:0', size=(5, 32)),), **{}):
a and b must have same reduction dim, but got [5, 32] X [64, 32].

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''