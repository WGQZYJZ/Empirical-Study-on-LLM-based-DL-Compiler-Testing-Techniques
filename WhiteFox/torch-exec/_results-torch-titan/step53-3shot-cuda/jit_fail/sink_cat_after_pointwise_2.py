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
        self.test_1 = nn.Conv2d(3, 3, 3, 1, 1)
        self.test_2 = nn.Conv1d(3, 3, 3, 1, 1)

    def forward(self, x):
        (x_r, x_c) = torch.split(x, 3, dim=(- 1))
        x = self.test_1(x)
        x_r = (x_r + x_c)
        x_c = torch.cat([self.test_2(x).squeeze((- 1)), x_c], dim=1)
        x_cat = torch.cat([x_r, x_c], dim=(- 1))
        return (x_cat, x)




func = Model().to('cuda')



x = torch.randn(4, 3, 8, 8)


test_inputs = [x]

# JIT_FAIL
'''
direct:
too many values to unpack (expected 2)

jit:


from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''