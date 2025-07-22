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
        v1 = x1.conv2d(3, 8, 1, stride=1, padding=1)
        v2 = v1 + 3
        v3 = v2.clamp(min=0, max=6)
        v4 = v3 / 6
        return v4



func = Model().to('cuda')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
'Tensor' object has no attribute 'conv2d'

jit:
AttributeError: 'Tensor' object has no attribute 'conv2d'

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''