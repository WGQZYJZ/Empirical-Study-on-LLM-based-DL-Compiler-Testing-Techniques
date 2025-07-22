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

    def __init__(self, N=64, D=2, H=2, dropout_p=0.2):
        super().__init__()
        self.qkv = torch.nn.Linear(D, ((D * H) * 3))
        self.softmax_kv = torch.nn.Softmax(dim=(- 1))
        self.dropout_kv = torch.nn.Dropout(dropout_p)
        self.final_linear = torch.nn.Linear((D * H), D)

    def forward(self, q, k, v, inv_scale_factor):
        qk = self.qkv(q)
        qk = qk.reshape(q.size(0), q.size(1), 3, int((qk.size(1) / 3)))
        q = qk.reshape((- 1), int((qk.size(1) / 3)))
        k = qk[:, :, 1, :]
        v = qk[:, :, 2, :]
        scaled_qk = (torch.matmul(q, k.transpose((- 2), (- 1))) / inv_scale_factor)
        softmax_qk = self.softmax_kv(scaled_qk)
        dropout_qk = self.dropout_kv(softmax_qk)
        output = torch.matmul(dropout_qk, v)
        output = output.reshape(q.size(0), q.size(1), output.size(1))
        output = output.reshape(q.size(0), output.size(1), 1, 1)
        output = self.final_linear(output)
        return output



func = Model().to('cuda')



D = 256


N = 8


q = torch.randn(N, D)



D = 256


N = 8


k = torch.randn(N, D)



D = 256


N = 8


v = torch.randn(N, D)

inv_scale_factor = 1

test_inputs = [q, k, v, inv_scale_factor]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (8x256 and 2x12)

jit:
Failed running call_module L__self___qkv(*(FakeTensor(..., device='cuda:0', size=(8, 256)),), **{}):
a and b must have same reduction dim, but got [8, 256] X [2, 12].

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''