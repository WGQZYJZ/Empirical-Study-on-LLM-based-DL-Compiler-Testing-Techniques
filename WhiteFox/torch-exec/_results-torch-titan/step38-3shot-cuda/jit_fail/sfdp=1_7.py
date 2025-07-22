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

    def __init__(self, dim=128, n_heads=8, dropout_p=0.01, inv_scale_factor=1):
        super().__init__()
        self.head_dim = (dim // n_heads)
        self.scale = (self.head_dim ** (- 0.5))
        self.fc_0 = torch.nn.Linear(dim, dim)
        self.fc_1 = torch.nn.Linear(dim, dim, bias=False)
        self.fc_2 = torch.nn.Linear(dim, dim)
        self.fc_3 = torch.nn.Linear(dim, dim, bias=True)
        self.fc_3.bias = torch.nn.Parameter(torch.zeros(dim), requires_grad=False)

    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = qk.div(self.scale)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(value)
        return output



func = Model().to('cuda')



query = torch.randn(2, 16, 128)



key = torch.randn(2, 16, 128)



value = torch.randn(2, 16, 128)


test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'dropout_p'

jit:
dropout_p

from user code:
   File "<string>", line 31, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''