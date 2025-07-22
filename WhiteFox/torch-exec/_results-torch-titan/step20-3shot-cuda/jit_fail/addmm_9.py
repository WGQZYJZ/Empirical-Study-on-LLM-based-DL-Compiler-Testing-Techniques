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

    def forward(self, x1, x2, inp):
        v1 = torch.nn.functional.conv1d(x1, x2, stride=757)
        v2 = (v1 + inp)
        return v2




func = Model().to('cuda')



x1 = torch.randn(3, 3, 39)



x2 = torch.randn(3, 39, 5)

inp = 1

test_inputs = [x1, x2, inp]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [3, 39, 5], expected input[3, 3, 39] to have 39 channels, but got 3 channels instead

jit:
Failed running call_function <built-in method conv1d of type object at 0x7b030c2699e0>(*(FakeTensor(..., device='cuda:0', size=(3, 3, 39)), FakeTensor(..., device='cuda:0', size=(3, 39, 5))), **{'stride': 757}):
Invalid channel dimensions

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''