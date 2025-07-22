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

class Model(nn.Module):

    def __init__(self):
        super().__init__()
        self.layers = nn.Linear(2, 4)

    def forward(self, x):
        x = self.layers(x)
        x = torch.cat((x, x), dim=1)
        x = x.reshape(4, 8)
        x = torch.stack(([x], [x]), dim=1)
        return x



func = Model().to('cpu')


x = torch.randn(2, 2)

test_inputs = [x]

# JIT_FAIL
'''
direct:
shape '[4, 8]' is invalid for input of size 16

jit:
Failed running call_method reshape(*(FakeTensor(..., size=(2, 8)), 4, 8), **{}):
shape '[4, 8]' is invalid for input of size 16

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''