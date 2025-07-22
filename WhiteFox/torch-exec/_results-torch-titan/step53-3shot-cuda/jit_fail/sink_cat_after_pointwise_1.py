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
        y = torch.cat([x[:, :3], x[:, 4:]], dim=1)
        x = y.reshape(y.shape[0], x.shape[1], (- 1))
        return x.tanh()




func = Model().to('cuda')



x = torch.randn(2, 10, 4)


test_inputs = [x]

# JIT_FAIL
'''
direct:
shape '[2, 10, -1]' is invalid for input of size 72

jit:
Failed running call_method reshape(*(FakeTensor(..., device='cuda:0', size=(2, 9, 4)), 2, 10, -1), **{}):
shape '[2, 10, -1]' is invalid for input of size 72

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''