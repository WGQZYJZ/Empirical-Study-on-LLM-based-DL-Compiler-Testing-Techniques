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

    def forward(self, input1, input2, input3, input4):
        t0 = torch.mm(input1, input2)
        t1 = torch.mm(input2, input1)
        t2 = torch.mm(input3, input2)
        t3 = torch.mm(input3, input1)
        t4 = (t2 + t1)
        t5 = (t0 + t3)
        t6 = torch.mm(input1, input3)
        return ((t6 + t5) + t4)




func = Model().to('cuda')



input1 = torch.randn(10, 8, 8)



input2 = torch.randn(10, 8, 8)



input3 = torch.randn(10, 8, 8)



input4 = torch.randn(10, 8, 8)


test_inputs = [input1, input2, input3, input4]

# JIT_FAIL
'''
direct:
self must be a matrix

jit:
Failed running call_function <built-in method mm of type object at 0x77e77ec699e0>(*(FakeTensor(..., device='cuda:0', size=(10, 8, 8)), FakeTensor(..., device='cuda:0', size=(10, 8, 8))), **{}):
a must be 2D

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''