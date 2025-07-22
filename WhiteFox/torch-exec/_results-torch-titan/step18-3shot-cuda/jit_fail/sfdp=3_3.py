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

    def __init__(self, num_heads=8, d_model=26, dropout_rate=0.0):
        super().__init__()
        self.attn_qk = torch.nn.Linear(d_model, num_heads)
        self.v = torch.nn.Linear(d_model, d_model)
        self.dropout = torch.nn.Dropout(dropout_rate)

    def forward(self, query, key, value):
        qk = (self.attn_qk(query) * self.attn_qk(key))
        scale_factor = torch.sqrt(torch.Tensor([query.shape[(- 1)]]))
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = self.dropout(softmax_qk)
        output = self.v(dropout_qk.matmul(value))
        return output



func = Model(num_heads=2, d_model=4, dropout_rate=0.0).to('cuda')



query = torch.randn(2, 4)



key = torch.randn(2, 4)



value = torch.randn(2, 4)


test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu!

jit:
Failed running call_method mul(*(FakeTensor(..., device='cuda:0', size=(2, 2)), FakeTensor(..., size=(1,))), **{}):
Unhandled FakeTensor Device Propagation for aten.mul.Tensor, found two different devices cuda:0, cpu

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''