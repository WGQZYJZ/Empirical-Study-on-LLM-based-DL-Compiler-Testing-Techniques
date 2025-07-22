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
        self.layers = nn.Linear(2, 20)
        self.linear3 = nn.Linear(30, 2)

    def forward(self, x):
        x = self.layers(x)
        x = torch.stack([x, x, x], dim=1)
        x = torch.stack([x, x, x], dim=1)
        x = torch.stack([x, x, x], dim=1)
        x = torch.stack([x, x, x], dim=1)
        x = x.flatten(start_dim=1)
        x = self.linear3(x)
        return x




func = Model().to('cuda')



x = torch.randn(2, 2)


test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x1620 and 30x2)

jit:
Failed running call_module L__self___linear3(*(FakeTensor(..., device='cuda:0', size=(2, 1620)),), **{}):
a and b must have same reduction dim, but got [2, 1620] X [30, 2].

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''