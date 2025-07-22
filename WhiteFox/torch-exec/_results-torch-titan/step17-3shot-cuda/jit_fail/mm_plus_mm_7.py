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
        v1 = torch.mm(x1, x3)
        v2 = torch.mm(x2, x4)
        v3 = (v1 + v2)
        return v3




func = Model().to('cuda')



x1 = torch.FloatTensor(5, 3, 7)



x2 = torch.FloatTensor(5, 7, 6)



x3 = torch.FloatTensor(5, 3, 7)



x4 = torch.FloatTensor(5, 7, 6)


test_inputs = [x1, x2, x3, x4]

# JIT_FAIL
'''
direct:
self must be a matrix

jit:
Failed running call_function <built-in method mm of type object at 0x7bdf1ba699e0>(*(FakeTensor(..., device='cuda:0', size=(5, 3, 7)), FakeTensor(..., device='cuda:0', size=(5, 3, 7))), **{}):
a must be 2D

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''