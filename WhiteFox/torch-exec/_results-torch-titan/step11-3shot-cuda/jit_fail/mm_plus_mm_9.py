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
        t2 = (t1 * t1)
        t3 = (t2 - t1)
        t4 = torch.mm(t3, input3)
        t5 = (t3 + t2)
        t6 = torch.mm(t5, input3)
        return (t4 + t6)




func = Model().to('cuda')



input1 = torch.randn(14, 13)



input2 = torch.randn(14, 13)



input3 = torch.randn(13, 28)


test_inputs = [input1, input2, input3]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (14x13 and 14x13)

jit:
Failed running call_function <built-in method mm of type object at 0x71485c8699e0>(*(FakeTensor(..., device='cuda:0', size=(14, 13)), FakeTensor(..., device='cuda:0', size=(14, 13))), **{}):
a and b must have same reduction dim, but got [14, 13] X [14, 13].

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''