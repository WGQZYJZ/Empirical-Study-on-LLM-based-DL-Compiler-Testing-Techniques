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

    def forward(self, x1, x2, x3):
        v1 = torch.mm(x1, x2)
        v2 = torch.mm(v1, x2)
        v3 = (v2 + x3)
        return v3




func = Model().to('cuda')



x1 = torch.randn(20, 4)



x2 = torch.randn(4, 20)



x3 = torch.randn(1, 1)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (20x20 and 4x20)

jit:
Failed running call_function <built-in method mm of type object at 0x7831edc699e0>(*(FakeTensor(..., device='cuda:0', size=(20, 20)), FakeTensor(..., device='cuda:0', size=(4, 20))), **{}):
a and b must have same reduction dim, but got [20, 20] X [4, 20].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''