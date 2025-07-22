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

    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1))
        inv_scale_factor = math.sqrt(dimension_per_head)
        scaled = qk.div(inv_scale_factor)
        softmax = scaled.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output


func = Model().to('cpu')


query = torch.randn(1, 12, 12, 36)

key = torch.randn(1, 6, 12, 36)

value = torch.randn(1, 6, 12, 36)

test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
The size of tensor a (12) must match the size of tensor b (6) at non-singleton dimension 1

jit:
Failed running call_function <built-in method matmul of type object at 0x74f71e996ec0>(*(FakeTensor(..., size=(1, 12, 12, 36)), FakeTensor(..., size=(1, 6, 36, 12))), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''