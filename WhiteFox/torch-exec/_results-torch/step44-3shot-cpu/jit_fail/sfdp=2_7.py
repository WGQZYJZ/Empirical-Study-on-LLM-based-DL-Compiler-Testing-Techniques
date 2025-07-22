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

    def __init__(self, num_heads):
        super().__init__()
        self.num_heads = num_heads

    def forward(self, query, key, value, training):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk * (1.0 / sqrt(self.num_heads))
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output


num_heads = 1

func = Model(num_heads).to('cpu')


query = torch.randn(1, 12, 128, 64)

key = torch.randn(1, 12, 128, 64)

value = torch.randn(1, 12, 128, 64)
training = 1

test_inputs = [query, key, value, training]

# JIT_FAIL
'''
direct:
name 'sqrt' is not defined

jit:
NameError: name 'sqrt' is not defined

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''