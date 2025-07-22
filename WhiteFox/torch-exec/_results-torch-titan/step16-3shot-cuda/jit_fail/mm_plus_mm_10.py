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
        self.w1 = torch.randn(3, 3)
        self.w2 = torch.randn(3, 3)
        self.w3 = torch.randn(3, 3)
        self.w4 = torch.randn(3, 3)

    def forward(self, input):
        t1 = torch.mm(input, self.w1)
        t2 = ((t1 * torch.mm(input, self.w2)) + torch.mm(input, self.w3))
        t3 = ((t1 * torch.mm(input, self.w2)) + torch.mm(input, self.w4))
        t4 = ((t1 * torch.mm(t2, self.w2)) + torch.mm(input, self.w3))
        return t4




func = Model().to('cuda')



input = torch.randn(10, 10)


test_inputs = [input]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (10x10 and 3x3)

jit:
Failed running call_function <built-in method mm of type object at 0x78248e8699e0>(*(FakeTensor(..., device='cuda:0', size=(10, 10)), FakeTensor(..., device='cuda:0', size=(3, 3))), **{}):
a and b must have same reduction dim, but got [10, 10] X [3, 3].

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''