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
        self.emb_dim = 256
        self.num_heads = 2
        self.attention_head_size = int((self.emb_dim / self.num_heads))
        self.all_head_size = (self.num_heads * self.attention_head_size)
        self.query_proj = torch.nn.Linear(self.emb_dim, self.all_head_size)
        self.key_proj = torch.nn.Linear(self.emb_dim, self.all_head_size)
        self.value_proj = torch.nn.Linear(self.emb_dim, self.all_head_size)
        self.out_proj = torch.nn.Linear(self.all_head_size, self.emb_dim)

    def forward(self, q, k, v, attention_mask=None):
        q = self.query_proj(q)
        k = self.key_proj(k)
        v = self.value_proj(v)
        q = (q / math.sqrt(q.size((- 1))))
        q = q.view(q.size(0), q.size(1), self.num_heads, self.attention_head_size).permute(0, 2, 1, 3)
        k = k.view(k.size(0), k.size(1), self.num_heads, self.attention_head_size).permute(0, 2, 1, 3)
        v = v.view(v.size(0), v.size(1), self.num_heads, self.attention_head_size).permute(0, 2, 1, 3)
        attn_mask = (attention_mask == 0).to(torch.float)
        attn_mask = attn_mask.view(attn_mask.size(0), (- 1))
        attn_mask = attn_mask.unsqueeze(1).unsqueeze(2)
        attn_mask = attn_mask.repeat(1, self.num_heads, q.size(1), 1)
        attn_mask = attn_mask.view((- 1), q.size(1), k.size((- 1)))
        output = torch.matmul(q, k)
        output = (output + attn_mask)
        output = F.softmax(output, dim=(- 1))
        output = output.view(q.size(0), self.num_heads, q.size(1), k.size((- 1)))
        output = output.permute(0, 2, 1, 3)
        output = output.contiguous().view(output.size(0), output.size(1), (- 1))
        output = self.out_proj(output)
        return output



func = Model().to('cuda')



x1 = torch.randn(1, 16, 256)



x2 = torch.randn(1, 16, 256)

q = 1
k = 1

test_inputs = [x1, x2, q, k]

# JIT_FAIL
'''
direct:
linear(): argument 'input' (position 1) must be Tensor, not int

jit:
Failed running call_module L__self___value_proj(*(1,), **{}):
linear(): argument 'input' (position 1) must be Tensor, not int

from user code:
   File "<string>", line 31, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''