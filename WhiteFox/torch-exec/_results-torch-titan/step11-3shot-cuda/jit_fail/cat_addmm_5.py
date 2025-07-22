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
        super(Model, self).__init__()

    def forward(self, x1, x2, x3, x4):
        y = torch.cat([x1, x2, x3, x4], dim=(- 1))
        return y



func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)



x2 = torch.randn(1, 32, 64, 64)



x3 = torch.randn(1, 64, 128, 128)



x4 = torch.randn(1, 64, 32, 32)


test_inputs = [x1, x2, x3, x4]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 3. Expected size 3 but got size 32 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x7560e48699e0>(*([FakeTensor(..., device='cuda:0', size=(1, 3, 64, 64)), FakeTensor(..., device='cuda:0', size=(1, 32, 64, 64)), FakeTensor(..., device='cuda:0', size=(1, 64, 128, 128)), FakeTensor(..., device='cuda:0', size=(1, 64, 32, 32))],), **{'dim': -1}):
Sizes of tensors must match except in dimension 3. Expected 3 but got 32 for tensor number 1 in the list

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''