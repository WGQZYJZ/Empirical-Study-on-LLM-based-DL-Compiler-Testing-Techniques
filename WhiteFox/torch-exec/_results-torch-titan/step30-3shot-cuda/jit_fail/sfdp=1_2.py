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

    def __init__(self, query_size, key_size, value_size, scale_factor=1, droput_p=0.1):
        super().__init__()
        self.scale_factor = scale_factor
        self.dropout_p = droput_p
        self.query = torch.nn.Linear(query_size, key_size, bias=False)
        self.key = torch.nn.Linear(key_size, query_size, bias=False)
        self.value = torch.nn.Linear(value_size, query_size)

    def forward(self, x1, x2, x3, dropout_p=None):
        if (dropout_p == None):
            dropout_p = self.dropout_p
        q = self.query(x1)
        k = self.key(x2)
        v = self.value(x3)
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        scaled_qk = qk.div(self.scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v)
        return (output, softmax_qk)



query_size = 1
key_size = 1
value_size = 1

func = Model(query_size, key_size, value_size).to('cuda')



x1 = torch.randn(5, 13)



x2 = torch.randn(10, 17)



x3 = torch.randn(13, 23)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (5x13 and 1x1)

jit:
Failed running call_module L__self___query(*(FakeTensor(..., device='cuda:0', size=(5, 13)),), **{}):
a and b must have same reduction dim, but got [5, 13] X [1, 1].

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''