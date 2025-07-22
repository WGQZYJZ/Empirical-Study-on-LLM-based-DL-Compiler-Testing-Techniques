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
        return (torch.cat([x, x], dim=1).view(x.shape[0], -1).leaky_relu(negative_slope=0.2) + torch.cat([x, x], dim=1).view(x.shape[0], -1).leaky_relu(negative_slope=0.05)).sum()



func = Model().to('cpu')


x = torch.randn(2, 3, 4)

test_inputs = [x]

# JIT_FAIL
'''
direct:
'Tensor' object has no attribute 'leaky_relu'

jit:
Failed running call_method leaky_relu(*(FakeTensor(..., size=(2, 24)),), **{'negative_slope': 0.2}):
'FakeTensor' object has no attribute 'leaky_relu'

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''