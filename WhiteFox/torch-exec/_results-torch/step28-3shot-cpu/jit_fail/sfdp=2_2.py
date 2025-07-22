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
        self.dropout = torch.nn.Dropout(dropout_p)

    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1))
        v1 = inv_scale_factor * qk
        v2 = v1.softmax(dim=-1)
        v3 = self.dropout(v2)
        output = torch.matmul(v3, value)
        return output


func = Model().to('cpu')


key = torch.randn(1, 6, 64, 128)

value = torch.randn(1, 6, 64, 128)

query = torch.randn(1, 6, 64, 128)

test_inputs = [key, value, query]

# JIT_FAIL
'''
direct:
name 'inv_scale_factor' is not defined

jit:
NameError: name 'inv_scale_factor' is not defined

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''