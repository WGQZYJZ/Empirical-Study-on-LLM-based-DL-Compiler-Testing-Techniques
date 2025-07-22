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
        self.input = torch.nn.quantized.FloatFunctional()
        self.linear = torch.nn.Linear(8, 8)
        self.sigmoid = torch.nn.Sigmoid()

    def forward(self, x1):
        v1 = self.input.linear(x1, self.linear.weight, self.linear.bias)
        v2 = self.input.sigmoid(v1)
        v3 = (v1 * v2)
        return (v3, v2, v1)



func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
'FloatFunctional' object has no attribute 'linear'

jit:
linear

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''