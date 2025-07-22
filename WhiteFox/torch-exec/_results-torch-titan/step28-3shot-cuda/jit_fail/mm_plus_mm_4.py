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
        t1 = torch.mm(input1, input2)
        t2 = torch.mm(input1, input4)
        t3 = (t1 + t2)
        t4 = torch.mm(input3, input4)
        t5 = (t4 + t3)
        t6 = torch.mm(input3, input2)
        return (t5 + t6)




func = Model().to('cuda')



input1 = torch.randn(7, 4)



input2 = torch.randn(4, 3)



input3 = torch.randn(7, 3)



input4 = torch.randn(3, 6)


test_inputs = [input1, input2, input3, input4]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (7x4 and 3x6)

jit:
Failed running call_function <built-in method mm of type object at 0x73d518e699e0>(*(FakeTensor(..., device='cuda:0', size=(7, 4)), FakeTensor(..., device='cuda:0', size=(3, 6))), **{}):
a and b must have same reduction dim, but got [7, 4] X [3, 6].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''