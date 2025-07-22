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

    def __init__(self, n):
        super().__init__()
        self.W_query = torch.nn.Parameter(torch.Tensor(n, n))
        self.W_key = torch.nn.Parameter(torch.Tensor(n, n))
        self.W_value = torch.nn.Parameter(torch.Tensor(n, n))
        self.scale_factor = math.sqrt(n)

    def forward(self, x):
        qy = torch.matmul(x, self.W_query)
        ky = torch.matmul(x, self.W_key)
        vy = torch.matmul(x, self.W_value)
        s1 = qy.mul(self.scale_factor)
        s2 = s1.softmax(dim=(- 1))
        s3 = torch.nn.functional.dropout(s2, p=0.05)
        z = s3.matmul(vy)
        return z



n = 1
func = Model(3).to('cuda')



batch = torch.randn((10, 3, 7, 7))


test_inputs = [batch]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (210x7 and 3x3)

jit:
Failed running call_function <built-in method matmul of type object at 0x7168e1a699e0>(*(FakeTensor(..., device='cuda:0', size=(10, 3, 7, 7)), Parameter(FakeTensor(..., device='cuda:0', size=(3, 3), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [210, 7] X [3, 3].

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''