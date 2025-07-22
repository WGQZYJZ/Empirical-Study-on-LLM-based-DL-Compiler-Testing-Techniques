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
        self.attn_mask = torch.tensor([[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0]])

    def attention(self, Q, K, V, attn_mask):
        attn = torch.matmul(Q, K.transpose((- 2), (- 1)))
        attn = (attn / math.sqrt(Q.size((- 1))))
        attn = (attn + attn_mask[:, None, None, :])
        attn = torch.softmax(attn, dim=(- 1))
        attn = torch.dropout(attn, 0.1, training=True)
        output = torch.matmul(attn, V)
        return (attn, output)

    def forward(self, x1):
        q = x1
        k = x1
        v = x1
        (attn, output) = self.attention(q, k, v, self.attn_mask)
        return output



func = Model().to('cuda')



x1 = torch.randn(2, 4, 8)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (4) must match the size of tensor b (8) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(2, 4, 4)), FakeTensor(..., device='cuda:0', size=(2, 1, 1, 8))), **{}):
Attempting to broadcast a dimension of length 8 at -1! Mismatching argument at index 1 had torch.Size([2, 1, 1, 8]); but expected shape should be broadcastable to [1, 2, 4, 4]

from user code:
   File "<string>", line 34, in forward
  File "<string>", line 24, in attention


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''