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

    def __init__(self, scale_factor, dropout_p):
        super().__init__()
        self.dropout_p = dropout_p

    def forward(self, q, k, v):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output


scale_factor = 1
dropout_p = 1

func = Model(scale_factor, dropout_p).to('cpu')


query = torch.randn(4, 3, 64, 64)

key = torch.randn(4, 3, 64, 64)
q = 1

test_inputs = [query, key, q]

# JIT_FAIL
'''
direct:
name 'value' is not defined

jit:
NameError: name 'value' is not defined

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''