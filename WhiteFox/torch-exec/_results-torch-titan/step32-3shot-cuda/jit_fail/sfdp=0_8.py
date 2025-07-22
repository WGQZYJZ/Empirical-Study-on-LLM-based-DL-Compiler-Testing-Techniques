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
        self.k = torch.nn.Parameter(torch.randn(4, 2, 3, 7, 3, 9, 9, 7, 9))
        self.v = torch.nn.Parameter(torch.randn(8, 7, 4, 6, 5, 5, 4, 9, 8))

    def forward(self, x1):
        k = x1
        v = x1
        k = k.reshape(2, 4)
        v = v.reshape(8, 56)
        q = x1
        q = q.reshape(8, 36)
        inv_scale = math.sqrt(k.size(1))
        scaled_dot_product = (torch.matmul(q, k.transpose((- 2), (- 1))) / inv_scale)
        attention_weights = scaled_dot_product.softmax(dim=(- 1))
        output = attention_weights.matmul(v)
        return output




func = Model().to('cuda')



x1 = torch.randn(8, 4, 2, 3, 7, 3, 9, 9, 7, 9)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
shape '[2, 4]' is invalid for input of size 20575296

jit:
Failed running call_method reshape(*(FakeTensor(..., device='cuda:0', size=(8, 4, 2, 3, 7, 3, 9, 9, 7, 9)), 2, 4), **{}):
shape '[2, 4]' is invalid for input of size 20575296

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''