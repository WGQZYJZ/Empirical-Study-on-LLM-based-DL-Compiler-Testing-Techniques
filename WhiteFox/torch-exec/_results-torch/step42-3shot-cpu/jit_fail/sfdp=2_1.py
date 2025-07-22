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
        self.linear1 = torch.nn.Linear(64, 8)
        self.linear3 = torch.nn.Linear(64, 8)
        self.linear4 = torch.nn.Linear(64, 8)

    def forward(self, x1, x2, x3):
        v1 = self.linear1(x1)
        v2 = self.linear3(x2)
        v3 = self.linear4(x3)
        v4 = torch.matmul(v1, v2.transpose(-2, -1))
        v5 = v4.div(0.5)
        v6 = v5.softmax(dim=-1)
        v7 = torch.nn.functional.dropout(v6, p=0.5, training=self.training)
        v8 = v3.matmul(v7)
        return v8


func = Model().to('cpu')


x1 = torch.randn(1, 64)

x2 = torch.randn(1, 64)

x3 = torch.randn(1, 64)

test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x8 and 1x1)

jit:
Failed running call_method matmul(*(FakeTensor(..., size=(1, 8)), FakeTensor(..., size=(1, 1))), **{}):
a and b must have same reduction dim, but got [1, 8] X [1, 1].

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''