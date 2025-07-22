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

    def __init__(self, negative_slope):
        super().__init__()
        self.conv = torch.nn.Conv2d(49, 1, 3, padding=16)
        self.relu = torch.nn.ReLU()

    def forward(self, x):
        y = self.conv(x)
        z = self.relu(y)
        u = (z * self.negative_slope)
        v = (u - 0.001)
        w = v.relu()
        return w




negative_slope = (- 0.252)


func = Model(negative_slope).to('cuda')



x = torch.randn(3, 49, 9, 9)


test_inputs = [x]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'negative_slope'

jit:
negative_slope

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''