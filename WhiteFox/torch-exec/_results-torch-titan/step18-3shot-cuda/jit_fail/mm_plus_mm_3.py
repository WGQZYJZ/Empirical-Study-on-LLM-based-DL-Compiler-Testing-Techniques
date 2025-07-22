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

    def forward(self, data1):
        data1 = torch.mm(data1, data1)
        return data1




func = Model().to('cuda')



data1 = torch.randn(128, 64)


test_inputs = [data1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (128x64 and 128x64)

jit:
Failed running call_function <built-in method mm of type object at 0x7a40ff6699e0>(*(FakeTensor(..., device='cuda:0', size=(128, 64)), FakeTensor(..., device='cuda:0', size=(128, 64))), **{}):
a and b must have same reduction dim, but got [128, 64] X [128, 64].

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''