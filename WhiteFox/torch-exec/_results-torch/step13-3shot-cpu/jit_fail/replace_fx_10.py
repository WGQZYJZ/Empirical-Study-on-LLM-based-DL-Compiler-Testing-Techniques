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
        x1 = torch.rand_like(x, dtype=torch.long)
        x2 = torch.relu6(x)
        return x2



func = Model().to('cpu')


x1 = torch.randn(1, 6)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
"check_uniform_bounds" not implemented for 'Long'

jit:
AttributeError: module 'torch' has no attribute 'relu6'

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''