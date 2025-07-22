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

    def __init__(self, size, dropout_p):
        super(Model, self).__init__()
        num_heads = 2
        head_dim = (size / num_heads)




class MultiHeadAttention(nn.Module):

    def __init__(self, model_dim: int, num_heads: int, dropout, bias: bool=False):
        super(MultiHeadAttention, self).__init__()
        self._size_per_head = (model_dim // num_heads)
        self._num_heads = num_heads
        self.scale_factor = (self._size_per_head ** (- 0.5))
        self.dropout = nn.Dropout(dropout)
        self.q_net = nn.Linear(model_dim, model_dim, bias=bias)
        self.k_neat = nn.Linear(model_dim, model_dim, bias=bias)
        self.v_net = nn.Linear(model_dim, model_dim, bias=bias)
        self.out_proj = nn.Linear(model_dim, model_dim, bias=bias)

    def forward(self, q: Tensor, k: Tensor, v: Tensor):
        residual = q
        q = self.q_net(q)
        k = self.k_net(k)
        v = self.v_net(v)
        q *= (self._size_per_head ** (- 0.5))
        q = self._reshape_heads(x)
        attn_output = self.attention(q, k, v).transpose(0, 1).contiguous().view(tgt_len, bsz, embed_dim)
        return attn_output

    def attention(self, q_heads: Tensor, k_heads: Tensor, v_heads: Tensor) -> Tensor:
        x = self.scaled_dot_product_attention(q_heads, k_heads, v_heads)
        x = self.dropout(x)
        return x

    def scaled_dot_product_attention(self, q_heads: Tensor, k_heads: Tensor, v_heads: Tensor) -> Tensor:
        x = torch.matmul(q_heads, k_heads.transpose((- 2), (- 1)))
        x *= self.scale_factor
        x = torch.nn.functional.softmax(x)
        x = self.dropout(x)
        return torch.matmul(x, v_heads)

    def _reshape_heads(self, x: Tensor) -> Tensor:
        x = x.view(*x.size()[:(- 1)], self._num_heads, self._size_per_head)
        return x



model_dim = 1
num_heads = 1
dropout = 1

func = MultiHeadAttention(model_dim, num_heads, dropout).to('cuda')

q = 1
k = 1
v = 1

test_inputs = [q, k, v]
