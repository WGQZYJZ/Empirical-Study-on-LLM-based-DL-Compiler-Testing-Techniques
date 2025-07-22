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

    def __init__(self, query_size, key_size):
        super().__init__()
        self.query = torch.nn.Parameter(torch.rand(query_size), requires_grad=True)
        self.key = torch.nn.Parameter(torch.rand(key_size), requires_grad=True)
        self.inv_scale_factor = math.sqrt(key_size)

    def forward(self, value, dropout_p):
        qk = torch.matmul(self.query, self.key.transpose((- 2), (- 1)))
        scaled_qk = (qk / self.inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output




query_size = 256


key_size = 64

func = Model(query_size, key_size).to('cuda')


key_size = 64



value = torch.randn(1, 32, (key_size * 2))

dropout_p = 1

test_inputs = [value, dropout_p]

# JIT_FAIL
'''
direct:
Dimension out of range (expected to be in range of [-1, 0], but got -2)

jit:
Failed running call_method transpose(*(Parameter(FakeTensor(..., device='cuda:0', size=(64,), requires_grad=True)), -2, -1), **{}):
Dimension out of range (expected to be in range of [-1, 0], but got -2)

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''