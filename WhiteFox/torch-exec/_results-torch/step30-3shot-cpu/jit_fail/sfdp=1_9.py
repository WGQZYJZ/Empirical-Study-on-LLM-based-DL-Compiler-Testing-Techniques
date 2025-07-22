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

    def __init__(self, dim=6, input_dim=12, value_dim=8, dropout_p=0.3):
        super().__init__()
        self.dropout_p = dropout_p
        self.dim = dim
        self.query = torch.nn.Linear(input_dim, dim)
        self.key = torch.nn.Linear(input_dim, dim)
        self.value = torch.nn.Linear(input_dim, value_dim)

    def forward(self, x1):
        q1 = self.query(x1)
        k1 = self.key(x1)
        v1 = self.value(x1)
        q2 = q1.view(-1, self.dim, 1)
        k2 = k1.view(-1, 1, self.dim)
        q3 = q2.expand(-1, -1, self.dim).flatten(-2, -1)
        k3 = k2.expand(-1, -1, self.dim).flatten(-2, -1)
        q4 = torch.matmul(q3, k3.transpose(-2, -1))
        q5 = q4.div(self.dim ** (-0.5))
        q6 = q5.softmax(dim=-1)
        q7 = torch.nn.functional.dropout(q6, p=self.dropout_p)
        q8 = torch.matmul(q7, v1)
        return q8


func = Model().to('cpu')


x1 = torch.randn(1, 12)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x36 and 6x1)

jit:
Failed running call_function <built-in method matmul of type object at 0x7b0457d96ec0>(*(FakeTensor(..., size=(1, 36)), FakeTensor(..., size=(6, 1))), **{}):
a and b must have same reduction dim, but got [1, 36] X [6, 1].

from user code:
   File "<string>", line 31, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''