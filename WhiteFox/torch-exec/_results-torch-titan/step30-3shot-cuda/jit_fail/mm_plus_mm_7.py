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

    def forward(self, matrix1, matrix2, matrix3, matrix4):
        mm1 = torch.nn.functional.linear(matrix1, torch.randn_like(matrix1))
        mm_t = torch.mm(mm1, matrix2)
        t = (mm_t + matrix3)
        m1 = torch.nn.functional.linear(matrix1, torch.randn_like(matrix1))
        m2 = torch.mm(m1, matrix4)
        return t.matmul(m2)




func = Model().to('cuda')



matrix1 = torch.randn(1, 3, 10)



matrix2 = torch.randn(5, 10)



matrix3 = torch.randn(1, 5)



matrix4 = torch.randn(5, 5)


test_inputs = [matrix1, matrix2, matrix3, matrix4]

# JIT_FAIL
'''
direct:
t() expects a tensor with <= 2 dimensions, but self is 3D

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., device='cuda:0', size=(1, 3, 10)), FakeTensor(..., device='cuda:0', size=(1, 3, 10))), **{}):
t() expects a tensor with <= 2 dimensions, but self is 3D

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''