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

    def forward(self, x):
        p = torch.rand(1, 5).expand(100)
        return torch.add(x, p)




func = Model().to('cuda')



x = torch.randn(1, 5)


test_inputs = [x]

# JIT_FAIL
'''
direct:
expand(torch.FloatTensor{[1, 5]}, size=[100]): the number of sizes provided (1) must be greater or equal to the number of dimensions in the tensor (2)

jit:
Failed running call_method expand(*(FakeTensor(..., size=(1, 5)), 100), **{}):
expand: the requested shape has too few dimensions!

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''