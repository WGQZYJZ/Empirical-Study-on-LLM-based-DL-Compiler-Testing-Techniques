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

    def __init__(self, input_size, hidden_size=32):
        super(Model, self).__init__()
        self.query = torch.nn.Linear(input_size, hidden_size)
        self.key = torch.nn.Linear(input_size, hidden_size)
        self.value = torch.nn.Linear(input_size, hidden_size)

    def forward(self, query, key, value, dropout_p=0.5, inv_scale_factor=1.0):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk / inv_scale_factor
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output


input_size = 1

func = Model(input_size).to('cpu')


query = torch.randn(1, 2, 4, 4)

key = torch.randn(1, 2, 8, 8)

value = torch.randn(1, 2, 8, 8)

test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [2, 4] but got: [2, 8].

jit:
Failed running call_function <built-in method matmul of type object at 0x71a34cd96ec0>(*(FakeTensor(..., size=(1, 2, 4, 4)), FakeTensor(..., size=(1, 2, 8, 8))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [2, 4] but got: [2, 8].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''