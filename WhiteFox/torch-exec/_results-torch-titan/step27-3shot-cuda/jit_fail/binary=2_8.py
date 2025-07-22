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
        v1 = torch.nn.functional.conv2d(x, torch.tensor([1], dtype=torch.float32), torch.tensor([1], dtype=torch.float32), stride=(1, 1), padding=(1, 1))
        v2 = (v1 - torch.tensor())
        return v2




func = Model().to('cuda')



x = torch.randn(1, 3, 64, 64)


test_inputs = [x]

# JIT_FAIL
'''
direct:
weight should have at least three dimensions

jit:
Failed running call_function <built-in method conv2d of type object at 0x7e67a70699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 3, 64, 64)), FakeTensor(..., size=(1,)), FakeTensor(..., size=(1,))), **{'stride': (1, 1), 'padding': (1, 1)}):
expected stride to be a single integer value or a list of -1 values to match the convolution dimensions, but got stride=[1, 1]

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''