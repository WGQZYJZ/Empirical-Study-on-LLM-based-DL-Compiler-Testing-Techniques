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
        self.input = torch.randn(3, 3, requires_grad=True)

    def forward(self, x):
        v1 = torch.mm(x, torch.tanh(torch.tanh(torch.mm(x, self.input))))
        return v1




func = Model().to('cuda')



x = torch.randn(5, 5)


test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (5x5 and 3x3)

jit:
Failed running call_function <built-in method mm of type object at 0x7c6cd7e699e0>(*(FakeTensor(..., device='cuda:0', size=(5, 5)), FakeTensor(..., device='cuda:0', size=(3, 3), grad_fn=<CloneBackward0>)), **{}):
a and b must have same reduction dim, but got [5, 5] X [3, 3].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''