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



class MultiHeadAttention(torch.nn.Module):

    def __init__(self, d_in, d_model, num_heads):
        super().__init__()
        self.d_k = (d_model // num_heads)
        self.num_heads = num_heads
        self.Q = torch.nn.Linear(d_in, d_model, bias=False)
        self.K = torch.nn.Linear(d_in, d_model, bias=False)
        self.V = torch.nn.Linear(d_in, d_in, bias=False)

    def forward(self, x1):
        (_, n, _) = x1.shape
        q = self.Q(x1)
        k = self.K(x1).permute(0, 2, 1)
        v = self.V(x1).permute(0, 2, 1)
        qk = ((q @ k) / math.sqrt(q.size((- 1))))
        attn_weight = torch.softmax(qk, dim=(- 1))
        output = torch.matmul(attn_weight, v)
        return output



d_in = 1
d_model = 1
num_heads = 1
func = MultiHeadAttention(3, 6, 2).to('cuda')



x1 = torch.randn((1, 1, 3))


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 1] but got: [1, 3].

jit:
Failed running call_function <built-in method matmul of type object at 0x7f5c5fc699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 1, 1)), FakeTensor(..., device='cuda:0', size=(1, 3, 1))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 1] but got: [1, 3].

from user code:
   File "<string>", line 32, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''