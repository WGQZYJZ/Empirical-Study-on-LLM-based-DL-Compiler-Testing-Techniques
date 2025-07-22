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
        self.linear = torch.nn.Linear(64 * 64, 8)

    def forward(self, x1):
        v1 = x1.view(x1.size(0), -1)
        v2 = self.linear(v1)
        v3 = v2 + 3
        v4 = torch.clamp_max(v3, 6)
        v5 = torch.clamp_min(v4, 0)
        v6 = v5 / 6
        return v6


func = Model().to('cpu')

x1 = 1

test_inputs = [x1]

# JIT_FAIL
'''
direct:
'int' object has no attribute 'view'

jit:
Failed running call_method size(*(s0, 0), **{}):
'SymInt' object has no attribute 'size'

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''