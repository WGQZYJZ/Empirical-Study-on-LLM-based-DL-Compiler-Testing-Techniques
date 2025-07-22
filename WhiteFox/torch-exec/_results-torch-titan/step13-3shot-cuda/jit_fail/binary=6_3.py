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
        self.fc = torch.nn.Linear(4096, 4096)

    def forward(self, x1):
        v1 = self.fc(x1)
        v2 = (v1 - 0.8165)
        return v2



func = Model().to('cuda')



x1 = torch.randn(5)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x5 and 4096x4096)

jit:
Failed running call_module L__self___fc(*(FakeTensor(..., device='cuda:0', size=(5,)),), **{}):
a and b must have same reduction dim, but got [1, 5] X [4096, 4096].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''