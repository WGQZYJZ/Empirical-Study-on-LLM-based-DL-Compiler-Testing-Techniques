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

    def forward(self, q, k, v, query_mask, key_padding_mask):
        scale_factor = 1 + key_padding_mask.max(dim=-1, keepdim=True).values.abs()
        scaled_qk = torch.matmul(q, k.transpose(-2, -1)) / scale_factor.unsqueeze(-1)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = torch.matmul(dropout_qk, v)
        return output


func = Model().to('cpu')


q = torch.randn(1, 8, 1, 8)

k = torch.randn(1, 8, 2, 8)

v = torch.randn(1, 8, 2, 8)

query_mask = torch.zeros(1, 8, 1, 1)

key_padding_mask = torch.ones(1, 8, 2, 1)

test_inputs = [q, k, v, query_mask, key_padding_mask]

# JIT_FAIL
'''
direct:
The size of tensor a (8) must match the size of tensor b (2) at non-singleton dimension 2

jit:
Failed running call_function <built-in function truediv>(*(FakeTensor(..., size=(1, 8, 1, 2)), FakeTensor(..., size=(1, 8, 2, 1, 1))), **{}):
Attempting to broadcast a dimension of length 2 at -3! Mismatching argument at index 1 had torch.Size([1, 8, 2, 1, 1]); but expected shape should be broadcastable to [1, 1, 8, 1, 2]

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''