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

    def forward(self, x1, inp):
        v1 = torch.mm(x1, x1)
        v1 = v1 + inp
        return v2



func = Model().to('cpu')


x1 = torch.randn(3, 3)

inp = torch.randn(3, 3)

test_inputs = [x1, inp]

# JIT_FAIL
'''
direct:
name 'v2' is not defined

jit:
NameError: name 'v2' is not defined

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''