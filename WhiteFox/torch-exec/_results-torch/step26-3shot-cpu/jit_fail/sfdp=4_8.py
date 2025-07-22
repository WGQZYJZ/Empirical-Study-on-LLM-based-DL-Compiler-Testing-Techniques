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

    def forward(self, q, k, v, attn_mask):
        result = torch.nn.functional.normalize(q, p=2, dim=1) @ torch.transpose(torch.nn.functional.normalize(k, p=2, dim=1), -2, -1)
        return result @ v + attn_mask


func = Model().to('cpu')


q = torch.randn(1, 5, 15)

k = torch.randn(1, 5, 20)

v = torch.randn(1, 20, 15)


attn_mask = torch.randn(15, 20).to(torch.bool)

test_inputs = [q, k, v, attn_mask]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 15] but got: [1, 20].

jit:
Failed running call_function <built-in function matmul>(*(FakeTensor(..., size=(1, 5, 15)), FakeTensor(..., size=(1, 20, 5))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 15] but got: [1, 20].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''