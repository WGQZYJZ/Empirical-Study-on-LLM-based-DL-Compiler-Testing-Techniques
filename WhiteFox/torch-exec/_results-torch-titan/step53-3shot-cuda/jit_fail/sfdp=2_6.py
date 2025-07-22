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

    def __init__(self, input_dim, output_dim, dropout_p):
        super().__init__()
        self.input_dim = input_dim

    def _make_linear(self, input_dim, output_dim, bias, dropout_p):
        return [torch.nn.Linear(input_dim, output_dim, bias=bias), torch.nn.Dropout(dropout_p)]

    def _make_attention(self, feature_dim, dropout_p):
        return [torch.nn.Linear(feature_dim, feature_dim), torch.nn.Tanh(), torch.nn.Linear(feature_dim, 1, bias=False), torch.nn.Dropout(dropout_p)]

    def forward(self, query, key, value, scale_factor):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        inv_scale_factor = (1.0 / scale_factor)
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output



input_dim = 1
output_dim = 1
dropout_p = 1

func = Model(input_dim, output_dim, dropout_p).to('cuda')



query = torch.randn(4, 10, 6)



key = torch.randn(5, 20, 6)



value = torch.randn(5, 20, 4)



scale_factor = torch.randn(1)


test_inputs = [query, key, value, scale_factor]

# JIT_FAIL
'''
direct:
The size of tensor a (4) must match the size of tensor b (5) at non-singleton dimension 0

jit:
Failed running call_function <built-in method matmul of type object at 0x79536ac699e0>(*(FakeTensor(..., device='cuda:0', size=(4, 10, 6)), FakeTensor(..., device='cuda:0', size=(5, 6, 20))), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''