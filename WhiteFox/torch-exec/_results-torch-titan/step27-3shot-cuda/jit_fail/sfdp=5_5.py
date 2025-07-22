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
        self.dropout = 0.2
        self.heads = 16
        self.seq_len = 128
        self.dim = (128 // self.heads)

    def forward(self, query, key, value, attn_mask=None):
        attn_mask = torch.zeros(query.shape[0], key.shape[1], key.shape[2], key.shape[2])
        qk = ((query @ key.transpose((- 2), (- 1))) / math.sqrt(query.size((- 1))))
        qk = (qk + attn_mask)
        attn_weight = torch.softmax(qk, dim=(- 1))
        attn_weight = torch.dropout(attn_weight, self.dropout, True)
        output = (attn_weight @ value)
        return output




func = Model().to('cuda')



query = torch.randn(1, 16, 128, 128)



key = torch.randn(1, 16, 128, 128)



value = torch.randn(1, 16, 128, 128)


test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu!

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 16, 128, 128)), FakeTensor(..., size=(1, 16, 128, 128))), **{}):
Unhandled FakeTensor Device Propagation for aten.add.Tensor, found two different devices cuda:0, cpu

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''