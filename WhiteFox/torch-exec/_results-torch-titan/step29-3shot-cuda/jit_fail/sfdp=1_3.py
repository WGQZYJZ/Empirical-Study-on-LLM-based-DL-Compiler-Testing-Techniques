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

    def __init__(self, query_size, key_size, value_size, dropout_p, scale_factor):
        super().__init__()
        self.dropout = torch.nn.Dropout(p=dropout_p)
        self.softmax = torch.nn.Softmax(dim=(- 1))
        self.scale_factor = scale_factor
        self.qk_projection = torch.nn.Linear(query_size, key_size)
        self.v_projection = torch.nn.Linear(value_size, key_size)

    def forward(self, query, key, value):
        qk = self.qk_projection(query).matmul(self.v_projection(key).transpose((- 2), (- 1)))
        scale_qk = (qk / self.scale_factor)
        soft_qk = self.softmax(scale_qk)
        dropout_qk = self.dropout(soft_qk)
        return dropout_qk.matmul(value)



query_size = 1
key_size = 1
value_size = 1

dropout_p = 0.8


scale_factor = 1.2


func = Model(query_size, key_size, value_size, dropout_p, scale_factor).to('cuda')



query = torch.randn(32, 128)



key = torch.randn(32, 256)



value = torch.randn(32, 512)


test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (32x128 and 1x1)

jit:
Failed running call_module L__self___qk_projection(*(FakeTensor(..., device='cuda:0', size=(32, 128)),), **{}):
a and b must have same reduction dim, but got [32, 128] X [1, 1].

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''