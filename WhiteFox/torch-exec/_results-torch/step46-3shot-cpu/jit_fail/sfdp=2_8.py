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

class Model_2(torch.nn.Module):

    def __init__(self, num_heads, head_size, dropout_p):
        super().__init__()
        self.num_heads = num_heads
        self.head_size = head_size
        self.dropout_p = dropout_p

    def forward(self, query, key, value, inv_scale_factor):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(value)
        return output


num_heads = 4
head_size = 32
dropout_p = 0.5
func = Model_2(num_heads, head_size, dropout_p).to('cpu')

d_model = [4096, 4096, 4096, 4096]

head_size = 32
x1 = torch.randn(2, d_model[0], head_size)
d_model = [4096, 4096, 4096, 4096]

head_size = 32
x2 = torch.randn(2, d_model[1], head_size)
d_model = [4096, 4096, 4096, 4096]

head_size = 32
x3 = torch.randn(2, d_model[2], head_size)
d_model = [4096, 4096, 4096, 4096]
num_heads = 4

inv_scale_factor = torch.tensor([d_model[0]] * num_heads)

test_inputs = [x1, x2, x3, inv_scale_factor]

# JIT_FAIL
'''
direct:
The size of tensor a (4096) must match the size of tensor b (4) at non-singleton dimension 2

jit:
Failed running call_method div(*(FakeTensor(..., size=(2, 4096, 4096)), FakeTensor(..., size=(4,), dtype=torch.int64)), **{}):
Attempting to broadcast a dimension of length 4 at -1! Mismatching argument at index 1 had torch.Size([4]); but expected shape should be broadcastable to [2, 4096, 4096]

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''