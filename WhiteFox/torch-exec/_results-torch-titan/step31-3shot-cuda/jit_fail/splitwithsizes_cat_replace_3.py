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
        self.features = torch.nn.ModuleList([torch.nn.Conv2d(3, 32, 3, 1, 1), torch.nn.Conv2d(32, 32, 3, 1, 1), torch.nn.Conv2d(32, 32, 3, 2, 3), torch.nn.Conv2d(32, 32, 3, 1, 1), torch.nn.Conv2d(32, 64, 3, 2, 0)])

    def forward(self, x27):
        (x23, x24, x25, x26) = torch.split(x27, [1, 1, 1], dim=0)
        (x37, x38) = torch.split(x33, [1, 1, 1], dim=0)
        (x42, x43, x44) = torch.split(x41, [1, 1, 1], dim=0)
        (x45, x46) = torch.split(x33, [1, 1, 1], dim=0)
        return (x37, x38, x39, x40)




func = Model().to('cuda')



x1 = torch.randn(3, 1, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
not enough values to unpack (expected 4, got 3)

jit:


from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''