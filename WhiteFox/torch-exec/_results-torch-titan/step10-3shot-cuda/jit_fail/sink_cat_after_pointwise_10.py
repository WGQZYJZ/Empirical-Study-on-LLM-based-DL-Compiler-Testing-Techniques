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
        y = x.flatten()
        for i in range(0, 2):
            y.tanh()
            if (i == 1):
                y = torch.cat((y, y), dim=1)
        if True:
            k = y.view(x.shape[0], (- 1)).tanh()
        else:
            k = y.view(x.shape[0], (- 1)).tanh()
        for i in range(0, 2):
            k.sin()
            if (i == 1):
                k = k.view(x.shape[0], (- 1)).sin()
        return x




func = Model().to('cuda')



x = torch.randn(2, 3, 4)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Dimension out of range (expected to be in range of [-1, 0], but got 1)

jit:
Failed running call_function <built-in method cat of type object at 0x7af1aaa699e0>(*((FakeTensor(..., device='cuda:0', size=(24,)), FakeTensor(..., device='cuda:0', size=(24,))),), **{'dim': 1}):
Dimension out of range (expected to be in range of [-1, 0], but got 1)

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''