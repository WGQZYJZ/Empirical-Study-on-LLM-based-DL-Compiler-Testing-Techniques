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

    def forward(self, x):
        v1 = torch.linear(x)
        v2 = torch.clamp_min(v1, min_value=3)
        return torch.clamp_max(v2, max_value=(- 3))



func = Model().to('cuda')



x = torch.randn(1, 3, 32, 32)


test_inputs = [x]

# JIT_FAIL
'''
direct:
module 'torch' has no attribute 'linear'

jit:
module 'torch' has no attribute 'linear'

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''