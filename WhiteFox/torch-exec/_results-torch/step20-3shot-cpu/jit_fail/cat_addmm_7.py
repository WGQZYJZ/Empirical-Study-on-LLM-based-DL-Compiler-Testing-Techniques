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

class Model(nn.Module):

    def __init__(self):
        super().__init__()
        self.layers = nn.Linear(2, 4)
        self.layers_2 = nn.Linear(3, 3)

    def forward(self, x):
        x = self.layers(x)
        x = x.transpose(0, 1)
        x = x.flatten(start_dim=2, end_dim=3)
        x = torch.stack([x, x, x], dim=1)
        x = torch.abs(x)
        x = self.layers_2(x)
        return x



func = Model().to('cpu')


x = torch.randn(2, 2)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Dimension out of range (expected to be in range of [-2, 1], but got 2)

jit:
Failed running call_method flatten(*(FakeTensor(..., size=(4, 2)),), **{'start_dim': 2, 'end_dim': 3}):
Dimension out of range (expected to be in range of [-2, 1], but got 2)

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''