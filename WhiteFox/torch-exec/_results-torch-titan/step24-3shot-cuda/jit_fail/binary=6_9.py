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

    def forward(self, x1, x2):
        v1 = torch.nn.functional.linear(x1, x2)
        v2 = (v1 - x2)
        return v1




func = Model().to('cuda')



x1 = torch.randn(1, 5, 5, 15, 15)



x2 = torch.randn(1, 10, 1, 28, 28)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
t() expects a tensor with <= 2 dimensions, but self is 5D

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., device='cuda:0', size=(1, 5, 5, 15, 15)), FakeTensor(..., device='cuda:0', size=(1, 10, 1, 28, 28))), **{}):
t() expects a tensor with <= 2 dimensions, but self is 5D

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''