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

    def forward(self, x1):
        v1 = torch.nn.functional.conv1d(x1, torch.ones(7, 64, 3), stride=1, padding=0, dilation=1, groups=1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.nn.functional.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        return v6



func = Model().to('cpu')


x1 = torch.randn(1, 64, 167)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
module 'torch.nn.functional' has no attribute 'erf'

jit:
AttributeError: module 'torch.nn.functional' has no attribute 'erf'

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''