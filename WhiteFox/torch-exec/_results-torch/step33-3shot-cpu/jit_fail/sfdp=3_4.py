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
        self.scale_factor = torch.sqrt(torch.FloatTensor([1 / 48]))
        self.dropout_p = torch.nn.Parameter(torch.ones(1) * 0.03, requires_grad=True)

    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.mul(self.scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(value)
        return output


func = Model().to('cpu')


query = torch.randn(23, 8, 384)

key = torch.randn(16, 8, 512)

value = torch.randn(16, 8, 512)

test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
The size of tensor a (23) must match the size of tensor b (16) at non-singleton dimension 0

jit:
Failed running call_function <built-in method matmul of type object at 0x78bf3f396ec0>(*(FakeTensor(..., size=(23, 8, 384)), FakeTensor(..., size=(16, 512, 8))), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''