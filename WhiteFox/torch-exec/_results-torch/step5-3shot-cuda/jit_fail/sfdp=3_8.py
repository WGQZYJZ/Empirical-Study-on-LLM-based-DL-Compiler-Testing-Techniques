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

    def forward(self, query, key, value, scale_factor, dropout_p, input_mask=None):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        if input_mask is not None:
            softmax_qk = softmax_qk.masked_fill(input_mask.unsqueeze(-1), float('-inf'))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output


func = Model().to('cuda')


query = torch.randn(2, 8, 512)

key = torch.randn(2, 8, 512)

value = torch.randn(2, 8, 512)

input_mask = torch.Tensor([[True, False, False], [True, True, False]])
scale_factor = 1
dropout_p = 1

test_inputs = [query, key, value, input_mask, scale_factor, dropout_p]

# JIT_FAIL
'''
direct:
The size of tensor a (8) must match the size of tensor b (3) at non-singleton dimension 2

jit:
Failed running call_method mul(*(FakeTensor(..., device='cuda:0', size=(s0, s4, s1)), FakeTensor(..., device='cuda:0', size=(s6, s7))), **{}):
The size of tensor a (s1) must match the size of tensor b (s7) at non-singleton dimension 2)

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''