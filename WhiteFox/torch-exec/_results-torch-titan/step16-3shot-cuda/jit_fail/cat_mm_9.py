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

    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        v2 = torch.mm(x1, x2)
        return torch.cat([v2, v2, v2, v2, v1, v1, v1, v1, v1, v1], 0)




func = Model().to('cuda')



x1 = torch.randn(3, 6)



x2 = torch.randn(4, 5)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (3x6 and 4x5)

jit:
Failed running call_function <built-in method mm of type object at 0x779f37c699e0>(*(FakeTensor(..., device='cuda:0', size=(3, 6)), FakeTensor(..., device='cuda:0', size=(4, 5))), **{}):
a and b must have same reduction dim, but got [3, 6] X [4, 5].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''