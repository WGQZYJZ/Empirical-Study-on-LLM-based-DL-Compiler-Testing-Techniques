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
        t2 = torch.mm(input3, input4)
        t3 = torch.mm(input3, input2)
        t4 = torch.mm(input4, input3)
        t5 = torch.mm(input3, input1)
        t6 = torch.mm(input4, input2)
        t7 = torch.mm(input1, input3)
        t8 = torch.mm(input2, input4)
        t9 = ((t2 + t3) + t4)
        t10 = ((t5 + t6) + t7)
        t11 = ((t8 + t9) + t10)
        return t11




func = Model().to('cuda')



input1 = torch.randn(2048, 2048)



input2 = torch.randn(2048, 1024)



input3 = torch.randn(2048, 256)



input4 = torch.randn(1024, 768)


test_inputs = [input1, input2, input3, input4]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2048x256 and 1024x768)

jit:
Failed running call_function <built-in method mm of type object at 0x7481eb6699e0>(*(FakeTensor(..., device='cuda:0', size=(2048, 256)), FakeTensor(..., device='cuda:0', size=(1024, 768))), **{}):
a and b must have same reduction dim, but got [2048, 256] X [1024, 768].

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''