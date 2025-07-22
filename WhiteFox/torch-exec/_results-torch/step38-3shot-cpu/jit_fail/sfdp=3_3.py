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

    def forward(self, query, key, value=None, scale_factor=1.0, dropout_p=0.2):
        v1 = torch.matmul(query, key.transpose(-2, -1))
        v2 = v1 * 1
        v3 = v1.softmax(dim=_ - 1)
        v4 = F.dropout(v3, p=0.2)
        v5 = torch.matmul(v4, value)
        return v5


func = Model().to('cpu')


query = torch.randn(1, 3, 10, 10)

key = torch.randn(1, 3, 10, 10)

value = torch.randn(1, 3, 10, 10)

test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
name '_' is not defined

jit:
NameError: name '_' is not defined

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''