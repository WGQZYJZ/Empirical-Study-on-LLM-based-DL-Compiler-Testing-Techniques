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

    def __init__(self, n_heads):
        super().__init__()
        self.n_heads = n_heads
        self.scale_factor = (self.n_heads * self.n_heads) ** 0.5

    def forward(self, x1, x2):
        qk = torch.matmul(x1, x2.transpose(-2, -1))
        scaled_qk = qk * self.scale_factor
        softmax_qk = torch.nn.functional.softmax(scaled_qk, dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.5)
        output = torch.matmul(dropout_qk, x2)
        return output


n_heads = 1
func = Model(8).to('cpu')


x1 = torch.randn(1, 8, 9, 10)

x2 = torch.randn(1, 9, 4, 5)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
The size of tensor a (8) must match the size of tensor b (9) at non-singleton dimension 1

jit:
Failed running call_function <built-in method matmul of type object at 0x78fc07f96ec0>(*(FakeTensor(..., size=(1, 8, 9, 10)), FakeTensor(..., size=(1, 9, 5, 4))), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''