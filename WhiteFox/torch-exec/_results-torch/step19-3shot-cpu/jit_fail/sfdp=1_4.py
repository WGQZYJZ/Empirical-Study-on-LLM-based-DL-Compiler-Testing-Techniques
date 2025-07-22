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

    def __init__(self, dropout_p=0.5, inv_scale_factor=1.0):
        super().__init__()
        self.dropout_p = dropout_p
        self.inv_scale_factor = inv_scale_factor

    def forward(self, query, key, value):
        matrix = torch.matmul(query, key.transpose(-2, -1))
        matrix_scale = matrix.div(self.inv_scale_factor)
        matrix_softmax = matrix_scale.softmax(dim=-1)
        output = torch.nn.functional.dropout(matrix_softmax, self.dropout_p).matmul(value)
        return output


func = Model(dropout_p=0.2, inv_scale_factor=100).to('cpu')


t1 = torch.randn(1, 3, 32, 32)

t2 = torch.randn(1, 4, 32, 32)

t3 = torch.randn(1, 4, 32, 32)

test_inputs = [t1, t2, t3]

# JIT_FAIL
'''
direct:
The size of tensor a (3) must match the size of tensor b (4) at non-singleton dimension 1

jit:
Failed running call_function <built-in method matmul of type object at 0x7fe9b0596ec0>(*(FakeTensor(..., size=(1, 3, 32, 32)), FakeTensor(..., size=(1, 4, 32, 32))), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''