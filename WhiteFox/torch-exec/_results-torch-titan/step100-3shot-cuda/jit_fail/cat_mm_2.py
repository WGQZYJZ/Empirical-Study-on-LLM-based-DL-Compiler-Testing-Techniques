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
        self.linear = torch.nn.Linear(50, 25)
        self.linear2 = torch.nn.Linear(25, 12)
        self.linear3 = torch.nn.Linear(12, 5)

    def forward(self, input1, input2, input3):
        v1 = self.linear(input1)
        v2 = self.linear(input2)
        v3 = self.linear(input3)
        v4 = self.linear2(v1)
        v5 = self.linear2(v2)
        v6 = self.linear2(v3)
        v7 = self.linear3(v1)
        v8 = self.linear3(v2)
        v9 = self.linear3(v3)
        v10 = torch.cat([v1, v2, v3], 1)
        v11 = torch.cat([v4, v5, v6], 1)
        v12 = torch.cat([v7, v8, v9], 1)
        v13 = torch.cat([v10, v11, v12], 0)
        return v13




func = Model().to('cuda')



input1 = torch.randn(5, 50)



input2 = torch.randn(5, 50)



input3 = torch.randn(5, 50)


test_inputs = [input1, input2, input3]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (5x25 and 12x5)

jit:
Failed running call_module L__self___linear3(*(FakeTensor(..., device='cuda:0', size=(5, 25)),), **{}):
a and b must have same reduction dim, but got [5, 25] X [12, 5].

from user code:
   File "<string>", line 30, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''