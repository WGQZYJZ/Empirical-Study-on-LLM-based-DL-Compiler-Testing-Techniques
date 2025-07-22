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

    def __init__(self, dim, dropout_p=0.2):
        super().__init__()
        self.dim = dim
        self.dropout_p = dropout_p
        self.softmax = nn.Softmax(dim=dim)
        self.dropout = nn.Dropout(dropout_p)

    def forward(self, query, key, value, inv_scale_factor=0.5):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = self.softmax(scaled_qk)
        dropout_qk = self.dropout(softmax_qk)
        output = dropout_qk.matmul(value)
        return output



dim = 1
func = Model(2048).to('cuda')



query = torch.randn(1, 10, 2048)



key = torch.randn(1, 25, 2048)



value = torch.randn(1, 25, 2048)


test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
Dimension out of range (expected to be in range of [-3, 2], but got 2048)

jit:
Failed running call_module L__self___softmax(*(FakeTensor(..., device='cuda:0', size=(1, 10, 25)),), **{}):
Dimension out of range (expected to be in range of [-3, 2], but got 2048)

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''