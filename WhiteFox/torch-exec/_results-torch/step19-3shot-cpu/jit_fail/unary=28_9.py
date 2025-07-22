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

    def __init__(self, min_value=-1, max_value=1):
        super().__init__()
        self.linear = torch.nn.Linear(in_features=10, out_features=10)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, min_value)
        v3 = torch.clamp_max(v2, max_value)
        return v3


func = Model(min_value=-1).to('cpu')


x1 = torch.randn(1, 10)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
name 'min_value' is not defined

jit:
NameError: name 'min_value' is not defined

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''