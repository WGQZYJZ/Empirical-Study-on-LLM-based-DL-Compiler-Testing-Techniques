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
        self.linear = torch.nn.Linear(2, 2)
        self.linear1 = torch.nn.Linear(2, 1)
        self.linear2 = torch.nn.Linear(1, 1)
        self.linear3 = torch.nn.Linear(2, 2)
        self.linear4 = torch.nn.Linear(2, 1)
        self.linear5 = torch.nn.Linear(1, 1)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        v2 = v2.tanh()
        v3 = torch.sigmoid(torch.nn.functional.linear(v2, self.linear1.weight, self.linear1.bias))
        v4 = torch.nn.functional.linear(v2, self.linear2.weight, torch.cat((self.linear2.bias, torch.tensor([1]).to(self.linear2.bias)), dim=0))
        v4 = torch.sigmoid(v4)
        v5 = torch.cat((v3, v4), dim=-1)
        v5 = v5.unsqueeze(dim=-1)
        v5 = v5.expand(1, 1, 8)
        v6 = v2.expand(1, 2, 2) * v5
        v7 = torch.sigmoid(torch.nn.functional.linear(v6, self.linear3.weight, self.linear3.bias))
        v6 = torch.sigmoid(torch.nn.functional.linear(v6, self.linear4.weight, torch.cat((self.linear4.bias, torch.tensor([1]).to(self.linear4.bias)), dim=0)))
        v8 = v6 * v7
        v8 = torch.nn.functional.linear(v8, self.linear5.weight, self.linear5.bias)
        return v8



func = Model().to('cpu')


x1 = torch.randn(1, 2, 2)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x2 and 1x1)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 2, 2)), Parameter(FakeTensor(..., size=(1, 1), requires_grad=True)), FakeTensor(..., size=(2,))), **{}):
a and b must have same reduction dim, but got [2, 2] X [1, 1].

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''