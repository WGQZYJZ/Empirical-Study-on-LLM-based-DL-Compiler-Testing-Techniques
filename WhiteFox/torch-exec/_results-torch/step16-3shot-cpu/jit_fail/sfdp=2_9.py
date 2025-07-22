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
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output


func = Model().to('cpu')


query = torch.randn(1, 3, 32, 64)

key = torch.randn(1, 3, 64, 32)

value = torch.randn(1, 3, 32, 64)

test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [3, 64] but got: [3, 32].

jit:
Failed running call_function <built-in method matmul of type object at 0x7e631af96ec0>(*(FakeTensor(..., size=(1, s0, s4, s5)), FakeTensor(..., size=(1, s0, s2, s1))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [s0, s5] but got: [s0, s2].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''