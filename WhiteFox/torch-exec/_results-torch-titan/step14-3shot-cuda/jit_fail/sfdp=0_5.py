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

    def __init__(self):
        super().__init__()
        self.key = torch.nn.Parameter(torch.randn(6, 10))

    def forward(self, x1):
        q = x1
        k = self.key
        v = self.key
        inv_scale = math.sqrt(k.size(1))
        scaled_dot_product = (torch.matmul(q, k.transpose((- 2), (- 1))) / inv_scale)
        attention_weights = scaled_dot_product.softmax(dim=(- 1))
        output = attention_weights.matmul(v)
        return output




func = Model().to('cuda')



x1 = torch.randn(1, 6, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (384x64 and 10x6)

jit:
Failed running call_function <built-in method matmul of type object at 0x7188368699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 6, 64, 64)), FakeTensor(..., device='cuda:0', size=(10, 6), requires_grad=True)), **{}):
a and b must have same reduction dim, but got [384, 64] X [10, 6].

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''