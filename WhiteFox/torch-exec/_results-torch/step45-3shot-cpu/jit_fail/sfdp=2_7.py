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

    def __init__(self, input_x, input_y, input_z):
        super().__init__()

    def forward(self, q, k, v):
        qk = torch.matmul(q, k.transpose(-2, -1))
        inv_scale_factor = math.sqrt(q.size(-1))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.1)
        output = dropout_qk.matmul(v)
        return output


input_x = torch.randn(1, 2, 8, 8)
input_y = torch.randn(1, 4, 8, 8)
input_z = torch.randn(3, 4, 1, 1)

func = Model(input_x, input_y, input_z).to('cpu')


input_x = torch.randn(1, 2, 8, 8)

input_y = torch.randn(1, 4, 8, 8)

input_z = torch.randn(3, 4, 1, 1)

test_inputs = [input_x, input_y, input_z]

# JIT_FAIL
'''
direct:
The size of tensor a (2) must match the size of tensor b (4) at non-singleton dimension 1

jit:
Failed running call_function <built-in method matmul of type object at 0x75b0e3f96ec0>(*(FakeTensor(..., size=(1, s3, s4, s5)), FakeTensor(..., size=(1, s0, s2, s1))), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''