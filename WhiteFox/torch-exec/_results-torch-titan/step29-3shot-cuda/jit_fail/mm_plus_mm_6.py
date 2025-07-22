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
        super(Model, self).__init__()

    def forward(self, x):
        t1 = torch.mm(x, x)
        t2 = torch.mm(t1, x)
        t3 = torch.sin(x)
        return (torch.mm(t3, t2) + torch.mm(t1, t3))




func = Model().to('cuda')



input1 = torch.randn(6, 2)


test_inputs = [input1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (6x2 and 6x2)

jit:
Failed running call_function <built-in method mm of type object at 0x7b90896699e0>(*(FakeTensor(..., device='cuda:0', size=(6, 2)), FakeTensor(..., device='cuda:0', size=(6, 2))), **{}):
a and b must have same reduction dim, but got [6, 2] X [6, 2].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''