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

    def __init__(self, batch, num, dims, dropout):
        super().__init__()
        self.batch = batch
        self.num = num
        self.dims = dims
        self.dropout = dropout
        self.dropout_p = (dropout / (dims * num))
        self.qk = torch.nn.Linear(dims, dims, bias=False)
        self.v = torch.nn.Linear(dims, dims, bias=False)
        self.dropout_qk = torch.nn.Dropout(p=self.dropout_p)

    def forward(self, q, k, v, mask=None):
        qk = torch.matmul(q, k.transpose((- 1), (- 2)))
        scaled_qk = qk.div((self.batch ** 0.5))
        if (mask is not None):
            scaled_qk = scaled_qk.masked_fill((mask == 0), (- 10000000000.0))
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = self.dropout_qk(softmax_qk)
        o = torch.matmul(dropout_qk, v)
        return o




batch = 8


num = 6


dims = 512


dropout = 0.1


func = Model(batch, num, dims, dropout).to('cuda')



dims = 512


num = 6


batch = 8


q = torch.randn(batch, num, dims)



dims = 512


num = 6


batch = 8


k = torch.randn(batch, num, dims)



dims = 512


num = 6


batch = 8


v = torch.randn(batch, num, dims)


num = 6


batch = 8



mask = torch.randint(2, (batch, num))


test_inputs = [q, k, v, mask]

# JIT_FAIL
'''
direct:
The size of tensor a (8) must match the size of tensor b (6) at non-singleton dimension 1

jit:
Failed running call_method masked_fill(*(FakeTensor(..., device='cuda:0', size=(8, 6, 6)), FakeTensor(..., device='cuda:0', size=(8, 6), dtype=torch.bool), -10000000000.0), **{}):
Attempting to broadcast a dimension of length 6 at -2! Mismatching argument at index 1 had torch.Size([8, 6, 6]); but expected shape should be broadcastable to [1, 8, 6]

from user code:
   File "<string>", line 32, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''