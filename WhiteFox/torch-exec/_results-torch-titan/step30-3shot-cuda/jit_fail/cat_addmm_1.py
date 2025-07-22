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
        self.layers = torch.nn.Sequential(torch.nn.Conv2d(2, 2, 2, padding=1), nn.Linear(4, 6))

    def forward(self, x):
        x = self.layers(x)
        return x




func = Model().to('cuda')



x = torch.randn(2, 2, 2, 2)


test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (12x3 and 4x6)

jit:
Failed running call_module L__self___layers_1(*(FakeTensor(..., device='cuda:0', size=(2, 2, 3, 3)),), **{}):
a and b must have same reduction dim, but got [12, 3] X [4, 6].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''