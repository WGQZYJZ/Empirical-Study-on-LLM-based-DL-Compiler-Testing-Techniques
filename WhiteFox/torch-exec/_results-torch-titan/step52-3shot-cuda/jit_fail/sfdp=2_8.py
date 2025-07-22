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



class Attention(torch.nn.Module):

    def __init__(self, query_size, key_size, value_size, dropout_p):
        super().__init__()
        self.query = torch.nn.Parameter(torch.randn(query_size, key_size))
        self.dropout_p = dropout_p

    def forward(self, query, key, value, mask=None, training=False):
        key_dim = key.size((- 1))
        inv_scale_factor = (key_dim ** (- 0.5))
        query = self.query.expand_as(query)
        key = self.query.expand_as(key)
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p, training=training)
        output = dropout_qk.matmul(value)
        return output



query_size = 1
key_size = 1
value_size = 1
dropout_p = 1
func = Attention(1024, 1024, 1024, 0.3).to('cuda')



query = torch.randn(32, 1024, 1)



key = torch.randn(32, 1024, 100)



value = torch.randn(32, 1024, 100)


test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
The expanded size of the tensor (1) must match the existing size (1024) at non-singleton dimension 2.  Target sizes: [32, 1024, 1].  Tensor sizes: [1024, 1024]

jit:
Failed running call_method expand_as(*(Parameter(FakeTensor(..., device='cuda:0', size=(1024, 1024), requires_grad=True)), FakeTensor(..., device='cuda:0', size=(32, 1024, 1))), **{}):
expand: attempting to expand a dimension of length 1024!

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''