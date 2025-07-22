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

    def __init__(self, dim, n_head, dropout_p):
        super().__init__()
        self.dim_head = dim_head
        self.n_head = n_head
        self.scale_factor = (self.dim_head ** (- 0.5))
        self.emb_proj_k = torch.nn.Linear(in_dim, (self.dim_head * self.n_head))
        self.emb_proj_q = torch.nn.Linear(in_dim, (self.dim_head * self.n_head))
        self.emb_proj_v = torch.nn.Linear(in_dim, (self.dim_head * self.n_head))
        self.attention = torch.nn.MultiheadAttention((self.dim_head * self.n_head), self.n_head, dropout_p)

    def forward(self, x_emb_k, x_emb_q, x_emb_v):
        q = self.emb_proj_q(x_emb_q)
        k = self.emb_proj_k(x_emb_k)
        v = self.emb_proj_v(x_emb_v)
        q = q.reshape(B, self.n_head, s_len, self.dim_head)
        k = k.reshape(B, self.n_head, s_len, self.dim_head)
        v = v.reshape(B, self.n_head, s_len, self.dim_head)
        q = q.transpose(2, 1)
        k = k.transpose(2, 1)
        v = v.transpose(2, 1)
        q = (q * self.scale_factor)
        k = k
        v = v
        (attn, output) = self.attention(q, k, v)
        attn = attn.transpose(2, 1)
        output = output.reshape((B, (nhead * self.dim_head), s_len))
        output = self.dropout(output)
        return output



dim = 1

n_head = 4


dropout_p = 0.2

func = Model(d_model, n_head, dropout_p).to('cuda')

x_emb_k = 1
x_emb_q = 1
x_emb_v = 1

test_inputs = [x_emb_k, x_emb_q, x_emb_v]
