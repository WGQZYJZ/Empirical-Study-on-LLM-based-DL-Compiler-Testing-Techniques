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

    def forward(self, x1, x2, inp):
        v1 = torch.dot(x1, x2)
        v2 = (v1 + inp)
        return v2




func = Model().to('cuda')



x1 = torch.randn(3, 3)



x2 = torch.randn(3, 3)



inp = torch.randn(3, 3)


test_inputs = [x1, x2, inp]

# JIT_FAIL
'''
direct:
1D tensors expected, but got 2D and 2D tensors

jit:
Failed running call_function <built-in method dot of type object at 0x76b3376699e0>(*(FakeTensor(..., device='cuda:0', size=(3, 3)), FakeTensor(..., device='cuda:0', size=(3, 3))), **{}):
1D tensors expected, but got 2D and 2D tensors

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''