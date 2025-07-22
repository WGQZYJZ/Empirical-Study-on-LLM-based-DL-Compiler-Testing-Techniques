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
        self.softmax = torch.nn.Softmax(dim=-1)

    def forward(self, qkv):
        (q, kv) = torch.split(qkv, [8, 16])
        qk = torch.matmul(q, kv.transpose(-2, -1))
        inv_scale_factor = torch.rsqrt((q * q).sum(dim=-1, keepdim=True) + 1e-12)
        scaled_qk = qk * inv_scale_factor
        softmax_qk = self.softmax(scaled_qk)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.1)
        return dropout_qk


func = Model().to('cpu')


qkv = torch.randn(1, 32, 8)

test_inputs = [qkv]

# JIT_FAIL
'''
direct:
split_with_sizes expects split_sizes to sum exactly to 1 (input tensor's size at dimension 0), but got split_sizes=[8, 16]

jit:
Failed running call_function <function split at 0x78728457bf70>(*(FakeTensor(..., size=(1, 32, 8)), [8, 16]), **{}):
Split sizes add up to 24 but got the tensor's size of 1

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''