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
        self.layers = nn.Linear(2, 2)

    def forward(self, x):
        x = self.layers(x)
        dim2 = 2
        dim1 = 2
        x = x.flatten(start_dim=1)
        x = torch.stack([x], dim=0)
        x = x.reshape(((2 * x.size(dim1)) + x.size(dim2)), 1)
        return x




func = Model().to('cuda')



x = torch.randn(2, 2)


test_inputs = [x]

# JIT_FAIL
'''
direct:
shape '[6, 1]' is invalid for input of size 4

jit:
Failed running call_method reshape(*(FakeTensor(..., device='cuda:0', size=(1, 2, 2)), 6, 1), **{}):
shape '[6, 1]' is invalid for input of size 4

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''