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

    def forward(self, q, k, v, isf, dp):
        qk = torch.matmul(q, k.transpose(-2, -1))
        scaled_qk = qk.div(isf)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dp)
        output = dropout_qk.matmul(v)
        return output


func = Model().to('cpu')


q1 = torch.randn(3, 5, 6)

k1 = torch.randn(5, 4, 6)

v1 = torch.randn(5, 4, 6)

isf1 = torch.tensor(1.0)

dp1 = torch.tensor(0.0)

test_inputs = [q1, k1, v1, isf1, dp1]

# JIT_FAIL
'''
direct:
The size of tensor a (3) must match the size of tensor b (5) at non-singleton dimension 0

jit:
Failed running call_function <built-in method matmul of type object at 0x7d808b196ec0>(*(FakeTensor(..., size=(3, 5, 6)), FakeTensor(..., size=(5, 6, 4))), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''