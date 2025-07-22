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

    def __init__(self, n_head, f_in, f_out, mask=None):
        super().__init__()
        self.n_head = n_head
        self.w1 = nn.Linear(f_in, f_out, bias=False)
        self.w2 = nn.Linear(f_in, f_out, bias=False)
        self.w3 = nn.Linear(f_out, f_out, bias=False)
        self.fc = nn.Linear(n_head, f_out)
        self.layer_norm = nn.LayerNorm(f_out, eps=1e-06)
        self.attention_dropout = nn.Dropout(attn_dropout)
        self.dropout = nn.Dropout(dropout)
        self.mask = mask

    def forward(self, x, mask=None):
        q = x
        k = self.w2(dropout(self.layer_norm))
        v = self.w3(dropout(self.layer_norm))
        k = k.view(bsz, self.n_head, k_len, (- 1)).transpose(2, 3)
        v = v.view(bsz, self.n_head, v_len, (- 1)).transpose(2, 3)
        q = q.view(bsz, self.n_head, (- 1), self.d_k).transpose(1, 2)
        attn = ((q @ k) / math.sqrt(k.size((- 1))))
        if (mask is not None):
            attn = (attn + mask)
        attn = relu(attn, inplace=True)
        output = (attn @ v)
        output = output.transpose(1, 2).reshap(bsz, (- 1), (self.h * self.d_k))
        return self.fc(output)



n_head = 1
f_in = 1
f_out = 1
func = MultiHeadAttention(16, 512, 1024, mask=None).to('cuda')



x1 = torch.randn(1, 3, 64, 64)

x = 1

test_inputs = [x1, x]
