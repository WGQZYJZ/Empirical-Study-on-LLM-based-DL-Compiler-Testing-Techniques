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

    def forward(self, left, right):
        mm1 = torch.mm(left, right)
        left = torch.mm(left, right)
        right = torch.mm(left, right)
        mm2 = (left + right)
        mm1 = torch.mm(left, right)
        return (mm1 + mm2)




func = Model().to('cuda')



left = torch.randn(20, 10)



right = torch.randn(10, 20)


test_inputs = [left, right]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (20x20 and 10x20)

jit:
Failed running call_function <built-in method mm of type object at 0x7774ba8699e0>(*(FakeTensor(..., device='cuda:0', size=(20, 20)), FakeTensor(..., device='cuda:0', size=(10, 20))), **{}):
a and b must have same reduction dim, but got [20, 20] X [10, 20].

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''