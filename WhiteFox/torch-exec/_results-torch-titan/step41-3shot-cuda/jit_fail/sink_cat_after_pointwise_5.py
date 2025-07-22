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
        self.fc1 = torch.nn.Linear(2, 4)
        self.fc2 = torch.nn.Linear(2, 6)

    def forward(self, x, x1):
        x = self.fc1(x)
        x = torch.cat((x, x1), dim=1)
        x = self.fc2(x)
        x = torch.relu(x)
        return x




func = Model().to('cuda')



x = torch.randn(2, 2)



x1 = torch.randn(2, 3)


test_inputs = [x, x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x7 and 2x6)

jit:
Failed running call_module L__self___fc2(*(FakeTensor(..., device='cuda:0', size=(2, 7)),), **{}):
a and b must have same reduction dim, but got [2, 7] X [2, 6].

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''