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
        self.query = torch.nn.Linear(1, 1)
        self.key = torch.nn.Linear(1, 1)
        self.value = torch.nn.Linear(1, 2)

    def forward(self, x1, x2):
        q = self.query(x1)
        k = self.key(x2)
        v = self.value(x2)
        inv_scale_factor = np.sqrt(q.numel())
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = torch.softmax(scaled_qk, dim=(- 1))
        dropout_p = 0.5
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        o1 = dropout_qk.matmul(v)
        return o1



func = Model().to('cuda')



x1 = torch.randn(128, 3, 16, 16)



x2 = torch.randn(128, 3, 16, 16)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (6144x16 and 1x1)

jit:
Failed running call_module L__self___query(*(FakeTensor(..., device='cuda:0', size=(128, 3, 16, 16)),), **{}):
a and b must have same reduction dim, but got [6144, 16] X [1, 1].

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''