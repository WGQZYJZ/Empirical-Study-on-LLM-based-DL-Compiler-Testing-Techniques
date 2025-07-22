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

    def forward(self, query, key, value, inv_scale_factor):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.div(inv_scale_factor)
        dropout_qk = torch.nn.functional.dropout(scaled_qk.softmax(dim=-1), p=1 - 0.75)
        output = dropout_qk.matmul(value)
        return output


func = Model().to('cpu')


query = x = torch.randn(1, 10, 4)

key = k = torch.randn(1, 10, 8)

value = v = torch.randn(1, 10, 8)

inv_scale_factor = z = torch.tensor(0.03125)

test_inputs = [query, key, value, inv_scale_factor]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 4] but got: [1, 8].

jit:
Failed running call_function <built-in method matmul of type object at 0x7d2d8cd96ec0>(*(FakeTensor(..., size=(1, 10, 4)), FakeTensor(..., size=(1, 8, 10))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 4] but got: [1, 8].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''