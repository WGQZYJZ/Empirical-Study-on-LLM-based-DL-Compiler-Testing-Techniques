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
        v2 = torch.cat([v1, v1, v1, v1, v1], 1)
        v3 = torch.mm(v2, v2)
        return torch.cat([v3, v3, v3, v3, v3, v3, v3, v3], 1)




func = Model().to('cuda')



x1 = torch.randn(1, 8)



x2 = torch.randn(8, 1)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x5 and 1x5)

jit:
Failed running call_function <built-in method mm of type object at 0x779f37c699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 5)), FakeTensor(..., device='cuda:0', size=(1, 5))), **{}):
a and b must have same reduction dim, but got [1, 5] X [1, 5].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''