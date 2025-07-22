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

    def forward(self, x1, other=None):
        for i in range(0, 3):
            x1 = torch.sum(x1, i)
        return x1




func = Model().to('cuda')



x1 = torch.randn(1, 2, 5)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Dimension out of range (expected to be in range of [-1, 0], but got 2)

jit:
Failed running call_function <built-in method sum of type object at 0x73051b6699e0>(*(FakeTensor(..., device='cuda:0', size=(2,)), 2), **{}):
Dimension out of range (expected to be in range of [-1, 0], but got 2)

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''