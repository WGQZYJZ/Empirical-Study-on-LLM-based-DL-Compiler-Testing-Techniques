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

    def __init__(self, dropout_p=0, out_features=60):
        super().__init__()
        self.dropout_p = dropout_p
        self.w_1 = torch.nn.Linear(10, 10, bias=False)
        self.w_2 = torch.nn.Linear(10, 50, bias=False)
        self.layer_norm = torch.nn.LayerNorm(out_features)

    def forward(self, query, key, value, attn_mask):
        v7 = torch.matmul(query, key.transpose((- 1), (- 2)))
        v8 = (v7 / np.sqrt(10))
        v9 = (v8 + attn_mask)
        v10 = F.softmax(v9, (- 1))
        v11 = F.dropout(v10, self.dropout_p, True)
        v12 = torch.matmul(v11, value)
        v13 = self.layer_norm(v12)
        return v13



func = Model().to('cuda')



__query__ = torch.randn(1, 10)



__key__ = torch.randn(2, 10)



__value__ = torch.randn(2, 5)



__attn_mask__ = torch.rand(2, 2)


test_inputs = [__query__, __key__, __value__, __attn_mask__]

# JIT_FAIL
'''
direct:
Given normalized_shape=[60], expected input with shape [*, 60], but got input of size[2, 5]

jit:
Failed running call_module L__self___layer_norm(*(FakeTensor(..., device='cuda:0', size=(2, 5)),), **{}):
Given normalized_shape=[60], expected input with shape [60], but got input of size torch.Size([2, 5])

from user code:
   File "<string>", line 31, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''