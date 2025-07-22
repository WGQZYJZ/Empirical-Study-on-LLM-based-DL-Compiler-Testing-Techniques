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
        self.key = torch.nn.Parameter(torch.randn(28, 28, 64, 128))

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



x1 = torch.randn(32, 128, 7, 7)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (128) must match the size of tensor b (28) at non-singleton dimension 1

jit:
Failed running call_function <built-in method matmul of type object at 0x7cf1020699e0>(*(FakeTensor(..., device='cuda:0', size=(32, 128, 7, 7)), FakeTensor(..., device='cuda:0', size=(28, 28, 128, 64), requires_grad=True)), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''