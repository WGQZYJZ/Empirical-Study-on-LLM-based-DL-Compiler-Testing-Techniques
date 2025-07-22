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



class Model(nn.Module):

    def __init__(self, hidden_dim, input_shape=None):
        super(Model, self).__init__()
        self.input_tensor = torch.randn(input_shape)
        self.linear1 = nn.Linear(2, hidden_dim, bias=False)
        self.linear2 = torch.nn.Linear(3, 2)

    def forward(self, x):
        x = self.input_tensor
        x = self.linear1(x)
        x = self.linear2(x)
        return x



hidden_dim = 1
func = Model(2, (3, 2)).to('cuda')



x = torch.randn(3, 2)


test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (3x2 and 3x2)

jit:
Failed running call_module L__self___linear2(*(FakeTensor(..., device='cuda:0', size=(3, 2)),), **{}):
a and b must have same reduction dim, but got [3, 2] X [3, 2].

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''