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

    def forward(self, x, mask, xmask):
        inp = xmask
        xmask = 0
        for i in range(inp.size(0)):
            input = inp[i]
            result = inp.new_empty((inp.size(0), 3))
            z = result[i]
            result = z
            xmask = z
        return result



func = Model().to('cpu')


x = torch.randn((3, 2, 2), requires_grad=True)

xmask = torch.randn(3, requires_grad=True)
mask = 1

test_inputs = [x, xmask, mask]

# JIT_FAIL
'''
direct:
'int' object has no attribute 'size'

jit:
AttributeError: 'int' object has no attribute 'size'

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''