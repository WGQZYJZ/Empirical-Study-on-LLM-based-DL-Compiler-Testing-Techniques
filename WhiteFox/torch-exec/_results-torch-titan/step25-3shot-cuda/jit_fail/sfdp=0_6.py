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
        self.key = torch.nn.Parameter(torch.randn(16, 16))

    def forward(self, x1):
        q = x1
        k = torch.cat([x.unsqueeze(1) for x in self.key.transpose(1, 0)], dim=1)
        inv_scale = math.sqrt(k.size(1))
        scaled_dot_product = (torch.matmul(q, k.transpose((- 2), (- 1))) / inv_scale)
        attention_weights = scaled_dot_product.softmax(dim=(- 1))
        output = attention_weights.matmul(self.key.transpose(0, 1))
        return output




func = Model().to('cuda')



x1 = torch.randn(32, 16, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (32768x64 and 16x16)

jit:
Failed running call_function <built-in method matmul of type object at 0x787626a699e0>(*(FakeTensor(..., device='cuda:0', size=(32, 16, 64, 64)), FakeTensor(..., device='cuda:0', size=(16, 16))), **{}):
a and b must have same reduction dim, but got [32768, 64] X [16, 16].

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''