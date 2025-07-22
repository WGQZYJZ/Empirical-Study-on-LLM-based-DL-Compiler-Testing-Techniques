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

    def __init__(self, hidden_dim=None):
        super().__init__()
        self.key = torch.nn.Parameter(torch.randn((hidden_dim or 8), (hidden_dim or 8)))
        self.query = torch.nn.Parameter(torch.randn((hidden_dim or 8), (hidden_dim or 8)))

    def forward(self, x3):
        v7 = torch.matmul(x3, self.query.t())
        v8 = torch.diagonal(v7, 0)
        v9 = torch.sum(v8, dim=1)
        v10 = torch.reciprocal(v9)
        v11 = torch.matmul(x3, self.key.t())
        v12 = (v11 * v10)
        v13 = torch.softmax(v12, dim=1)
        v14 = torch.nn.functional.dropout(v13, p=0.2)
        v15 = torch.matmul(v14, self.query)
        return v15



func = Model().to('cuda')



x3 = torch.randn(5, 8, 32)


test_inputs = [x3]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (40x32 and 8x8)

jit:
Failed running call_function <built-in method matmul of type object at 0x72566de699e0>(*(FakeTensor(..., device='cuda:0', size=(5, 8, 32)), FakeTensor(..., device='cuda:0', size=(8, 8), requires_grad=True)), **{}):
a and b must have same reduction dim, but got [40, 32] X [8, 8].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''