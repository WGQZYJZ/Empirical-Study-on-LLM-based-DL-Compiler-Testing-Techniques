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
        self.key = torch.nn.Parameter(torch.randn(1, 64, 1, 1))
        self.y = torch.nn.Parameter(torch.randn(1, 64, 1, 1))

    def forward(self, x1):
        q = x1
        k = x1
        v = x1
        inv_scale = math.sqrt(k.size(1))
        scaled_dot_product = (torch.matmul(q, k.transpose((- 2), (- 1))) / inv_scale)
        attention_weights = scaled_dot_product.softmax(dim=(- 1))
        output = attention_weights.matmul(v)
        m = torch.add(output, self.y)
        return m




func = Model().to('cuda')



x1 = torch.randn(2, 32, 57, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (32) must match the size of tensor b (64) at non-singleton dimension 1

jit:
Failed running call_function <built-in method add of type object at 0x720687e699e0>(*(FakeTensor(..., device='cuda:0', size=(2, 32, 57, 64)), Parameter(FakeTensor(..., device='cuda:0', size=(1, 64, 1, 1), requires_grad=True))), **{}):
Attempting to broadcast a dimension of length 64 at -3! Mismatching argument at index 1 had torch.Size([1, 64, 1, 1]); but expected shape should be broadcastable to [2, 32, 57, 64]

from user code:
   File "<string>", line 30, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''