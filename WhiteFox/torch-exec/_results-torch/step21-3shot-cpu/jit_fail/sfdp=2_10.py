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

    def forward(self, input, value, query, dropout_p=0.1):
        qk = torch.matmul(query, value.transpose(-2, -1))
        inv_scale_factor = torch.sqrt(torch.tensor(query.size(-1)).float())
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output


func = Model().to('cpu')


input = torch.randn(1, 16, 128)

value = torch.randn(1, 64, 16)

query = torch.randn(1, 8, 128)

test_inputs = [input, value, query]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 128] but got: [1, 16].

jit:
Failed running call_function <built-in method matmul of type object at 0x710640396ec0>(*(FakeTensor(..., size=(1, 8, 128)), FakeTensor(..., size=(1, 16, 64))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 128] but got: [1, 16].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''