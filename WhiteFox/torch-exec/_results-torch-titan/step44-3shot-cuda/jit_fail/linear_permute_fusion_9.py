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
        self.linear = torch.nn.Linear(2, 4)

    def forward(self, x2):
        v2 = torch.mm(x2, self.linear.weight)
        v3 = v2.permute(2, 0, 1)
        v4 = v3.contiguous()
        return v4




func = Model().to('cuda')



x2 = torch.randn(2, 3)


test_inputs = [x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x3 and 4x2)

jit:
Failed running call_function <built-in method mm of type object at 0x749af82699e0>(*(FakeTensor(..., device='cuda:0', size=(2, 3)), Parameter(FakeTensor(..., device='cuda:0', size=(4, 2), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [2, 3] X [4, 2].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''