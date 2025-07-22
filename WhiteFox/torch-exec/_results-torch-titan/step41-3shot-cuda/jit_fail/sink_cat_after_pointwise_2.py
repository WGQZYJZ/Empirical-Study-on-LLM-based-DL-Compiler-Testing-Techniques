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

    def forward(self, x, x1):
        y = torch.cat([x, x1], dim=1)
        x = y.view((- 1)).div(2)
        y = torch.cat([x, x1], dim=1)
        x = y.view((- 1)).div(2)
        z = y.view((- 1)).tanh()
        x = z.div(2)
        y = torch.cat([x, x1], dim=1)
        y = y.view((- 1)).sigmoid()
        return y




func = Model().to('cuda')



x = torch.randn(1, 2)



x1 = torch.randn(1, 3)


test_inputs = [x, x1]

# JIT_FAIL
'''
direct:
Dimension out of range (expected to be in range of [-1, 0], but got 1)

jit:
Failed running call_function <built-in method cat of type object at 0x7c0de02699e0>(*([FakeTensor(..., device='cuda:0', size=(5,)), FakeTensor(..., device='cuda:0', size=(1, 3))],), **{'dim': 1}):
Dimension out of range (expected to be in range of [-1, 0], but got 1)

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''