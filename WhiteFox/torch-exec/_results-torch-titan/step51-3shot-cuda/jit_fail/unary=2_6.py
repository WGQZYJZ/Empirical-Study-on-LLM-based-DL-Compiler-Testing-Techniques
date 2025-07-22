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
        x1 = torch.unsqueeze(x, 1)
        x2 = torch.unsqueeze(x1, 2)
        x3 = torch.cat((x, x, x, x), 1)
        x4 = torch.reshape(x3, (1, 4, 8, 32))
        x5 = torch.reshape(x, (1, 1, 4, 33))
        x6 = torch.cat((x5, x4, x5), 1)
        x7 = torch.cat((x2, x2, x6, x4, x4), 2)
        return x7




func = Model().to('cuda')



x = torch.randn(1, 4, 8, 32)


test_inputs = [x]

# JIT_FAIL
'''
direct:
shape '[1, 4, 8, 32]' is invalid for input of size 4096

jit:
Failed running call_function <built-in method reshape of type object at 0x75b31d2699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 16, 8, 32)), (1, 4, 8, 32)), **{}):
shape '[1, 4, 8, 32]' is invalid for input of size 4096

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''