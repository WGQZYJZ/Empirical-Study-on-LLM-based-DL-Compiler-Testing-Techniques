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
        self.fc2 = torch.nn.Linear(12, 5)

    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        v2 = (v1 + x1)
        v3 = (v2 + self.fc2)
        return v3




func = Model().to('cuda')



x1 = torch.randn(10, 12, requires_grad=True)



x2 = torch.randn(10, 12, requires_grad=True)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (10x12 and 10x12)

jit:
Failed running call_function <built-in method mm of type object at 0x700df5c699e0>(*(FakeTensor(..., device='cuda:0', size=(10, 12)), FakeTensor(..., device='cuda:0', size=(10, 12))), **{}):
a and b must have same reduction dim, but got [10, 12] X [10, 12].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''