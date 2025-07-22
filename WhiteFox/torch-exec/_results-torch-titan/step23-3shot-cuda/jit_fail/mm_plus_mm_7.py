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
        t1 = torch.mm(input, input)
        v2 = torch.mm(input, input)
        t3 = torch.mm(input, input)
        v4 = ((v1 + v2) + v3)
        return (((t1 + t2) + t3) + v4)




func = Model().to('cuda')



input = torch.randn(1, 10)


test_inputs = [input]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x10 and 1x10)

jit:
Failed running call_function <built-in method mm of type object at 0x74b8da6699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 10)), FakeTensor(..., device='cuda:0', size=(1, 10))), **{}):
a and b must have same reduction dim, but got [1, 10] X [1, 10].

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''