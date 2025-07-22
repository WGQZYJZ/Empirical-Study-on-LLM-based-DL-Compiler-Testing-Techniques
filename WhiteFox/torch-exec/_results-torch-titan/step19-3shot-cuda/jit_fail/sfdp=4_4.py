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

    def __init__(self, embed_dim, num_heads, num_levels):
        super().__init__()
        self.embed_dim = embed_dim
        self.num_heads = num_heads
        self.num_levels = num_levels
        self.heads_dim = (embed_dim // num_heads)
        self.scale = (self.heads_dim ** (- 0.5))
        self.proj_q = torch.nn.ModuleList()
        self.proj_k = torch.nn.ModuleList()
        self.proj_v = torch.nn.ModuleList()
        for l in range(num_levels):
            self.proj_q.append(torch.nn.Linear(((l + 1) * self.embed_dim), self.embed_dim))
            self.proj_k.append(torch.nn.Linear(((l + 1) * self.embed_dim), self.embed_dim))
            self.proj_v.append(torch.nn.Linear(((l + 1) * self.embed_dim), self.embed_dim))
        self.out_proj = torch.nn.Linear((num_levels * embed_dim), embed_dim)

    def forward(self, level_input, q_index, k_index, v_index, attn_mask):
        outputs = []
        for (level, inp) in enumerate(level_input):
            (q, k, v) = [linear(inp) for linear in ((self.proj_q[level:(level + 1)] + self.proj_k[level:(level + 1)]) + self.proj_v[level:(level + 1)])]
            q = rearrange(q, 'b n (h d) -> b h n d', h=self.num_heads)
            k = rearrange(k, 'b n (h d) -> b h n d', h=self.num_heads)
            v = rearrange(v, 'b n (h d) -> b h n d', h=self.num_heads)
            if (self.num_levels > 1):
                q = q[:, q_index[level]:q_index[(level + 1)], ...]
                k = k[:, k_index[level]:k_index[(level + 1)], ...]
                v = v[:, v_index[level]:v_index[(level + 1)], ...]
            else:
                q = q[:, q_index, ...]
                k = k[:, k_index, ...]
                v = v[:, v_index, ...]
            norm = (q.size((- 1)) ** (- 0.5))
            q = (q * norm)
            input_mask = attn_mask[:, None, None, :].expand(q.size()).float()
            output = compute_attention(q, k, v, input_mask)
            outputs.append(output)
        (x, output_mask) = pad_and_merge(outputs, q_index)
        output = self.out_proj(x)
        return (output, output_mask)




embed_dim = 128


num_heads = 6


num_levels = 2

func = Model(embed_dim, num_heads, num_levels).to('cuda')



attn_mask = torch.tensor([[0, 0, 0, 0], [1, (- 1), (- 1), (- 1)], [1, (- 1), (- 1), (- 1)], [1, (- 1), (- 1), (- 1)]])

level_input = 1
q_index = 1
k_index = 1
v_index = 1

test_inputs = [attn_mask, level_input, q_index, k_index, v_index]

# JIT_FAIL
'''
direct:
mat1 and mat2 must have the same dtype, but got Long and Float

jit:
mat1 and mat2 must have the same dtype, but got Long and Float
'''