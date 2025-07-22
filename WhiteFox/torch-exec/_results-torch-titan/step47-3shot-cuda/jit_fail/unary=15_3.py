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
        self.fc0 = torch.nn.Linear(512, 128)
        self.fc1 = torch.nn.Linear(128, 10)

    def forward(self, x1):
        x1 = x1.view((1, (- 1)))
        x2 = self.fc0(x1)
        x3 = torch.relu(x2)
        return self.fc1(x3)




func = Model().to('cuda')



x1 = torch.rand(1, 3, 28, 28)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x2352 and 512x128)

jit:
Failed running call_module L__self___fc0(*(FakeTensor(..., device='cuda:0', size=(1, 2352)),), **{}):
a and b must have same reduction dim, but got [1, 2352] X [512, 128].

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''