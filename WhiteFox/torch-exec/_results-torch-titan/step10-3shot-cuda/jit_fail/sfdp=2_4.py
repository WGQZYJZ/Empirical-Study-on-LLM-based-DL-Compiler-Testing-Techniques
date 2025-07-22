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

    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout(p=0.1, inplace=False)

    def forward(self, q, k, v, inv_scale_factor, dropout_p):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = self.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output



func = Model().to('cuda')



q = torch.randn(1, 3, 64, 64)



k = torch.randn(1, 6, 64, 64)



v = torch.randn(1, 6, 64, 64)

inv_scale_factor = 1
dropout_p = 1

test_inputs = [q, k, v, inv_scale_factor, dropout_p]

# JIT_FAIL
'''
direct:
forward() got an unexpected keyword argument 'p'

jit:
Failed running call_module L__self___dropout(*(FakeTensor(..., size=(1, 50, 32, 32)),), **{'p': 1}):
forward() got an unexpected keyword argument 'p'

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''