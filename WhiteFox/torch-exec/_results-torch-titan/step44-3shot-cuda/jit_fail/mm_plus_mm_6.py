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
        self.linear1 = torch.nn.Linear(1, 1)
        self.linear2 = torch.nn.Linear(1, 1)
        self.linear3 = torch.nn.Linear(1, 1)
        self.linear4 = torch.nn.Linear(1, 1)

    def forward(self, input1, input2, input3):
        x1 = input1
        x2 = input2
        x3 = input3
        x4 = input1
        x1 = torch.mm(x1, x4)
        x2 = self.linear1(input1)
        x3 = torch.mm(x2, x1)
        x4 = self.linear2(x3)
        x1 = torch.mm(x2, input2)
        x2 = self.linear3(x1)
        x3 = self.linear3(x2)
        x4 = torch.mm(x3, input3)
        x1 = self.linear3(x3)
        x2 = self.linear4(x1)
        x3 = (x4 + x2)
        return ((x2 + x3) + x3)




func = Model().to('cuda')



input1 = torch.randn(4, 4)



input2 = torch.randn(4, 4)



input3 = torch.randn(4, 4)


test_inputs = [input1, input2, input3]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (4x4 and 1x1)

jit:
Failed running call_module L__self___linear1(*(FakeTensor(..., device='cuda:0', size=(4, 4)),), **{}):
a and b must have same reduction dim, but got [4, 4] X [1, 1].

from user code:
   File "<string>", line 30, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''