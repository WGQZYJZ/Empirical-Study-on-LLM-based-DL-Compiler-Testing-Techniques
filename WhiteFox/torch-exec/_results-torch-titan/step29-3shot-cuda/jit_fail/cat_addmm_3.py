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
        self.layers = nn.Linear(2, 3)

    def forward(self, x):
        x = self.layers(x)
        x = x.reshape(1, 3)
        x = torch.cat([x], dim=1)
        return x




func = Model().to('cuda')



x = torch.randn(2, 2)


test_inputs = [x]

# JIT_FAIL
'''
direct:
shape '[1, 3]' is invalid for input of size 6

jit:
Failed running call_method reshape(*(FakeTensor(..., device='cuda:0', size=(2, 3)), 1, 3), **{}):
shape '[1, 3]' is invalid for input of size 6

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''