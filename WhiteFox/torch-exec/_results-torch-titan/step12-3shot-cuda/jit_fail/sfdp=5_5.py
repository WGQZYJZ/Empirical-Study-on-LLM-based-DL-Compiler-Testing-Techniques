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
        self.attention_mask = torch.ones((8 * 2), (8 * 2))

    def forward(self, q, k, v):
        attn = torch.matmul(q, k.transpose((- 1), (- 2)))
        attn = (attn / math.sqrt(8))
        attn = (attn + self.attention_mask)
        attn = attn.softmax(dim=(- 1))
        attn = F.dropout(attn, 0.3)
        output = torch.matmul(attn, v)
        return output



func = Model().to('cuda')



x1 = torch.randn((64 * 2), 8)



x2 = torch.randn((64 * 2), 8)



x3 = torch.randn((64 * 2), 8)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
The size of tensor a (128) must match the size of tensor b (16) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(128, 128)), FakeTensor(..., device='cuda:0', size=(16, 16))), **{}):
Attempting to broadcast a dimension of length 16 at -1! Mismatching argument at index 1 had torch.Size([16, 16]); but expected shape should be broadcastable to [128, 128]

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''