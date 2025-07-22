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

    def forward(self, input1, input2, input3, input4, input5):
        t1 = torch.mm(input1, input2)
        t2 = torch.mm(input3, input4)
        t3 = torch.mm(input5, t2)
        return ((t1 + t2) + t3)




func = Model().to('cuda')



input1 = torch.randn(5, 159)



input2 = torch.randn(5, 113)



input3 = torch.randn(5, 104)



input4 = torch.randn(5, 14)



input5 = torch.randn(5, 14)


test_inputs = [input1, input2, input3, input4, input5]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (5x159 and 5x113)

jit:
Failed running call_function <built-in method mm of type object at 0x78248e8699e0>(*(FakeTensor(..., device='cuda:0', size=(5, 159)), FakeTensor(..., device='cuda:0', size=(5, 113))), **{}):
a and b must have same reduction dim, but got [5, 159] X [5, 113].

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''