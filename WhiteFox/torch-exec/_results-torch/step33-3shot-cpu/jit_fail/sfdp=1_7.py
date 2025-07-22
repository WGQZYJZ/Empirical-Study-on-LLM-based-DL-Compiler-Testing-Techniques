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
        self.dropout_p = 0.1
        super().__init__()

    def forward(self, query, key, value, scale_factor):
        qk = torch.matmul(query, key.transpose(-2, -1))
        inv_scale_factor = 1.0 / scale_factor
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(value)
        return output


func = Model().to('cpu')


query = torch.randn(2, 3, 4)

key = torch.randn(2, 4, 5)

value = torch.randn(2, 4, 5)

scale_factor = torch.randn(2, 1, 1)

test_inputs = [query, key, value, scale_factor]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [2, 4] but got: [2, 5].

jit:
Failed running call_function <built-in method matmul of type object at 0x7d2d8cd96ec0>(*(FakeTensor(..., size=(2, 3, 4)), FakeTensor(..., size=(2, 5, 4))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [2, 4] but got: [2, 5].

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''