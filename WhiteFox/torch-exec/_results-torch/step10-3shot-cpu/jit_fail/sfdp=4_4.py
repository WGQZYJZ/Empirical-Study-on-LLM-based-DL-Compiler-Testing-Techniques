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
        self.q = torch.nn.Parameter(torch.randn(50, 8, dtype=torch.float), requires_grad=True)
        self.k = torch.nn.Parameter(torch.randn(3, 2, dtype=torch.float), requires_grad=True)
        self.v = torch.nn.Parameter(torch.randn(4, 2, dtype=torch.float), requires_grad=True)

    def forward(self, x1, x2):
        qk = self.q @ self.k.transpose(-2, -1) / math.sqrt(self.q.size(-1))
        qk = qk + x2
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ self.v
        return (qk, attn_weight, output)


func = Model().to('cpu')


x1 = torch.randn(1, 50, 8)

x2 = torch.randn(1, 3, 2)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (50x8 and 2x3)

jit:
Failed running call_function <built-in function matmul>(*(Parameter(FakeTensor(..., size=(50, 8), requires_grad=True)), FakeTensor(..., size=(2, 3), requires_grad=True)), **{}):
a and b must have same reduction dim, but got [50, 8] X [2, 3].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''