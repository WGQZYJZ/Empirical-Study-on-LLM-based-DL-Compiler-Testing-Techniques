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
        self.linear = torch.nn.Linear(2, 64)
        self.linear1 = torch.nn.Linear(64, 100)
        self.linear2 = torch.nn.Linear(100, 400)
        self.linear3 = torch.nn.Linear(400, 9)

    def forward(self, x1):
        out = torch.nn.functional.softmax(x1, dim=(- 1))
        out1 = self.linear1(torch.nn.functional.relu(self.linear(out)))
        out1 = torch.nn.functional.dropout(out1, p=0.1, training=self.training)
        out2 = self.linear2(torch.nn.functional.tanh(out1))
        out3 = self.linear3(torch.nn.functional.relu(out2))
        return out3



func = Model().to('cuda')



x1 = torch.rand(2, 500)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x500 and 2x64)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(2, 500)),), **{}):
a and b must have same reduction dim, but got [2, 500] X [2, 64].

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''