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
        t1 = torch.matmul(input1, input2)
        t2 = torch.matmul(input3, input4)
        t1 = torch.matmul(input1, input4)
        t2 = torch.matmul(input3, input2)
        t1 = torch.matmul(input3, input4)
        t2 = torch.matmul(input1, input2)
        t1 = torch.matmul(input1, input3)
        t2 = torch.matmul(input2, input4)
        t3 = (t1 + t2)
        t1 = torch.matmul(input1, input3)
        t2 = torch.matmul(input2, input4)
        t3 = (t1 * t2)
        t1 = torch.matmul(input3, input1)
        t2 = torch.matmul(input2, input4)
        t4 = (t1 + t2)
        t1 = torch.matmul(input3, input1)
        t2 = torch.matmul(input2, input4)
        t4 = (t1 * t2)
        t1 = torch.matmul(input3, input1)
        t2 = torch.matmul(input4, input2)
        t5 = (t1 + t2)
        t1 = torch.matmul(input3, input1)
        t2 = torch.matmul(input4, input2)
        t5 = (t1 * t2)
        t1 = (torch.matmul(t3, t4) + t5)
        t1 = (torch.matmul(t3, t4) * t5)
        t1 = (torch.matmul(t4, t5) + t3)
        t2 = (torch.matmul(t5, t3) + t4)
        t3 = (torch.matmul(t3, t4) + t5)
        t4 = (torch.matmul(t4, t5) + t3)
        t5 = (torch.matmul(t3, t4) + t5)
        t6 = (torch.matmul(t4, t5) + t3)
        return (((((t1 + t2) + t3) + t4) + t5) + t6)




func = Model().to('cuda')



input1 = torch.randn(384, 768)



input2 = torch.randn(768, 384)



input3 = torch.randn(768, 384)



input4 = torch.randn(768, 768)


test_inputs = [input1, input2, input3, input4]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (768x384 and 768x768)

jit:
Failed running call_function <built-in method matmul of type object at 0x7a8a65a699e0>(*(FakeTensor(..., device='cuda:0', size=(768, 384)), FakeTensor(..., device='cuda:0', size=(768, 768))), **{}):
a and b must have same reduction dim, but got [768, 384] X [768, 768].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''