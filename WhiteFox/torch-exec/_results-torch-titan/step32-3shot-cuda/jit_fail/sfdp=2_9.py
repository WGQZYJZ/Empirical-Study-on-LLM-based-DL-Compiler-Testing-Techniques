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
        self.query_projection = torch.nn.Linear(768, 214)
        self.key_projection = torch.nn.Linear(768, 214)
        self.value_projection = torch.nn.Linear(768, 768)

    def forward(self, x1, x2, x3):
        q = self.query_projection(x1)
        k = self.key_projection(x2)
        v = self.value_projection(x3)
        attn = torch.matmul(q, k.transpose((- 2), (- 1)))
        inv_scale_factor = (torch.FloatTensor(self.key_projection.weight.size()).uniform_() + 1)
        scaled_attn = attn.div(inv_scale_factor)
        softmax_attn = scaled_attn.softmax(dim=(- 1))
        dropout_attn = torch.nn.functional.dropout(softmax_attn, p=dropout_p)
        output = dropout_attn.matmul(v)
        return output



func = Model().to('cuda')



x1 = torch.randn(8, 8, 768)



x2 = torch.randn(8, 8, 768)



x3 = torch.randn(214, 8, 768)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
The size of tensor a (8) must match the size of tensor b (768) at non-singleton dimension 2

jit:
Failed running call_method div(*(FakeTensor(..., device='cuda:0', size=(8, 8, 8)), FakeTensor(..., size=(2,))), **{}):
Attempting to broadcast a dimension of length 2 at -1! Mismatching argument at index 1 had torch.Size([2]); but expected shape should be broadcastable to [8, 8, 8]

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''