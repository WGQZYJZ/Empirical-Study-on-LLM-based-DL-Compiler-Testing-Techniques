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

    def __init__(self, m):
        super().__init__()
        self.m = m

    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        inv_scale_factor = math.sqrt((math.sqrt(query.shape[(- 1)]) / math.sqrt(key.shape[(- 1)])))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.5)
        output = dropout_qk.mm(value)
        return output




m = Model(torch.nn.Identity(5))

func = Model(torch.nn.Identity(5)).to('cuda')



query = torch.randn(1, 2, 5)



key = torch.randn(1, 4, 5)



value = torch.randn(1, 4, 7)


test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
self must be a matrix

jit:
Failed running call_method mm(*(FakeTensor(..., device='cuda:0', size=(1, 2, 4)), FakeTensor(..., device='cuda:0', size=(1, 4, 7))), **{}):
a must be 2D

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''