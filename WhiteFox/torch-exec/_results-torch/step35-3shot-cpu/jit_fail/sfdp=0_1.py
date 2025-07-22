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
        self.key = torch.nn.Parameter(torch.randn(1, 1, 5, 5))

    def forward(self, x1):
        q = x1
        k = torch.matmul(x1, self.key)
        v = x1
        inv_scale = math.sqrt(k.size(1))
        scaled_dot_product = torch.matmul(q, k.transpose(-2, -1)) / inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(v)
        return output



func = Model().to('cpu')


x1 = torch.randn(1, 1, 2, 7)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 7] but got: [1, 5].

jit:
Failed running call_function <built-in method matmul of type object at 0x78a5ce596ec0>(*(FakeTensor(..., size=(1, 1, 2, 7)), Parameter(FakeTensor(..., size=(1, 1, 5, 5), requires_grad=True))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 7] but got: [1, 5].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''