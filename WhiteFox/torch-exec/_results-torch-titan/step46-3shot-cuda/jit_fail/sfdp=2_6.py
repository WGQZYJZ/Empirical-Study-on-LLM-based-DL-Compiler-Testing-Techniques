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

    def forward(self, a, b):
        q = (a @ b.T)
        sc = (q / 10)
        sm = torch.nn.functional.softmax(sc, dim=(- 1))
        dr = torch.nn.functional.dropout(sm, 0.2)
        out = (dr @ a)
        o = self.out(out)
        return o



func = Model().to('cuda')



a = torch.randn(1, 12, 32)



b = torch.randn(12, 32)


test_inputs = [a, b]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'out'

jit:
out

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''