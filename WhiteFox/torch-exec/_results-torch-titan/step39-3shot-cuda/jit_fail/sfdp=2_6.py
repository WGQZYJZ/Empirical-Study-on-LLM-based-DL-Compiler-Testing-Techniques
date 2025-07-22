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



class SelfAttention(torch.nn.Module):

    def __init__(self, num_heads: int, d_model: int):
        super().__init__()
        self.num_heads = num_heads
        self.key = torch.nn.Linear(d_model, d_model)
        self.query = torch.nn.Linear(d_model, d_model)
        self.value = torch.nn.Linear(d_model, d_model)
        self.dropout = torch.nn.Dropout(p=0.5)

    def forward(self, x1):
        key = self.key(x1)
        query = self.query(x1)
        value = self.value(x1)
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        softmax_qk = qk.softmax(dim=(- 1))
        dropout_qk = self.dropout(softmax_qk)
        output = torch.matmul(dropout_qk, value)
        output = output.permute(0, 2, 1, 3).contiguous().view(output.shape[0], (- 1), output.shape[(- 1)])
        return output




class Model(torch.nn.Module):

    def __init__(self, num_heads: int=8, d_model: int=64):
        super().__init__()
        self.encoder = SelfAttention(num_heads=num_heads, d_model=d_model)
        self.linear = torch.nn.Linear(d_model, 2)

    def forward(self, x1):
        v1 = x1.reshape((- 1), x1.shape[(- 1)])
        v2 = self.encoder(v1)
        v3 = self.linear(v2)
        return v3




func = Model().to('cuda')

x1 = 1

test_inputs = [x1]

# JIT_FAIL
'''
direct:
'int' object has no attribute 'reshape'

jit:
'int' object has no attribute 'reshape'

from user code:
   File "<string>", line 47, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''