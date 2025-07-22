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
        if (torch.__version__ <= '1.8.0'):
            self.linear = torch.nn.Linear(1024, 1000)
        else:
            self.linear = torch.nn.Linear(128, 384)

    def forward(self, x1, x2):
        v1 = self.linear(x1)
        v2 = (v1 + x2)
        v3 = torch.relu(v2)
        return v3



func = Model().to('cuda')



x1 = torch.randn(1, 1024)



x2 = torch.randn(1, 128)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x1024 and 128x384)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(1, 1024)),), **{}):
a and b must have same reduction dim, but got [1, 1024] X [128, 384].

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''