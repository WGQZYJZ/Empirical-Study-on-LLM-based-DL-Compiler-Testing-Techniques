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

    def forward(self, input, input1):
        t1 = torch.mm(input1, input)
        t1 = torch.mm(input, input)
        v1 = t1.mm(input)
        t2 = torch.mm(t1, input)
        t2 = torch.mm(input, input)
        v2 = t2.add(input)
        t3 = t2.mm(t2)
        return ((5 * t3) / v1)




func = Model().to('cuda')



input = torch.randn(10, 10)



input1 = torch.randn(10, 5)


test_inputs = [input, input1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (10x5 and 10x10)

jit:
Failed running call_function <built-in method mm of type object at 0x7de5cc6699e0>(*(FakeTensor(..., device='cuda:0', size=(10, 5)), FakeTensor(..., device='cuda:0', size=(10, 10))), **{}):
a and b must have same reduction dim, but got [10, 5] X [10, 10].

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''