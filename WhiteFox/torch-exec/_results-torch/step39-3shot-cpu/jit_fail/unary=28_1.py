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

    def __init__(self, t1=0.1, t2=-0.1):
        super().__init__()

    def forward(self, x1, x1_max=100, x1_min=-100):
        v1 = torch.clamp(x1, x1_min, x1_max)
        v2 = v1 * t1
        v3 = v2 + t2
        return v3


func = Model(0.1, -0.1).to('cpu')


x1 = torch.randn(1, 32, 32)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
name 't1' is not defined

jit:
NameError: name 't1' is not defined

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''