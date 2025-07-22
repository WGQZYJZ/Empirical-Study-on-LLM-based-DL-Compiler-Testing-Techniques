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
        self.layers = nn.Linear(2, 6)
        self.fc2 = nn.Linear(2, 3)

    def forward(self, x):
        x = self.layers(x)
        x = self.fc2(x)
        x = torch.stack((x, x), dim=1)
        x = torch.cat((x, x), dim=(- 1))
        return x




func = Model().to('cuda')



x = torch.randn(2, 2)


test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x6 and 2x3)

jit:
Failed running call_module L__self___fc2(*(FakeTensor(..., device='cuda:0', size=(2, 6)),), **{}):
a and b must have same reduction dim, but got [2, 6] X [2, 3].

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''