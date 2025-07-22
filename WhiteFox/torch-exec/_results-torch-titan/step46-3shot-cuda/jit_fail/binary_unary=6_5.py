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
        self.linear = torch.nn.Linear(224, 1000, bias=False)
        self.fc = torch.nn.Linear(1000, 1000)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 - 1)
        v3 = torch.nn.functional.relu(v2)
        v4 = self.linear(v3)
        v5 = self.fc(v4)
        return v5



func = Model().to('cuda')



x1 = torch.randn(1, 224)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x1000 and 224x1000)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(1, 1000)),), **{}):
a and b must have same reduction dim, but got [1, 1000] X [224, 1000].

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''