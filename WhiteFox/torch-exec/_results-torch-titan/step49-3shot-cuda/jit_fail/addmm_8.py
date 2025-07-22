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
        r = torch.randn(3, 3)

    def forward(self, x1, x2, inp):
        r1 = (x1 - r)
        inp = (r1 - inp)
        v1 = torch.mm(inp, r1)
        v2 = (v1 + x2)
        return v2




func = Model().to('cuda')



x1 = torch.randn(3, 3, requires_grad=True)



x2 = torch.randn(3, 3)



inp = torch.randn(3, 3, requires_grad=True)


test_inputs = [x1, x2, inp]

# JIT_FAIL
'''
direct:
name 'r' is not defined

jit:
name 'r' is not defined

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''