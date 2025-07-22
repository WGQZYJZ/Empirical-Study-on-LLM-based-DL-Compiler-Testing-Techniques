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
        x1 = x.view((x.shape + (1,)))
        x2 = torch.transpose(x1, 0, 2)
        x3 = torch.cat((x2, x2), dim=0)
        x4 = torch.cat((x1, x3), dim=1)
        x5 = x4.sum(dim=2)
        x6 = torch.cat((x5, x5), dim=0)
        return (2.0 * x6)




func = Model().to('cuda')



x = torch.randn(2, 3, 2, 2)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 1. Expected size 2 but got size 4 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x7c2cbcc699e0>(*((FakeTensor(..., device='cuda:0', size=(2, 3, 2, 2, 1)), FakeTensor(..., device='cuda:0', size=(4, 3, 2, 2, 1))),), **{'dim': 1}):
Sizes of tensors must match except in dimension 1. Expected 2 but got 4 for tensor number 1 in the list

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''