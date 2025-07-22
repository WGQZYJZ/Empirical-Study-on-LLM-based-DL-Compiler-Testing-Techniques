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
        self.q = torch.nn.Linear(128, 288)
        self.k = torch.nn.Linear(13, 288)
        self.v = torch.nn.Linear(13, 288)

    def forward(self, q, k, v, mask):
        q = self.q(q)
        k = self.k(k)
        v = self.v(v)
        qk = ((q @ k.transpose((- 2), (- 1))) / math.sqrt(288))
        qk = (qk + mask)
        attn = torch.softmax(qk, dim=(- 1))
        output = (attn @ v)
        return output



func = Model().to('cuda')



q = torch.randn(1, 128)



k = torch.randn(1, 13)



v = torch.randn(1, 13)



mask = torch.randn(1, 1, 13)


test_inputs = [q, k, v, mask]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x13 and 1x288)

jit:
Failed running call_function <built-in function matmul>(*(FakeTensor(..., device='cuda:0', size=(1, 1, 13)), FakeTensor(..., device='cuda:0', size=(1, 288))), **{}):
a and b must have same reduction dim, but got [1, 13] X [1, 288].

from user code:
   File "<string>", line 30, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''