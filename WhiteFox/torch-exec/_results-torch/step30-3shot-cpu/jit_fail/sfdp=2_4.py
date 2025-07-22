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

    def __init__(self, hparams):
        super().__init__()
        n_heads = 1
        dim = 28
        n = 12
        self.in_proj_weight_qkv = torch.nn.Parameter(torch.randn(n_heads, dim, n))
        self.pos_proj_weight_qkv = torch.nn.Parameter(torch.randn(n_heads, dim, n))
        self.in_proj_bias_qkv = torch.nn.Parameter(torch.randn(n_heads, dim))
        self.pos_proj_bias_qkv = torch.nn.Parameter(torch.randn(n_heads, dim))
        dropout_p = 0.5
        scale_factor_init = math.sqrt(n)
        self.pos_proj_weight_dropout = torch.nn.Parameter(torch.from_numpy(np.full((dim, dim), 1 / scale_factor_init)))
        self.pos_proj_bias_dropout = torch.nn.Parameter(torch.full((dim,), 1 / scale_factor_init))

    def _scaled_matmul(self, x1, weight, scale):
        return x1.matmul(weight).mul(scale)

    def forward(self, query, key, value):
        head_dim = query.shape[-1]
        (in_proj_weight_q, in_proj_weight_k, in_proj_weight_v) = self.in_proj_weight_qkv.chunk(3)
        q = query.matmul(in_proj_weight_q).div(head_dim)
        k = key.matmul(in_proj_weight_k).div(head_dim)
        v = value.matmul(in_proj_weight_v).div(head_dim)
        dropout_p = 0.5
        pos_proj_weight_dropout = self.pos_proj_weight_dropout.div(head_dim)
        pos_proj_bias_dropout = self.pos_proj_bias_dropout.div(head_dim)
        q = self._scaled_matmul(q, pos_proj_weight_dropout, pos_proj_bias_dropout)
        k = self._scaled_matmul(k, pos_proj_weight_dropout, pos_proj_bias_dropout)
        v = self._scaled_matmul(v, pos_proj_weight_dropout, pos_proj_bias_dropout)
        qk = q.matmul(k.transpose(-2, -1))
        dropout_p = 0.5
        pos_proj_weight_qkv = self.pos_proj_weight_qkv.div(head_dim)
        pos_proj_bias_qkv = self.pos_proj_bias_qkv.div(head_dim)
        qk = self._scaled_matmul(qk, pos_proj_weight_qkv, pos_proj_bias_qkv)
        softmax_qk = qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v)
        return output


hparams = 1

func = Model(hparams).to('cpu')

num_qkv_attention_heads = 2
dim = 3

n = 5
num_qkv_attention_heads = 2
batch_size = 3
query = torch.randn(batch_size, num_qkv_attention_heads, dim * num_qkv_attention_heads, n)
num_qkv_attention_heads = 2
dim = 3

n = 5
num_qkv_attention_heads = 2
batch_size = 3
key = torch.randn(batch_size, num_qkv_attention_heads, dim * num_qkv_attention_heads, n)
num_qkv_attention_heads = 2
dim = 3

n = 5
num_qkv_attention_heads = 2
batch_size = 3
value = torch.randn(batch_size, num_qkv_attention_heads, dim * num_qkv_attention_heads, n)

test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
not enough values to unpack (expected 3, got 1)

jit:
not enough values to unpack (expected 3, got 1)
'''