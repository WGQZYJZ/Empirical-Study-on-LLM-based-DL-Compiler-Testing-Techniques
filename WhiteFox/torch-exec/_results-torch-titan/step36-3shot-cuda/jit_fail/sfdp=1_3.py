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
        self.dot = torch.nn.Linear(127, 64)

    def forward(self, x1, x2):
        query = x1
        key = x2
        v1 = self.dot(query)
        v2 = self.dot(key)
        v3 = torch.matmul(v1, v2.transpose((- 2), (- 1)))
        inv_scale_factor = (1 / math.sqrt(v3.shape[(- 1)]))
        v4 = v3.div(inv_scale_factor)
        v5 = v4.softmax(dim=(- 1))
        dropout_p = 0.01
        v6 = torch.nn.functional.dropout(v5, p=dropout_p)
        value = x2
        v7 = torch.matmul(v6, value)
        return v7



func = Model().to('cuda')



x1 = torch.randn(1, 128, 127)



x2 = torch.randn(1, 128, 64)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (128x64 and 127x64)

jit:
Failed running call_module L__self___dot(*(FakeTensor(..., device='cuda:0', size=(1, 128, 64)),), **{}):
a and b must have same reduction dim, but got [128, 64] X [127, 64].

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''