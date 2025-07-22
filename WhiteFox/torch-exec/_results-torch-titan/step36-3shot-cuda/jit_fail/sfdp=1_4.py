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



class Relative_Attention(nn.Module):

    def __init__(self, query_dim, key_dim, n_heads):
        super().__init__()
        self.wq = nn.Linear(query_dim, (n_heads * key_dim))
        self.wk = nn.Linear(key_dim, (n_heads * key_dim))
        self.wv = nn.Linear(key_dim, (n_heads * key_dim))
        self.wo = nn.Linear((n_heads * key_dim), (n_heads * key_dim))

    def forward(self, x_q, x_k, x_v):
        q = self.wq(x_q).chunk(self.n_heads, dim=(- 1))
        k = self.wk(x_k).chunk(self.n_heads, dim=(- 1))
        v = self.wv(x_v).chunk(self.n_heads, dim=(- 1))
        attn_score = []
        q_t = q[0].transpose((- 1), (- 2))
        for k_t in k:
            attn_score.append((q_t @ k_t.transpose((- 1), (- 2))))
        attn = torch.cat(attn_score)
        attn = F.softmax(attn, dim=(- 1))
        attn = F.dropout(attn, p=dropout_p)
        output = []
        v_t = v[0].transpose((- 2), (- 1))
        for attn_t in attn:
            output.append((attn_t @ v_t))
        output = torch.cat(output)
        output = output.transpose((- 2), (- 1))
        return self.wo(output)




class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.relative_attention = Relative_Attention(64, 64, 2)

    def forward(self, x1, x2, x3):
        q = torch.randn(1, 2, 1, 64)
        k = torch.randn(1, 2, 10, 64)
        v = torch.randn(1, 2, 10, 64)
        v1 = self.relative_attention(q, k, v)
        return v1



func = Model().to('cuda')



x1 = torch.randn(1, 2, 64)



x2 = torch.randn(1, 2, 10, 64)



x3 = torch.randn(1, 2, 10, 64)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu! (when checking argument for argument mat1 in method wrapper_CUDA_addmm)

jit:
Failed running call_module L__self___relative_attention_wq(*(FakeTensor(..., size=(1, 2, 1, 64)),), **{}):
Unhandled FakeTensor Device Propagation for aten.mm.default, found two different devices cpu, cuda:0

from user code:
   File "<string>", line 56, in forward
  File "/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl
    return forward_call(*args, **kwargs)
  File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''