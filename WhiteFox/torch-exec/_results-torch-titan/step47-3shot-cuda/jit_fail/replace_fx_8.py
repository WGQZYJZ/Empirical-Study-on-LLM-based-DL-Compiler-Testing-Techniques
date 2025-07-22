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



class model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(4, 2)

    def forward(self, y, x):
        a = self.linear(x)
        return (a + torch.nn.functional.dropout(y, p=0.5))




func = model().to('cuda')



x1 = torch.randn(1, 2, 4)




y = torch.exp(torch.randn(1, 1, 1))


test_inputs = [x1, y]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x1 and 4x2)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(1, 1, 1)),), **{}):
a and b must have same reduction dim, but got [1, 1] X [4, 2].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''