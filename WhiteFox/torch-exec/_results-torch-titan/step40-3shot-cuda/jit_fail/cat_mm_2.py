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
        v = []
        for loopVar1 in range(3):
            v.append(torch.mm(x1, x2))
        v.append(torch.mm(x1, x2))
        v.append(torch.mm(x1, x2))
        return torch.cat(v, 1)




func = Model().to('cuda')



x1 = torch.randn(2, 3, 1)



x2 = torch.randn(1, 1, 3)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
self must be a matrix

jit:
Failed running call_function <built-in method mm of type object at 0x797feea699e0>(*(FakeTensor(..., device='cuda:0', size=(2, 3, 1)), FakeTensor(..., device='cuda:0', size=(1, 1, 3))), **{}):
a must be 2D

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''