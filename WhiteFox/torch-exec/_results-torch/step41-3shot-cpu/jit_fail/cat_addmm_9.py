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

    def __init__(self):
        super().__init__()
        self.layers = nn.Linear(4, 2)

    def forward(self, x):
        x = self.layers(x)
        output_one = torch.stack((x, x))
        output_two = torch.matmul(x, x.t())
        output_three = torch.matmul(torch.matmul(x, x.t()), x)
        output_four = torch.cat((output_one, output_two, output_three), dim=1)
        return output_four



func = Model().to('cpu')


x = torch.randn(2, 4)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Tensors must have same number of dimensions: got 3 and 2

jit:
Failed running call_function <built-in method cat of type object at 0x77e199396ec0>(*((FakeTensor(..., size=(2, 2, 2)), FakeTensor(..., size=(2, 2)), FakeTensor(..., size=(2, 2))),), **{'dim': 1}):
Number of dimensions of tensors must match.  Expected 3-D tensors, but got 2-D for tensor number 1 in the list

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''