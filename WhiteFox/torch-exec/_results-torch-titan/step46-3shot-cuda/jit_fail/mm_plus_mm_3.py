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
        t11 = torch.mm(input[0:, 0:], input[0:, 0:])
        t12 = torch.mm(input[0:, 0:], input[0:, 0:])
        t13 = torch.mm(input[0:, 0:], input[0:, 0:])
        t21 = torch.mv(input[0:, 0:], input[0:, 0:])
        t22 = torch.mv(input[0:, 0:], input[0:, 0:])
        t23 = torch.mv(input[0:, 0:], input[0:, 0:])
        t31 = torch.mv(input[0:, 0:], input[0:, 0:])
        t32 = torch.mv(input[0:, 0:], input[0:, 0:])
        t33 = torch.mv(input[0:, 0:], input[0:, 0:])
        return ((((((((t11 + t12) + t13) + t21) + t22) + t23) + t31) + t32) + t33)




func = Model().to('cuda')



input = torch.randn(3, 3)


test_inputs = [input]

# JIT_FAIL
'''
direct:
vector + matrix @ vector expected, got 1, 2, 2

jit:
Failed running call_function <built-in method mv of type object at 0x7faf32c699e0>(*(FakeTensor(..., device='cuda:0', size=(3, 3)), FakeTensor(..., device='cuda:0', size=(3, 3))), **{}):
matrix @ vector expected, got 2, 2

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''