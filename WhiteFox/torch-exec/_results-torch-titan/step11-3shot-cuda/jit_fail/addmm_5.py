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
        v1 = torch.mm(inp, x2)
        v2 = (v1 + x1)
        return v2




func = Model().to('cuda')



x1 = torch.randn(385, 17)



x2 = torch.randn(17, 1093)



inp = torch.randn(385, 1093)


test_inputs = [x1, x2, inp]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (385x1093 and 17x1093)

jit:
Failed running call_function <built-in method mm of type object at 0x76a7784699e0>(*(FakeTensor(..., device='cuda:0', size=(385, 1093)), FakeTensor(..., device='cuda:0', size=(17, 1093))), **{}):
a and b must have same reduction dim, but got [385, 1093] X [17, 1093].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''