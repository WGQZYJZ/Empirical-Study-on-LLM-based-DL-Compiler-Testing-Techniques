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

class Model2(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 3, 3)

    def forward(self, x1):
        x2 = self.conv(x)
        y = torch.add(x2, x2)
        s = x2.size(1)
        y = torch.split(y, s)
        return y[0] + y[1]



func = Model2().to('cpu')


x1 = torch.randn(1, 3, 4, 4)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
name 'x' is not defined

jit:
NameError: name 'x' is not defined

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''