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

    def forward(self, I):
        p = torch.mm(I[:, 0:12], torch.t(I[:, 1:4]))
        I = torch.mm(torch.t(I[:12, :12]), I[12:, :])
        return (p + I)




func = Model().to('cuda')



I = torch.randn(2100, 100)


test_inputs = [I]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2100x12 and 3x2100)

jit:
Failed running call_function <built-in method mm of type object at 0x7d4289a699e0>(*(FakeTensor(..., device='cuda:0', size=(2100, 12)), FakeTensor(..., device='cuda:0', size=(3, 2100))), **{}):
a and b must have same reduction dim, but got [2100, 12] X [3, 2100].

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''