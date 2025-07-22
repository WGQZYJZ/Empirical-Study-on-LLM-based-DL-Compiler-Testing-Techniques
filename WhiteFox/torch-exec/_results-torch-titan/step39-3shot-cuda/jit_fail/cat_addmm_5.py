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
        self.layers = nn.Linear(100, (100 + 100))
        self.layers1 = nn.Linear(100, (100 + 100))
        self.layers2 = nn.Linear(100, (100 + 100))
        self.layers3 = nn.Linear(100, (100 + 100))

    def forward(self, x):
        x = self.layers(x)
        x = torch.stack((x, x, x, x, x), dim=1)
        x = x.flatten(start_dim=1)
        x = (self.layers1(x), self.layers2(x), self.layers3(x))
        return x




func = Model().to('cuda')



x = torch.randn(5, 100)


test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (5x1000 and 100x200)

jit:
Failed running call_module L__self___layers1(*(FakeTensor(..., device='cuda:0', size=(5, 1000)),), **{}):
a and b must have same reduction dim, but got [5, 1000] X [100, 200].

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''