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
        self.fc1 = torch.nn.Linear(3, 4)
        self.layer_norm = torch.nn.LayerNorm((4,))

    def forward(self, x):
        y = torch.cat([x, x, x], dim=1)
        y = self.fc1(y)
        y = self.layer_norm(y)
        x = y.view((- 1)).tanh()
        return x




func = Model().to('cuda')



x = torch.randn(2, 3, 4)


test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (18x4 and 3x4)

jit:
Failed running call_module L__self___fc1(*(FakeTensor(..., device='cuda:0', size=(2, 9, 4)),), **{}):
a and b must have same reduction dim, but got [18, 4] X [3, 4].

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''