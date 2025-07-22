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
        super(Model, self).__init__()
        self.num_heads = num_heads

    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1))
        inv_scale_factor = 1.0 / math.sqrt(math.sqrt(self.num_heads))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_pk = torch.nn.functional.dropout(softmax_qk, p=0.5)
        output = dropout_qk.matmul(value)
        return output


num_heads = 1

func = Model(num_heads).to('cpu')


shape = (16, 128)
query = torch.randn(shape)

shape = (16, 128)
key = torch.randn(shape)

shape = (16, 128)
value = torch.randn(shape)

test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
name 'dropout_qk' is not defined

jit:
NameError: name 'dropout_qk' is not defined

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''