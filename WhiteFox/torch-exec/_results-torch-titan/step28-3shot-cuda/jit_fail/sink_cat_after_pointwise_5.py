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
        (batch, _, width) = x.shape
        bias = torch.zeros(width)
        x = F.conv1d(x, bias.view(1, 1, (- 1)))
        x = x.contiguous().view(batch, (- 1))
        x = x.relu_()
        x = F.conv1d(x, bias.view(1, 1, (- 1)))
        x = x.contiguous().view(batch, (- 1))
        x = x.relu_()
        return x




func = Model().to('cuda')



x = torch.randn(2, 3, 4)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [1, 1, 4], expected input[2, 3, 4] to have 1 channels, but got 3 channels instead

jit:
Failed running call_function <built-in method conv1d of type object at 0x7e03fe2699e0>(*(FakeTensor(..., device='cuda:0', size=(2, 3, 4)), FakeTensor(..., size=(1, 1, 4))), **{}):
Invalid channel dimensions

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''