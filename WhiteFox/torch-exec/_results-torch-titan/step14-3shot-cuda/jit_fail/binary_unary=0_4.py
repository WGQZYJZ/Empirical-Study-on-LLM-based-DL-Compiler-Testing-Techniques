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
        self.conv = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)

    def forward(self, x):
        v1 = torch.gelu(self.conv(x))
        v2 = torch.tanh(v1)
        return v2




func = Model().to('cuda')



x = torch.randn(1, 16, 64, 64)


test_inputs = [x]

# JIT_FAIL
'''
direct:
module 'torch' has no attribute 'gelu'

jit:
module 'torch' has no attribute 'gelu'

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''