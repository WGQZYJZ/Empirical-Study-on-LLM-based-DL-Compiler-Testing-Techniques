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
        self.linear = torch.nn.Linear(4, 4)

    def forward(self, x):
        v1 = self.linear(x)
        v2 = F.clamp_min(v1, min_value=-2)
        v3 = F.clamp_max(v2, max_value=1)
        return v3


func = Model().to('cpu')


x = torch.randn(1, 4)

test_inputs = [x]

# JIT_FAIL
'''
direct:
module 'torch.nn.functional' has no attribute 'clamp_min'

jit:
AttributeError: module 'torch.nn.functional' has no attribute 'clamp_min'

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''