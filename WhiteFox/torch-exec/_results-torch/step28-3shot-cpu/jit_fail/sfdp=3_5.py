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
        super(Model, self).__init__()

    def forward(self, query, key, scale_factor, dropout_p, value):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = f.softmax(scaled_qk, dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output


func = Model().to('cpu')


query = torch.rand(20, 10, 128)

key = torch.rand(20, 128, 16)

scale_factor = torch.tensor([10.0])

value = torch.rand(20, 16, 128)
dropout_p = 1

test_inputs = [query, key, scale_factor, value, dropout_p]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [20, 128] but got: [20, 16].

jit:
Failed running call_function <built-in method matmul of type object at 0x7d5898196ec0>(*(FakeTensor(..., size=(20, 10, 128)), FakeTensor(..., size=(20, 16, 128))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [20, 128] but got: [20, 16].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''