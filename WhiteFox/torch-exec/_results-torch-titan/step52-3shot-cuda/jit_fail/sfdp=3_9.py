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
        super(Model, self).__init__()
        self.query = torch.nn.Linear(256, 256)
        self.key = torch.nn.Linear(32, 256)
        self.value = torch.nn.Linear(256, 64)
        self.dropout = torch.nn.Dropout(p=0.2)

    def forward(self, q, k, v):
        q = self.query(q)
        k = self.key(k)
        v = self.value(v)
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        scaled_qk = qk.mul((1.0 / math.sqrt(q.size((- 1)))))
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = self.dropout(softmax_qk)
        output = torch.matmul(dropout_qk, v)
        return output



func = Model().to('cuda')



q = torch.randn(1, 256, 1)



k = torch.randn(1, 32, 1)



v = torch.randn(1, 256, 1)


test_inputs = [q, k, v]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (256x1 and 256x256)

jit:
Failed running call_module L__self___query(*(FakeTensor(..., device='cuda:0', size=(1, 256, 1)),), **{}):
a and b must have same reduction dim, but got [256, 1] X [256, 256].

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''