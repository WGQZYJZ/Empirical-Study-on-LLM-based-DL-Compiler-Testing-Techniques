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
        self.key = torch.nn.Parameter(torch.randn(8, 7, 5))
        self.value = torch.nn.Parameter(torch.randn(1, 1, 5))

    def forward(self, x1):
        q = x1
        k = x1
        v = self.value
        inv_scale = math.sqrt(k.size(1))
        scaled_dot_product = (torch.matmul(q, k.transpose((- 2), (- 1))) / inv_scale)
        attention_weights = scaled_dot_product.softmax(dim=(- 1))
        output = attention_weights.matmul(v)
        return output




func = Model().to('cuda')



x1 = torch.randn(1, 8, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 8] but got: [1, 1].

jit:
Failed running call_method matmul(*(FakeTensor(..., device='cuda:0', size=(1, 8, 8)), Parameter(FakeTensor(..., device='cuda:0', size=(1, 1, 5), requires_grad=True))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 8] but got: [1, 1].

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''