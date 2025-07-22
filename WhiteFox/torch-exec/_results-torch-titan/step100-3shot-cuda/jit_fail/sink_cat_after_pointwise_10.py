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
        self.weight = torch.randn(4, 6)

    def forward(self, x):
        z = torch.cat([x, x, x], dim=1)
        x = z.tanh()
        x = torch.cat([x, x], dim=3)
        x = torch.cat([x, x], dim=3)
        return x.relu()




func = Model().to('cuda')



x = torch.randn(2, 4, 3)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Dimension out of range (expected to be in range of [-3, 2], but got 3)

jit:
Failed running call_function <built-in method cat of type object at 0x758ee24699e0>(*([FakeTensor(..., device='cuda:0', size=(2, 12, 3)), FakeTensor(..., device='cuda:0', size=(2, 12, 3))],), **{'dim': 3}):
Dimension out of range (expected to be in range of [-3, 2], but got 3)

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''