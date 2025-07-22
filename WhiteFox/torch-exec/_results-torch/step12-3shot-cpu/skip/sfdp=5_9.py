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
        self.linear_query = torch.nn.Linear(feature_size, feature_size)
        self.linear_key = torch.nn.Linear(feature_size, feature_size)
        self.linear_value = torch.nn.Linear(feature_size, feature_size)
        self.dropout = torch.nn.Dropout(dropout_p)
        self.layernorm1 = torch.nn.LayerNorm(feature_size)
        self.layernorm2 = torch.nn.LayerNorm(feature_size)

    def forward(self, q, k, v, attn_mask):
        q = rearrange(self.linear_query(q), 'b n (h d) -> b h n d', h=h)
        k = rearrange(self.linear_key(k), 'b n (h d) -> b h n d', h=h)
        v = rearrange(self.linear_value(v), 'b n (h d) -> b h n d', h=h)
        attn_mask = repeat(attn_mask, 's s -> b h s s', b=b, h=h)
        attn = q @ k.transpose(-2, -1) / math.sqrt(q.size(-1))
        attn = attn + attn_mask
        attn_weight = torch.softmax(attn, dim=-1)
        attn_weight = rearrange(self.dropout(attn_weight), 'b h n s -> b n (h s)')
        output = attn_weight @ v
        output = rearrange(output, 'b n (h d) -> b n h d', h=h)
        output = self.layernorm1(output + q)
        output = rearrange(self.dropout(output), 'b n h d -> b (n h) d')
        output = self.layernorm2(output + k)
        output = rearrange(self.dropout(output), 'b (n h) d -> b n h d', n=seq_len)
        output = output + v
        return output


func = Model().to('cpu')

q = 1
k = 1
v = 1
attn_mask = 1

test_inputs = [q, k, v, attn_mask]
