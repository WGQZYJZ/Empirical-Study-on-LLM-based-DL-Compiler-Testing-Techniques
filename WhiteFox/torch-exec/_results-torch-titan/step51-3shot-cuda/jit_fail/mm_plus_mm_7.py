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

    def forward(self, input):
        t1 = torch.mm(input, input)
        t1 = (t1 + t1)
        t2 = (t1 + t1)
        t2 = (t2 + t1)
        return t2




func = Model().to('cuda')



input = torch.randn(1, 100)


test_inputs = [input]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x100 and 1x100)

jit:
Failed running call_function <built-in method mm of type object at 0x72c26b8699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 100)), FakeTensor(..., device='cuda:0', size=(1, 100))), **{}):
a and b must have same reduction dim, but got [1, 100] X [1, 100].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''