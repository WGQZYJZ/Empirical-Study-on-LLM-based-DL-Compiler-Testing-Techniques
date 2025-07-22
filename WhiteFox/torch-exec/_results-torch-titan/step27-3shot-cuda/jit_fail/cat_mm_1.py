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
        self.linear = torch.nn.Linear(10, 4)

    def forward(self, x):
        v1 = torch.mm(x, self.linear.weight)
        v2 = torch.mm(x, self.linear.weight)
        return torch.cat([v1, v1, v2, v2], 1)




func = Model().to('cuda')



x = torch.randn(2, 10)


test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x10 and 4x10)

jit:
Failed running call_function <built-in method mm of type object at 0x707fef8699e0>(*(FakeTensor(..., device='cuda:0', size=(2, 10)), Parameter(FakeTensor(..., device='cuda:0', size=(4, 10), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [2, 10] X [4, 10].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''