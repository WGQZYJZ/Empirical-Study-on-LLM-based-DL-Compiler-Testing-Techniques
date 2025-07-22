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

    def __init__(self, dropout_p=0.1, inv_scale_factor=1.0 / 64):
        super().__init__()

    def forward(self, query, key, value):
        softmax_qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = softmax_qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output


func = Model().to('cpu')


query = torch.randn(1, 3, 64, 64)

key = torch.randn(1, 3, 64, 64)

value = torch.randn(1, 3, 64, 64)

test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
name 'inv_scale_factor' is not defined

jit:
NameError: name 'inv_scale_factor' is not defined

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''