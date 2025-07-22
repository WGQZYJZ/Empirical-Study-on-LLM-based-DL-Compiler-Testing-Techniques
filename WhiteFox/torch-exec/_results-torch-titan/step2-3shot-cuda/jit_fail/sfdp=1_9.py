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

    def __init__(self, dim_head, num_heads, dropout_p):
        super().__init__()
        self.scale = (dim_head ** (- 0.5))
        self.query = torch.nn.Linear(1024, (dim_head * num_heads))
        self.key = torch.nn.Linear(1024, (dim_head * num_heads))
        self.value = torch.nn.Linear(1024, (dim_head * num_heads))
        self.dropout_p = dropout_p

    def forward(self, x1):
        qk = self.query(x1)
        qk = self.key(qk)
        qk_scaled = (qk * self.scale).softmax(dim=(- 1))
        return qk_scaled.matmul(value)



dim_head = 1
num_heads = 1
dropout_p = 1

func = Model(dim_head, num_heads, dropout_p).to('cuda')



x1 = torch.randn(1, 1024)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x1 and 1024x1)

jit:
Failed running call_module L__self___key(*(FakeTensor(..., device='cuda:0', size=(1, 1)),), **{}):
a and b must have same reduction dim, but got [1, 1] X [1024, 1].

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''