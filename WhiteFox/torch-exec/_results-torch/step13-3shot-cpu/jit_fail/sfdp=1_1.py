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

    def __init__(self, dim_k):
        super().__init__()
        self.dropout = torch.nn.Dropout(p=0.2)

    def forward(self, query, key, value, inv_scale_factor):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = self.dropout(softmax_qk)
        output = dropout_qk.matmul(value)
        return output


dim_k = 1

func = Model(dim_k).to('cpu')


query = torch.randn(1, 2, 10)

key = torch.randn(1, 5, 2)

value = torch.randn(1, 5, 10)

inv_scale_factor = torch.randn(1, 2, 10)

test_inputs = [query, key, value, inv_scale_factor]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 10] but got: [1, 2].

jit:
Failed running call_function <built-in method matmul of type object at 0x743628f96ec0>(*(FakeTensor(..., size=(1, 2, 10)), FakeTensor(..., size=(1, 2, 5))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 10] but got: [1, 2].

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''