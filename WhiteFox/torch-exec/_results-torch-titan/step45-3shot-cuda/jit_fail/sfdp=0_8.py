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
        self.key = torch.nn.Parameter(torch.randn(86, 1, 47, 50))

    def forward(self, x1):
        q = x1
        k = self.key
        v = x1
        inv_scale = math.sqrt(k.size(1))
        scaled_dot_product = (torch.matmul(q, k.transpose((- 2), (- 1))) / inv_scale)
        attention_weights = scaled_dot_product.softmax(dim=(- 1))
        output = attention_weights.matmul(v)
        return output




func = Model().to('cuda')



x1 = torch.randn(10, 1, 49, 28)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (10) must match the size of tensor b (86) at non-singleton dimension 0

jit:
Failed running call_function <built-in method matmul of type object at 0x73850b8699e0>(*(FakeTensor(..., device='cuda:0', size=(10, 1, 49, 28)), FakeTensor(..., device='cuda:0', size=(86, 1, 50, 47), requires_grad=True)), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''