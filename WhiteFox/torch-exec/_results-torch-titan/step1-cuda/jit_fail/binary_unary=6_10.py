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
        self.fc = torch.nn.Linear(3, 5, bias=False)

    def forward(self, x1, x2):
        v1 = torch.relu((x2 - self.fc(x1)))
        return v1



func = Model().to('cuda')



x1 = torch.randn(3, 4, 2)



x2 = torch.randn(3, 4, 2)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (12x2 and 3x5)

jit:
Failed running call_module L__self___fc(*(FakeTensor(..., device='cuda:0', size=(3, 4, 2)),), **{}):
a and b must have same reduction dim, but got [12, 2] X [3, 5].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''