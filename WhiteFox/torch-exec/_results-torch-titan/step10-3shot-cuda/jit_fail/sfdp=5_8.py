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



class Transformer(nn.Module):

    def forward(self, query, key, value, attn_mask, dropout_p=0.0):
        bsz = query.size(0)
        len_q = query.size(1)
        bsz = key.size(0)
        len_k = key.size(1)
        bsz = value.size(0)
        len_v = value.size(1)
        _____ = torch.bmm(query, key.transpose(1, 2))
        query = query.view(bsz, len_q, 1, ______).repeat(1, 1, len_k, 1)
        key = key.view(bsz, 1, len_k, ______).repeat(1, len_q, 1, 1)
        dks = (______ + ______)
        dks = (dks / math.sqrt(_______.size(dim=(- 1))))
        dks = (dks + ______)
        ______ = F.softmax(______, dim=(- 1))
        ______ = (______ * ______)
        ______ = F.dropout(______, p=dropout_p, training=self.training)
        ______ = torch.bmm(______, value)
        ______ = ______.view(bsz, len_q, len_v)
        return _______



func = Transformer().to('cuda')



query = torch.randn(8, 16, 128)



key = torch.randn(8, 64, 256)



value = torch.randn(8, 64, 16)



attn_mask = torch.tensor([[1, 0, 1], [1, 0, 0], [0, 1, 1]])


test_inputs = [query, key, value, attn_mask]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [8, 128] but got: [8, 256].

jit:
Failed running call_function <built-in method bmm of type object at 0x7137080699e0>(*(FakeTensor(..., device='cuda:0', size=(8, 16, 128)), FakeTensor(..., device='cuda:0', size=(8, 256, 64))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [8, 128] but got: [8, 256].

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''