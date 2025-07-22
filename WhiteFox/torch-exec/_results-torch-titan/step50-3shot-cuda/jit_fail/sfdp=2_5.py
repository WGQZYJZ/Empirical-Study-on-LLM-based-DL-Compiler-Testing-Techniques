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

    def __init__(self, query_dim, key_dim, value_dim, dropout_p=0):
        super().__init__()
        self.dropout = torch.nn.Dropout(dropout_p)
        weight = torch.Tensor(query_dim, key_dim)
        self.query_key_score = torch.nn.Parameter(torch.nn.init.uniform_(weight, (- 0.001), 0.001))

    def forward(self, query, key, value):
        inv_scale_factor = (torch.sqrt(query.size((- 1))) + torch.sqrt((key.size((- 1)) - query.size((- 1)))))
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = self.dropout(softmax_qk)
        output = dropout_qk.matmul(value)
        return output



query_dim = 1
key_dim = 1
value_dim = 1
func = Model(16, 64, 64).to('cuda')



query = torch.randn(1, 4, 16)



key = torch.randn(1, 4, 64)



value = torch.randn(1, 4, 64)


test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
sqrt(): argument 'input' (position 1) must be Tensor, not int

jit:
Failed running call_function <built-in method sqrt of type object at 0x7db4164699e0>(*(16,), **{}):
sqrt(): argument 'input' (position 1) must be Tensor, not int

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''