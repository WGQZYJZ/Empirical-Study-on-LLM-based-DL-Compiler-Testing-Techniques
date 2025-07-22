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
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 6, 3, stride=2, padding=1)

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = v1.add(3)
        v3 = F.clamp(v2, 0, 6)
        v4 = torch.div(v3, 6)
        return v4



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
module 'torch.nn.functional' has no attribute 'clamp'

jit:
AttributeError: module 'torch.nn.functional' has no attribute 'clamp'

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''