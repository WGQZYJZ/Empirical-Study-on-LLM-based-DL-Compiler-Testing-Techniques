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
        x = (x.view(1, 2, 1, 16) if (x.size((- 1)) == 16) else x.view(1, 2, 2, 8))
        return x.view(x.size(0), (- 1))




func = Model().to('cuda')



x = torch.randn(1, 2, 2, 16)


test_inputs = [x]

# JIT_FAIL
'''
direct:
shape '[1, 2, 1, 16]' is invalid for input of size 64

jit:
Failed running call_method view(*(FakeTensor(..., device='cuda:0', size=(1, 2, 2, 16)), 1, 2, 1, 16), **{}):
shape '[1, 2, 1, 16]' is invalid for input of size 64

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''