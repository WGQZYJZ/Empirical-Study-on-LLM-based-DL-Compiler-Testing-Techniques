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
        self.query = torch.nn.Parameter(torch.randn(89, 1, 101))
        self.key = torch.nn.Parameter(torch.randn(1, 1, 63, 218))
        self.value = torch.nn.Parameter(torch.randn(1, 1, 39, 287))

    def forward(self, x3):
        q = self.query
        k = self.key
        v = self.value
        inv_scale = math.sqrt(k.size(1))
        scaled_dot_product = (torch.matmul(q, k.transpose((- 2), (- 1))) / inv_scale)
        attention_weights = scaled_dot_product.softmax(dim=(- 1))
        output = attention_weights.matmul(v)
        return output




func = Model().to('cuda')



x3 = torch.randn(1, 1, 1, 223)


test_inputs = [x3]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [89, 101] but got: [89, 218].

jit:
Failed running call_function <built-in method matmul of type object at 0x7dab190699e0>(*(Parameter(FakeTensor(..., device='cuda:0', size=(89, 1, 101), requires_grad=True)), FakeTensor(..., device='cuda:0', size=(1, 1, 218, 63), requires_grad=True)), **{}):
Expected size for first two dimensions of batch2 tensor to be: [89, 101] but got: [89, 218].

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''