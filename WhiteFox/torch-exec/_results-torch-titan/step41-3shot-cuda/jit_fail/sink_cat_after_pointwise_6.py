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

    def forward(self, x, x1, x2):
        v1 = torch.cat((x1, x2), dim=1)
        v2 = torch.cat((v1, x1, x2, x1, x2, x1, x2, x1, x2), dim=1)
        y = (torch.tanh(v2) + (x1 * x2))
        return y




func = Model().to('cuda')



x = torch.randn(1, 3)



x1 = torch.randn(1)



x2 = torch.randn(1)


test_inputs = [x, x1, x2]

# JIT_FAIL
'''
direct:
Dimension out of range (expected to be in range of [-1, 0], but got 1)

jit:
Failed running call_function <built-in method cat of type object at 0x7c2cbcc699e0>(*((FakeTensor(..., device='cuda:0', size=(1,)), FakeTensor(..., device='cuda:0', size=(1,))),), **{'dim': 1}):
Dimension out of range (expected to be in range of [-1, 0], but got 1)

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''