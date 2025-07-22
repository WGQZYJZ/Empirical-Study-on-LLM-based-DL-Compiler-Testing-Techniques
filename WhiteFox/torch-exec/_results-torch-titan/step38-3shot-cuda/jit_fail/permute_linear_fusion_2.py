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
        self.linear = torch.nn.Linear(1, 4)
        self.linear1 = torch.nn.Linear(4, 2)

    def forward(self, x1):
        v1 = x1.unsqueeze(dim=(- 1))
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        v2 = torch.nn.functional.relu(v2)
        v2 = v2.squeeze(dim=(- 2))
        v3 = torch.max(v2, dim=(- 1))
        v3 = v3[0]
        return torch.nn.functional.linear(v3, self.linear1.weight, self.linear1.bias)




func = Model().to('cuda')



x1 = torch.randn(1, 1)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x1 and 4x2)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., device='cuda:0', size=(1,)), Parameter(FakeTensor(..., device='cuda:0', size=(2, 4), requires_grad=True)), Parameter(FakeTensor(..., device='cuda:0', size=(2,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [1, 1] X [4, 2].

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''