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
        self.softmax = torch.nn.Softmax()

    def forward(self, query, key, scale_factor, dropout_p, value):
        v1 = torch.matmul(query, key.transpose((- 2), (- 1)))
        v2 = (v1 * scale_factor)
        v3 = self.softmax(v2, dim=(- 1))
        v4 = torch.dropout(v3, p=dropout_p)
        output = torch.matmul(v4, value)
        return v4



func = Model().to('cuda')



query = key = scale_factor = dropout_p = value = torch.randn(6, 5, 7)

key = 1
scale_factor = 1
dropout_p = 1
value = 1

test_inputs = [query, key, scale_factor, dropout_p, value]

# JIT_FAIL
'''
direct:
'int' object has no attribute 'transpose'

jit:
'int' object has no attribute 'transpose'

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''