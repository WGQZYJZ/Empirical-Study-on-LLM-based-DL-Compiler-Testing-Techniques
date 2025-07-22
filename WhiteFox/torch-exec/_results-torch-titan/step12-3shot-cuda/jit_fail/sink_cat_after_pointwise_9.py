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
        tensor_list = [x, x, x]
        x = torch.cat(tensor_list, dim=1)
        x = (x.view(x.shape[0], 6) if (x.shape == (1, 18)) else x.view(x.shape[0], 6))
        x = (x.tanh() if (x.shape == (1, 6)) else x.tanh())
        return x




func = Model().to('cuda')



x = torch.randn(2, 3, 4)


test_inputs = [x]

# JIT_FAIL
'''
direct:
shape '[2, 6]' is invalid for input of size 72

jit:
Failed running call_method view(*(FakeTensor(..., device='cuda:0', size=(2, 9, 4)), 2, 6), **{}):
shape '[2, 6]' is invalid for input of size 72

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''