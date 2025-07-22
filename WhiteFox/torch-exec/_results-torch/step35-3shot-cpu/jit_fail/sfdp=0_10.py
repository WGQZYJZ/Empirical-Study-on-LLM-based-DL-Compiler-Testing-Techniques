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
        self.key = torch.nn.Parameter(torch.tensor(1.0))

    def forward(self, x1):
        q = torch.tensor(1.0)
        k = x1
        v = torch.tensor(1.0)
        inv_scale = math.sqrt(k.size(1))
        scaled_dot_product = torch.matmul(q, k.transpose(-2, -1)) / inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(v)
        return output



func = Model().to('cpu')


x1 = torch.randn(133, 89, 62, 77)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
both arguments to matmul need to be at least 1D, but they are 0D and 4D

jit:
Failed running call_function <built-in method matmul of type object at 0x78a5ce596ec0>(*(FakeTensor(..., size=()), FakeTensor(..., size=(s0, s1, s3, s2))), **{}):


from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''