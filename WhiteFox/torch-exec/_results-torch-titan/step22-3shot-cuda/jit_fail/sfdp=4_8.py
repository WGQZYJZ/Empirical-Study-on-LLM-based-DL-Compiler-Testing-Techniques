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

    def forward(self, query, key, value, attn_mask):
        s1 = (query @ key.transpose((- 2), (- 1)))
        s2 = (s1 / math.sqrt(query.size((- 1))))
        s2 = (s2 + attn_mask)
        output = (torch.nn.functional.softmax(s2, dim=(- 1)) @ value)
        return output



func = Model().to('cuda')



__query__ = torch.randn(1, 6, 7)



__key__ = torch.randn(1, 5, 7)



__value__ = torch.randn(1, 5, 6)



__attn_mask__ = torch.randn(1, 5, 6)


test_inputs = [__query__, __key__, __value__, __attn_mask__]

# JIT_FAIL
'''
direct:
The size of tensor a (5) must match the size of tensor b (6) at non-singleton dimension 2

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 6, 5)), FakeTensor(..., device='cuda:0', size=(1, 5, 6))), **{}):
Attempting to broadcast a dimension of length 6 at -1! Mismatching argument at index 1 had torch.Size([1, 5, 6]); but expected shape should be broadcastable to [1, 6, 5]

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''