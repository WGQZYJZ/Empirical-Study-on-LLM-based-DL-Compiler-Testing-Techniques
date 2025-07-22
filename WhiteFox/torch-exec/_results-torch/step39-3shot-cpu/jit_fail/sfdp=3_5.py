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

    def forward(self, query, key, value, scale_factor, dropout_p=0.1):
        qk = torch.matmul(query, key.transpose(-2, -1))
        qk = qk * scale_factor
        softmax_qk = torch.nn.functional.softmax(qk, dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        return torch.matmul(dropout_qk, value)


func = Model().to('cpu')


query = torch.randn(3, 5, 7)

key = torch.randn(3, 7, 11)

value = torch.randn(3, 5, 11)
scale_factor = 1

test_inputs = [query, key, value, scale_factor]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [3, 7] but got: [3, 11].

jit:
Failed running call_function <built-in method matmul of type object at 0x7feea9396ec0>(*(FakeTensor(..., size=(s0, s4, s5)), FakeTensor(..., size=(s0, s2, s1))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [s0, s5] but got: [s0, s2].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''