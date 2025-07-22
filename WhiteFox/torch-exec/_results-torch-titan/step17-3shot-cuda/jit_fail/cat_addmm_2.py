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
        self.layers = nn.Linear(2, 1)
        self.layer = nn.Sequential(nn.Linear(2, 4), nn.ReLU(), nn.Linear(4, 1))

    def forward(self, x):
        x = self.layers(x)
        x = self.layer(x)
        return x




func = Model().to('cuda')



x = torch.randn(1, 2)


test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x1 and 2x4)

jit:
Failed running call_module L__self___layer_0(*(FakeTensor(..., device='cuda:0', size=(1, 1)),), **{}):
a and b must have same reduction dim, but got [1, 1] X [2, 4].

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''