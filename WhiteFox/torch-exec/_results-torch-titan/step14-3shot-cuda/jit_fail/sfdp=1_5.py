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

    def __init__(self, num_heads, dim_key, dim_value):
        super().__init__()
        self.norm1 = torch.nn.LayerNorm(dim_key)
        self.softmax = torch.nn.Softmax(dim=(- 1))
        self.attn_dropout = torch.nn.Dropout(0.1)
        self.attn_layer = torch.nn.Linear(dim_key, dim_value)
        self.norm2 = torch.nn.LayerNorm(dim_key)
        self.mlp1 = torch.nn.Linear(dim_key, dim_key)
        self.mlp_dropout1 = torch.nn.Dropout(0.1)
        self.mlp2 = torch.nn.Linear(dim_key, dim_key)
        self.mlp_dropout2 = torch.nn.Dropout(0.1)
        self.apply(self._init_weights)

    def forward(self, x1, x2):
        x1_ = self.norm1(x1)
        x2_ = self.norm1(x2)
        (query, _) = torch.chunk(x1_, 2, dim=(- 1))
        (key, _) = torch.chunk(x2_, 2, dim=(- 1))
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = qk.div(10)
        softmax_qk = self.softmax(scaled_qk)
        dropout_qk = self.attn_dropout(softmax_qk)
        attn = self.attn_layer(dropout_qk)
        x1_new = torch.cat([x1, attn], dim=(- 1))
        x1_new = (x1_new + x1_)
        mlp = nn.functional.gelu(x1_new)
        x2_ = self.norm2(mlp)
        mlp = (x2_ + x2)
        mlp = self.mlp1(x2_)
        mlp = self.mlp_dropout1(mlp)
        mlp = self.mlp2(mlp)
        mlp = (mlp + x2_)
        return mlp

    def _init_weights(self, module):
        if isinstance(module, (nn.Linear, nn.Embedding)):
            module.weight.data.normal_(mean=0.0, std=0.02)
        if isinstance(module, nn.Linear):
            module.bias.data.zero_()



num_heads = 1
dim_key = 1
dim_value = 1

func = Model(num_heads, dim_key, dim_value).to('cuda')



x1 = torch.randn(1, 64, 2)



x2 = torch.randn(1, 64, 4)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Given normalized_shape=[1], expected input with shape [*, 1], but got input of size[1, 64, 2]

jit:
Failed running call_module L__self___norm1(*(FakeTensor(..., device='cuda:0', size=(1, 64, 2)),), **{}):
Given normalized_shape=[1], expected input with shape [1], but got input of size torch.Size([1, 64, 2])

from user code:
   File "<string>", line 31, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''