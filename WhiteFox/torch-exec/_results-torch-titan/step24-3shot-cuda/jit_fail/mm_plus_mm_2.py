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

    def forward(self, input1, input2, input3):
        t1 = torch.mm(input1, input2)
        t2 = torch.mm(input1, input3)
        t3 = (t1 + t2)
        return t3




func = Model().to('cuda')



input1 = torch.randn(3, 3)



input2 = torch.randn(3, 5)



input3 = torch.randn(5, 3)


test_inputs = [input1, input2, input3]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (3x3 and 5x3)

jit:
Failed running call_function <built-in method mm of type object at 0x76b2870699e0>(*(FakeTensor(..., device='cuda:0', size=(3, 3)), FakeTensor(..., device='cuda:0', size=(5, 3))), **{}):
a and b must have same reduction dim, but got [3, 3] X [5, 3].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''