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

    def __init__(self, *, n_heads, head_size):
        super().__init__()
        self.n_heads = n_heads
        self.head_size = head_size
        self.scale_factor = (head_size ** (- 0.5))

    def forward(self, query, key, value, dropout_p):
        shape = query.size()[:(- 1)]
        qk = query.view((shape + (self.n_heads, self.head_size))).matmul(key.transpose((- 2), (- 1)).contiguous().view((shape + (self.n_heads, self.head_size))).transpose((- 1), (- 2)))
        qk = qk.mul(self.scale_factor)
        softmax_qk = qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        return dropout_qk.matmul(value.view((shape + (self.n_heads, self.head_size))).permute((0, 2, 1, 3))).view((shape + ((self.n_heads * self.head_size),)))



func = Model(n_heads=8, head_size=16).to('cuda')



query = torch.randn(1, 3, 64, 64)



key = torch.randn(1, 3, 64, 64)



value = torch.randn(1, 3, 64, 64)

dropout_p = 1

test_inputs = [query, key, value, dropout_p]

# JIT_FAIL
'''
direct:
shape '[1, 3, 64, 8, 16]' is invalid for input of size 12288

jit:
Failed running call_method view(*(FakeTensor(..., device='cuda:0', size=(1, 3, 64, 64)), (1, 3, 64, 8, 16)), **{}):
shape '[1, 3, 64, 8, 16]' is invalid for input of size 12288

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''