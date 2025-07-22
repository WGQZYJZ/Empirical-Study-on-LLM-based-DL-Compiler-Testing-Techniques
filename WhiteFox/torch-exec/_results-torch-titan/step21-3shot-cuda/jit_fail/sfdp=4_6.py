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

    def __init__(self, nHeads, queryDim, keyDim, valueDim):
        super().__init__()
        self.nHeads = nHeads
        self.query = torch.nn.Linear(queryDim, (nHeads * keyDim), bias=False)
        self.key = torch.nn.Linear(keyDim, (nHeads * keyDim), bias=False)
        self.value = torch.nn.Linear(valueDim, (nHeads * valueDim), bias=False)
        self.attn_mask = (torch.randn(3, keyDim, queryDim) * 1e-05)

    def forward(self, x1, x2):
        qk = ((self.query(x1) @ self.key(x2).transpose((- 2), (- 1))) / math.sqrt(x1.size((- 1))))
        qk = (qk + self.attn_mask)
        attn_weight = torch.softmax(qk, dim=(- 1))
        output = (attn_weight @ self.value(x2))
        return output



nHeads = 1
queryDim = 1
keyDim = 1
valueDim = 1

func = Model(nHeads, queryDim, keyDim, valueDim).to('cuda')



x1 = torch.randn(4, 24)



x2 = torch.randn(2, 3, 24)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (4x24 and 1x1)

jit:
Failed running call_module L__self___query(*(FakeTensor(..., device='cuda:0', size=(4, 24)),), **{}):
a and b must have same reduction dim, but got [4, 24] X [1, 1].

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''