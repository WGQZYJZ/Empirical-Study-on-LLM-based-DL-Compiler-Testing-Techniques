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
        self.conv = torch.nn.Conv2d(10, 10, 3)

    def forward(self, x):
        x = self.conv(x)
        x = torch.cat([x, x, x], dim=1)
        x = torch.dropout(x)
        x = torch.relu(((- 3.0) * x))
        x = (torch.sigmoid((1.0 + x)) if (x.shape[1] == 1) else torch.sigmoid((1.0 - x)))
        x = torch.sin(x)
        return x




func = Model().to('cuda')



x = torch.randn(1, 10, 3, 11)


test_inputs = [x]

# JIT_FAIL
'''
direct:
dropout() missing 2 required positional argument: "p", "train"

jit:
Failed running call_function <built-in method dropout of type object at 0x7dda2e6699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 30, 1, 9)),), **{}):
dropout() missing 2 required positional argument: "p", "train"

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''