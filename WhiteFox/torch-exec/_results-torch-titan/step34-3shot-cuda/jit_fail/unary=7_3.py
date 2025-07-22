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
        self.fc = torch.nn.Linear(224, 187)

    def forward(self, x1):
        l1 = self.fc(x1)
        l2 = ((l1 * torch.clamp(l1.min(), l1.max(), 6)) + 3)
        l3 = (l2 / 6)
        return l3



func = Model().to('cuda')



x1 = torch.randn(1, 288, 3, 3)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (864x3 and 224x187)

jit:
Failed running call_module L__self___fc(*(FakeTensor(..., device='cuda:0', size=(1, 288, 3, 3)),), **{}):
a and b must have same reduction dim, but got [864, 3] X [224, 187].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''