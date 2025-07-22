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
        super(Model, self).__init__()
        self.linear = torch.nn.Linear(16, 32)

    def forward(self, x1):
        v1 = self.linear(x)
        v2 = torch.clamp_min(v1, min_value=-0.5)
        v3 = torch.clamp_max(v2, max_value=0.4)
        return v3


func = Model().to('cpu')


x1 = torch.randn(16, 4)

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