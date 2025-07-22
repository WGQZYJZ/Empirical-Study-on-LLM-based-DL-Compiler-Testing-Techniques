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

    def forward(self, x):
        y = torch.cat((x.permute(3, 2, 1, 0), x), dim=0)
        y = y + y
        return y.view(-1).tanh() if y.shape != (8, 2, 3, 1) else y.view(-1).tanh()



func = Model().to('cpu')


x = torch.randn(2, 3, 1, 2)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 0. Expected size 1 but got size 3 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x726252b96ec0>(*((FakeTensor(..., size=(2, 1, 3, 2)), FakeTensor(..., size=(2, 3, 1, 2))),), **{'dim': 0}):
Sizes of tensors must match except in dimension 0. Expected 1 in dimension 1 but got 3 for tensor number 1 in the list

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''