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

    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.n1 = negative_slope

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 > 0)
        v3 = (v1 * self.n1)
        v4 = torch.where(v2, v1, v3)
        return v4



func = Model().to('cuda')



x1 = torch.randn(3, 10)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'linear'

jit:
linear

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''