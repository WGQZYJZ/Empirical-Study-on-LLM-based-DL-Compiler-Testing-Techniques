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

    def __init__(self, query_size, key_size, val_size, dropout_p=0.1):
        super().__init__()
        self.key = torch.nn.Linear(query_size, key_size, bias=False)
        self.value = torch.nn.Linear(query_size, val_size, bias=False)
        self.inv_scale_factor = torch.sqrt(torch.FloatTensor([key_size])).cuda()
        self.dropout_p = dropout_p

    def forward(self, query1, query2):
        k = self.key(query1)
        v = self.key(query2)
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output


query_size = 1
key_size = 1
val_size = 1

func = Model(query_size, key_size, val_size).to('cpu')


query1 = torch.randn(1, 128)

query2 = torch.randn(32, 128)

test_inputs = [query1, query2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x128 and 1x1)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 128)), Parameter(FakeTensor(..., size=(1, 1), requires_grad=True)), None), **{}):
a and b must have same reduction dim, but got [1, 128] X [1, 1].

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''