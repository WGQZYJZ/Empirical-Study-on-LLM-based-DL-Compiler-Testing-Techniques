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
        y1 = torch.cat((x, x), dim=1).view(2, 6)
        y2 = torch.cat((y1, x), dim=1)
        y3 = torch.relu(y2)
        y4 = torch.cat((y3, x), dim=1).tanh()
        return y4




func = Model().to('cuda')



x = torch.randn(1, 3, 2)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Tensors must have same number of dimensions: got 2 and 3

jit:
Failed running call_function <built-in method cat of type object at 0x7d10d00699e0>(*((FakeTensor(..., device='cuda:0', size=(2, 6)), FakeTensor(..., device='cuda:0', size=(1, 3, 2))),), **{'dim': 1}):
Sizes of tensors must match except in dimension 1. Expected 2 but got 1 for tensor number 1 in the list

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''