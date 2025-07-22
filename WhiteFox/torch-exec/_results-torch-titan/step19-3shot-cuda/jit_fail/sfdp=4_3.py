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
        self.qkv = torch.nn.Linear(64, 1024)

    def forward(self, x):
        qkv = self.qkv(x).reshape(1, 4, 32, (- 1))
        q = qkv[0:1, 0:1]
        k = qkv[0:1, 1:2]
        v = qkv[0:1, 2:3]
        q = (q * (1.0 / math.sqrt(q.size((- 1)))))
        attn_mask = torch.tensor([[[(- 10000.0), 0.0, 0.0, 0.0], [0.0, (- 10000.0), 0.0, 0.0], [0.0, 0.0, (- 10000.0), 0.0], [0.0, 0.0, 0.0, (- 10000.0)]]])
        attn_weight = torch.nn.functional.softmax((torch.matmul(q, torch.transpose(k, (- 2), (- 1))) + attn_mask), dim=(- 1))
        output = torch.matmul(attn_weight, v)
        return output



func = Model().to('cuda')



x = torch.randn(4, 3, 64)


test_inputs = [x]

# JIT_FAIL
'''
direct:
The size of tensor a (32) must match the size of tensor b (4) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 1, 32, 32)), FakeTensor(..., size=(1, 4, 4))), **{}):
Attempting to broadcast a dimension of length 4 at -1! Mismatching argument at index 1 had torch.Size([1, 4, 4]); but expected shape should be broadcastable to [1, 1, 32, 32]

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''