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
        self.linear = torch.nn.Linear(64, 64)

    def forward(self, x1):
        v7 = self.linear(x1)
        v8 = v7 + 3
        v9 = torch.nn.functional.clamp_min(v8, 0)
        v10 = torch.nn.functional.clamp_max(v9, 6)
        v11 = v10 / 6
        return v11


func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
module 'torch.nn.functional' has no attribute 'clamp_min'

jit:
AttributeError: module 'torch.nn.functional' has no attribute 'clamp_min'

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''