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
        self.linear1 = torch.nn.Linear(3, 3)
        self.linear2 = torch.nn.Linear(1, 2)

    def forward(self, x1):
        s = self.linear1(x1)
        t = self.linear1(x1)
        y = self.linear2(t)
        return (s, y)




func = Model().to('cuda')



x1 = torch.rand((2, 3))


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x3 and 1x2)

jit:
Failed running call_module L__self___linear2(*(FakeTensor(..., device='cuda:0', size=(2, 3)),), **{}):
a and b must have same reduction dim, but got [2, 3] X [1, 2].

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''