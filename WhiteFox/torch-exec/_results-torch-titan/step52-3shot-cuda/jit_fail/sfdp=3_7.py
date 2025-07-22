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
        self.dim = 32
        self.num_heads = 4
        self.scale_factor = ((self.dim // self.num_heads) ** (- 0.5))
        self.q_linear = torch.nn.Linear(self.dim, self.dim)
        self.k_linear = torch.nn.Linear(self.dim, self.dim)
        self.v_linear = torch.nn.Linear(self.dim, self.dim)

    def forward(self, x):
        q = self.q_linear(x)
        k = self.k_linear(x)
        v = self.v_linear(x)
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        scaled_qk = (self.scale_factor * qk)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.1, training=True)
        output = torch.matmul(dropout_qk, v)
        return output



func = Model().to('cuda')



x = torch.randn(1, 32, 128)


test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (32x128 and 32x32)

jit:
Failed running call_module L__self___q_linear(*(FakeTensor(..., device='cuda:0', size=(1, 32, 128)),), **{}):
a and b must have same reduction dim, but got [32, 128] X [32, 32].

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''