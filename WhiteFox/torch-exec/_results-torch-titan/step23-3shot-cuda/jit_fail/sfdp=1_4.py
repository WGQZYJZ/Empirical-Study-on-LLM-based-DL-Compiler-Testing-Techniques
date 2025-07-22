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

    def __init__(self, query_dim, key_dim, value_dim, dropout_p):
        super().__init__()
        self.query = torch.nn.Parameter(torch.randn(1, query_dim))
        self.key = torch.nn.Parameter(torch.randn(1, key_dim))
        self.value = torch.nn.Parameter(torch.randn(1, value_dim))
        self.dropout = 0.3

    def forward(self, x1, x2, inv_scale_factor):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output




query_dim = 128


key_dim = 128


value_dim = 512

dropout_p = 1

func = Model(query_dim, key_dim, value_dim, dropout_p).to('cuda')



query_dim = 128


x1 = torch.randn(1, 20, query_dim)



key_dim = 128


x2 = torch.randn(1, 30, key_dim)



query_dim = 128


inv_scale_factor = torch.randn(1, query_dim, 1)


test_inputs = [x1, x2, inv_scale_factor]

# JIT_FAIL
'''
direct:
name 'query' is not defined

jit:
name 'query' is not defined

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''