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



class Model(nn.Module):

    def __init__(self, dropout_p):
        super().__init__()
        self.dropout_p = dropout_p

    def forward(self, q, k, v, scale_factor):
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        inv_scale_factor = scale_factor.pow((- 1))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(v)
        return output




dropout_p = 0.3

func = Model(dropout_p).to('cuda')



q = torch.randn(32, 10, 64)



k = torch.randn(32, 16, 64)



v = torch.randn(32, 16, 64)



scale_factor = torch.randint(low=1, high=256, size=[32, 1])


test_inputs = [q, k, v, scale_factor]

# JIT_FAIL
'''
direct:
Integers to negative integer powers are not allowed.

jit:
Failed running call_method div(*(FakeTensor(..., device='cuda:0', size=(32, 10, 16)), FakeTensor(..., device='cuda:0', size=(32, 1), dtype=torch.int64)), **{}):
Attempting to broadcast a dimension of length 32 at -2! Mismatching argument at index 1 had torch.Size([32, 1]); but expected shape should be broadcastable to [32, 10, 16]

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''