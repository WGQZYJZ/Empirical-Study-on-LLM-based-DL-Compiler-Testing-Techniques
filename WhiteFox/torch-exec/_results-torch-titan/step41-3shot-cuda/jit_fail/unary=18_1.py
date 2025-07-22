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
        self.convm = torch.nn.Conv2d(10, 10, 1, stride=1, padding=1)
        self.conv = torch.nn.Conv2d(10, 10, 1, stride=1, padding=1)

    def forward(self, x1, x2):
        z1 = self.convm(x1)
        z2 = self.conv(x2)
        z3 = torch.cat([z1, z2])
        z4 = torch.sigmoid(z3)
        return z4




func = Model().to('cuda')



x1 = torch.randn(1, 10, 5, 5)



x2 = torch.randn(1, 10, 1, 1)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 0. Expected size 7 but got size 3 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x781076c699e0>(*([FakeTensor(..., device='cuda:0', size=(1, 10, 7, 7)), FakeTensor(..., device='cuda:0', size=(1, 10, 3, 3))],), **{}):
Sizes of tensors must match except in dimension 0. Expected 7 but got 3 for tensor number 1 in the list

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''