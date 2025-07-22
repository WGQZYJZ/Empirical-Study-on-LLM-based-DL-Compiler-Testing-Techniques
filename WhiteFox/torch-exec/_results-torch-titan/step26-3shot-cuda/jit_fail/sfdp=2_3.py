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

    def forward(self, x1, x2, x3, x4, x5, x6, x7, x8):
        a1 = torch.matmul(x1, x2.transpose((- 2), (- 1)))
        b1 = (a1 / x3)
        c1 = torch.nn.functional.dropout(b1, x4, training=True)
        d1 = torch.matmul(c1, x5)
        b2 = d1.add(x6)
        c2 = torch.nn.functional.gelu(b2)
        f1 = torch.matmul(c2, x7)
        h1 = torch.nn.functional.dropout(f1, x8, training=True)
        g1 = torch.sigmoid(h1)
        return g1




func = Model().to('cuda')

x1 = 1
x2 = 1
x3 = 1
x4 = 1
x5 = 1
x6 = 1
x7 = 1
x8 = 1

test_inputs = [x1, x2, x3, x4, x5, x6, x7, x8]

# JIT_FAIL
'''
direct:
'int' object has no attribute 'transpose'

jit:
'int' object has no attribute 'transpose'

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''