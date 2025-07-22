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

    def __init__(self, query_size, key_size, value_size, dropout_p):
        super().__init__()
        self.dropout_p = dropout_p
        self.query = torch.nn.Parameter(torch.Tensor([0.7152, 0.0001, 0.484, 0.9726, 0.2713, 0.423, 0.1675, 0.2349]), requires_grad=True)
        self.key = torch.nn.Parameter(torch.Tensor([0.8767, 0.807, 0.1362, 0.007, 0.5368, 0.5706, 0.5209, 0.7151]), requires_grad=True)
        self.value = torch.nn.Parameter(torch.Tensor([0.2789, 0.327, 0.197, 0.631, 0.9674, 0.179, 0.5554, 0.8951]), requires_grad=True)
        self.inv_scale_factor = 1 / math.sqrt(key_size)

    def forward(self, x1):
        q = self.query
        k = self.key
        v = self.value
        qk = torch.matmul(q, k.transpose(-2, -1))
        scaled_qk = qk.div(self.inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(v)
        return output


query_size = 1
key_size = 1
value_size = 1
dropout_p = 1
func = Model(8, 8, 8, 0.01479775).to('cpu')


x1 = torch.randn(1, 8, 15)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Dimension out of range (expected to be in range of [-1, 0], but got -2)

jit:
Failed running call_method transpose(*(Parameter(FakeTensor(..., size=(8,), requires_grad=True)), -2, -1), **{}):
Dimension out of range (expected to be in range of [-1, 0], but got -2)

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''