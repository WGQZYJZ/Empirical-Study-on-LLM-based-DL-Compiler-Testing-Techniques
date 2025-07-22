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

    def __init__(self, dim, dropout_p=0.2):
        super().__init__()
        self.dim = dim
        self.dropout_p = dropout_p
        self.softmax = nn.Softmax(dim=dim)
        self.dropout = nn.Dropout(dropout_p)

    def forward(self, query, key, value, inv_scale_factor=0.5):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = self.softmax(scaled_qk)
        dropout_qk = self.dropout(softmax_qk)
        output = dropout_qk.matmul(value)
        return output


dim = 1
func = Model(2048).to('cpu')


query = torch.randn(1, 10, 2048)

key = torch.randn(1, 25, 2048)

value = torch.randn(1, 25, 2048)

test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
Dimension out of range (expected to be in range of [-3, 2], but got 2048)

jit:
Failed running call_function <function softmax at 0x7105ee7eb700>(*(FakeTensor(..., size=(1, 10, 25)), 2048), **{'_stacklevel': 5}):
Dimension out of range (expected to be in range of [-3, 2], but got 2048)

from user code:
   File "<string>", line 25, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/activation.py", line 1672, in forward
    return F.softmax(input, self.dim, _stacklevel=5)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''