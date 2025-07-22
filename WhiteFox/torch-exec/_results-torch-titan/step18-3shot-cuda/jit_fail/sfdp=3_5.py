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
        self.scale_factor = 1

    def forward(self, q, k, v):
        v1 = torch.matmul(q, k.transpose((- 2), (- 1)))
        v2 = (v1 * self.scale_factor)
        v3 = v2.softmax(dim=(- 1))
        v4 = torch.nn.functional.dropout(v3, p=0.2)
        v5 = torch.matmul(v4, v)
        return v5



func = Model().to('cuda')



q = torch.randn(1, 10, 16)

k = 1
v = 1

test_inputs = [q, k, v]

# JIT_FAIL
'''
direct:
'int' object has no attribute 'transpose'

jit:
'int' object has no attribute 'transpose'

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''