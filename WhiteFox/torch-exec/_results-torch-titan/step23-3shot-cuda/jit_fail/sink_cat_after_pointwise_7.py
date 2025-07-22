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
        self.weight = torch.randn(5, 4)

    def forward(self, x):
        x = torch.cat((x, x), dim=1)
        x = torch.matmul(x, self.weight)
        x = x.view((- 1))
        return x




func = Model().to('cuda')



x = torch.randn(2, 3, 4)


test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (12x4 and 5x4)

jit:
Failed running call_function <built-in method matmul of type object at 0x78f8e52699e0>(*(FakeTensor(..., device='cuda:0', size=(2, 6, 4)), FakeTensor(..., device='cuda:0', size=(5, 4))), **{}):
a and b must have same reduction dim, but got [12, 4] X [5, 4].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''