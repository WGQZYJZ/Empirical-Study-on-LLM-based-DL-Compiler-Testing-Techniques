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
        self.key = torch.nn.Parameter(torch.randn(128))

    def forward(self, x1):
        q = x1[:, 0:8, :, :]
        k = x1[:, 8:16, :, :]
        v = x1[:, 16:, :, :]
        w = torch.cat([q, k, v], dim=1)
        inv_scale = math.sqrt(w.size(1))
        scaled_dot_product = (torch.matmul(w, w.transpose((- 2), (- 1))) / inv_scale)
        attention_weights = scaled_dot_product.softmax(dim=(- 1))
        output = attention_weights.matmul(w)
        return output.split(v.size())




func = Model().to('cuda')



x1 = torch.randn(1, 24, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
split_with_sizes expects split_sizes to sum exactly to 1 (input tensor's size at dimension 0), but got split_sizes=[1, 8, 64, 64]

jit:
Failed running call_method split(*(FakeTensor(..., device='cuda:0', size=(1, 24, 64, 64)), (1, 8, 64, 64)), **{}):
Split sizes don't add up to the tensor's size in the given dimension

from user code:
   File "<string>", line 30, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''