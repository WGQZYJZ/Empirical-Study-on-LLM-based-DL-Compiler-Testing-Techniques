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

    def forward(self, x1, x2, inp):
        v = torch.mm(x1, x2.flatten())
        return (v + inp)




func = Model().to('cuda')



x1 = torch.randn(2, 2)



x2 = torch.randn(2, 3)



inp = torch.randn(2, 3)


test_inputs = [x1, x2, inp]

# JIT_FAIL
'''
direct:
mat2 must be a matrix

jit:
Failed running call_function <built-in method mm of type object at 0x7ff7c76699e0>(*(FakeTensor(..., device='cuda:0', size=(2, 2)), FakeTensor(..., device='cuda:0', size=(6,))), **{}):
b must be 2D

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''