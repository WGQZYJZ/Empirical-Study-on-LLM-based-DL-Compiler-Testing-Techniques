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

class MultiHeadAttention(nn.Module):

    def __init__(self, d_model: int, n_heads: int):
        super(MultiHeadSelfAttention, self).__init__()
        self.n_heads = n_heads
        self.d_head = d_model // n_heads
        self.query_proj = nn.Linear(d_model, d_model)
        self.key_proj = nn.Linear(d_model, d_model)
        self.value_proj = nn.Linear(d_model, d_model)
        self.out_proj = nn.Linear(d_model, d_model)

    def forward(self, x, mask=None):
        (B, T, _) = x.size()
        xq = self.query_proj(x).view(B, T, self.n_heads, self.d_head).transpose(2, 1)
        xk = self.key_proj(x).view(B, T, self.n_heads, self.d_head).transpose(2, 1)
        v = self.value_proj(x).view(B, T, self.n_heads, self.d_head).transpose(2, 1)
        scores = q @ k.transpose(-2, -1) / math.sqrt(self.d_head)
        if mask is not None:
            scores += mask
        attn = torch.softmax(scores, dim=-1)
        context = attn @ v
        context = context.transpose(2, 1).contiguous().view(B, T, self.n_heads * self.d_head)
        return self.out_proj(context)


d_model = 1
n_heads = 1

func = MultiHeadAttention(d_model, n_heads).to('cpu')


x = torch.randn(1, 60, 512)


mask = torch.full((1, 60, 60), float('-inf'))

test_inputs = [x, mask]
