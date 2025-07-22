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
        self.w_q = torch.nn.Linear(64, (64 * self.num_heads))
        self.w_k = torch.nn.Linear(64, (64 * self.num_heads))
        self.w_v = torch.nn.Linear(64, (64 * self.num_heads))
        self.dropout_1 = torch.nn.Dropout(p=0.2)

    def forward(self, q, k, v):
        self.q = self.w_q(q)
        self.k = self.w_k(k)
        self.v = self.w_v(v)
        self.transpose_q = self.q.transpose(dim0=2, dim1=3)
        self.transpose_k = self.k.transpose(dim0=2, dim1=3)
        self.transpose_v = self.v.transpose(dim0=2, dim1=3)
        self.softmax_qk = torch.softmax((torch.matmul(self.transpose_q, self.transpose_k.transpose(0, 1)) / math.sqrt(64)), dim=(- 1))
        self.dropout_qk = self.dropout_1(self.softmax_qk)
        self.dropout_v = self.dropout_qk.matmul(self.transpose_v)
        return self.dropout_v.transpose(dim0=2, dim1=3)



num_heads = 1

func = Model(num_heads).to('cuda')



q = torch.randn(10, 30, 64)



k = torch.randn(8, 20, 64)



v = torch.randn(12, 20, 64)


test_inputs = [q, k, v]

# JIT_FAIL
'''
direct:
Dimension out of range (expected to be in range of [-3, 2], but got 3)

jit:
Failed running call_method transpose(*(FakeTensor(..., device='cuda:0', size=(10, 30, 64)),), **{'dim0': 2, 'dim1': 3}):
Dimension out of range (expected to be in range of [-3, 2], but got 3)

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''