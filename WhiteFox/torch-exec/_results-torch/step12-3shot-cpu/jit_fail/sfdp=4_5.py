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
        self.query = torch.nn.Linear(4, 4)
        self.key = torch.nn.Linear(4, 4)

    def forward(self, q1, k2, p3=torch.tensor(1.0)):
        qk = self.query(q1) @ self.key(k2).transpose(-2, -1) / math.sqrt(self.query.weight.size(-1))
        qk = qk + p3
        attn_weight = torch.softmax(qk, dim=-1)
        return attn_weight @ self.value(v3)


func = Model().to('cpu')


x1 = torch.randn(2, 4)

x2 = torch.randn(2, 4)

x3 = torch.randn(2, 4)

test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
The size of tensor a (2) must match the size of tensor b (4) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(2, 2)), FakeTensor(..., size=(2, 4))), **{}):
Attempting to broadcast a dimension of length 4 at -1! Mismatching argument at index 1 had torch.Size([2, 4]); but expected shape should be broadcastable to [2, 2]

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''