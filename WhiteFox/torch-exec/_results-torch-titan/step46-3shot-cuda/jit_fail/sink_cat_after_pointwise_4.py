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

    def forward(self, x, y):
        x1 = torch.cat((x, y), dim=1)
        x2 = torch.cat((x, x1), dim=1)
        x3 = torch.cat((x1, x2), dim=1)
        x4 = torch.cat((x, x3), dim=1)
        x5 = torch.cat((x1, x4), dim=1)
        x6 = torch.cat((x2, x5), dim=1)
        x7 = torch.cat((x3, x6), dim=1)
        x8 = torch.cat((x4, x7), dim=1)
        return x8.view(x8.shape).relu()




func = Model().to('cuda')



x = torch.randn(2, 3, 4)



y = torch.randn(2, 3, 2)


test_inputs = [x, y]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 1. Expected size 4 but got size 2 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x7c9ed40699e0>(*((FakeTensor(..., device='cuda:0', size=(2, 3, 4)), FakeTensor(..., device='cuda:0', size=(2, 3, 2))),), **{'dim': 1}):
Sizes of tensors must match except in dimension 1. Expected 4 but got 2 for tensor number 1 in the list

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''