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
        self.key = torch.nn.Parameter(torch.randn(10, 36))

    def forward(self, x1):
        q = x1
        k = x1
        v = x1
        inv_scale = math.sqrt(k.size(1))
        scaled_dot_product = (torch.matmul(q, k.transpose((- 2), (- 1))) / inv_scale)
        attention_weights = scaled_dot_product.softmax(dim=(- 1))
        output = attention_weights.matmul(v.repeat(1, 3, 1, 1, 1))
        return output




func = Model().to('cuda')



x1 = torch.randn(11, 9, 51, 23)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (11) must match the size of tensor b (33) at non-singleton dimension 1

jit:
Failed running call_method matmul(*(FakeTensor(..., device='cuda:0', size=(11, 9, 51, 51)), FakeTensor(..., device='cuda:0', size=(1, 33, 9, 51, 23))), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''