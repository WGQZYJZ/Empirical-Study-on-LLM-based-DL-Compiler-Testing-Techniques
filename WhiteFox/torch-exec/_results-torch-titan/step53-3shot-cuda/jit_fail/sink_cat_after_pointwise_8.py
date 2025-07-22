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

    def forward(self, x):
        y = torch.cat([x, x, x], dim=3)
        return (y.view(y.shape[0], y.shape[1], (- 1)).tanh() if (y.shape != (2, 3, 2, 1)) else y.view(y.shape[0], y.shape[1], (- 1)).relu())




func = Model().to('cuda')



x = torch.randn(2, 3, 4)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Dimension out of range (expected to be in range of [-3, 2], but got 3)

jit:
Failed running call_function <built-in method cat of type object at 0x7f40a9a699e0>(*([FakeTensor(..., device='cuda:0', size=(2, 3, 4)), FakeTensor(..., device='cuda:0', size=(2, 3, 4)), FakeTensor(..., device='cuda:0', size=(2, 3, 4))],), **{'dim': 3}):
Dimension out of range (expected to be in range of [-3, 2], but got 3)

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''