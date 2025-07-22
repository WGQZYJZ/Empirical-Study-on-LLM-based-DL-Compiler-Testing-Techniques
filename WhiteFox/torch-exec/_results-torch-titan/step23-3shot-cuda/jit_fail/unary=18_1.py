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
        self.sig = torch.nn.Sigmoid()
        self.fc2 = torch.nn.Linear(9216, 10)

    def forward(self, x1):
        v1 = self.sig(x1)
        v2 = v1.view(v1.size(0), (- 1))
        v3 = self.fc2(v2)
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 1, 2, 4, 12)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x96 and 9216x10)

jit:
Failed running call_module L__self___fc2(*(FakeTensor(..., device='cuda:0', size=(1, 96)),), **{}):
a and b must have same reduction dim, but got [1, 96] X [9216, 10].

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''