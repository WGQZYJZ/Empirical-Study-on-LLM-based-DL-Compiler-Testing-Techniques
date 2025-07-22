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

    def __init__(self, min_value=-3.0):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, m.weight, None)
        v2 = v1.clamp_min(self.min_value)
        v3 = v2.clamp_max(-1.5)
        return v3


func = Model(1.5).to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
name 'm' is not defined

jit:
NameError: name 'm' is not defined

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''