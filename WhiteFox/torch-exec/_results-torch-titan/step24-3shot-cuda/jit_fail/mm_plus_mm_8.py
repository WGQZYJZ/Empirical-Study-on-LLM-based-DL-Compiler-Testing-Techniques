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

    def forward(self, input):
        t1 = torch.mm(input, torch.rand(40, 40))
        t2 = torch.mm(input, torch.rand(32, 32))
        t3 = torch.mm(input, torch.rand(32, 32))
        return torch.mm(torch.mm(t1, t3), torch.rand(32, 32))




func = Model().to('cuda')

input = 1

test_inputs = [input]

# JIT_FAIL
'''
direct:
mm(): argument 'input' (position 1) must be Tensor, not int

jit:
Failed running call_function <built-in method mm of type object at 0x76b2870699e0>(*(1, FakeTensor(..., size=(40, 40))), **{}):
mm(): argument 'input' (position 1) must be Tensor, not int

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''