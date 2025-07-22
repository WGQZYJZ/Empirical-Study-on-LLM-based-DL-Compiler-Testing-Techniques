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

    def forward(self, x1, x2):
        x3 = torch.transpose(x1, 0, 1)
        x4 = torch.transpose(x1, 0, 1)
        x5 = torch.transpose(x2, 0, 1)
        return torch.cat([x5, x4, x3], 0)




func = Model().to('cuda')



x1 = torch.randn(4, 3)



x2 = torch.randn(3)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Dimension out of range (expected to be in range of [-1, 0], but got 1)

jit:
Failed running call_function <built-in method transpose of type object at 0x78db570699e0>(*(FakeTensor(..., device='cuda:0', size=(3,)), 0, 1), **{}):
Dimension out of range (expected to be in range of [-1, 0], but got 1)

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''