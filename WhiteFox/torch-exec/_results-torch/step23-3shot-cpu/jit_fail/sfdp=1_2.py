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
        self.dropout = torch.nn.Dropout(0.5)
        self.softmax = torch.nn.Softmax(dim=-1)

    def forward(self, query, key, value):
        qk = torch.matmul(query_tensor, key_tensor.transpose(-2, -1))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = self.softmax(scaled_qk)
        dropout_qk = self.dropout(softmax_qk)
        output = dropout_qk.matmul(value_tensor)
        return output


func = Model().to('cpu')


query = torch.randn(1, 3, 8, 8)

key = torch.randn(1, 3, 16, 16)

value = torch.randn(1, 3, 16, 16)

test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
name 'query_tensor' is not defined

jit:
NameError: name 'query_tensor' is not defined

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''