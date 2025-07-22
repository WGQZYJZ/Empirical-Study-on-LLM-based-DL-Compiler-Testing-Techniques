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

    def forward(self, query, key, value, inv_scale_factor, dropout_p):
        v3 = torch.matmul(query, key.transpose((- 2), (- 1)))
        v5 = v3.div(inv_scale_factor)
        v6 = torch.nn.functional.dropout(v5, p=dropout_p)
        v7 = torch.matmul(v6, value)
        return v7



func = Model().to('cuda')

query = 1
key = 1
value = 1
inv_scale_factor = 1
dropout_p = 1

test_inputs = [query, key, value, inv_scale_factor, dropout_p]

# JIT_FAIL
'''
direct:
'int' object has no attribute 'transpose'

jit:
'int' object has no attribute 'transpose'

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''