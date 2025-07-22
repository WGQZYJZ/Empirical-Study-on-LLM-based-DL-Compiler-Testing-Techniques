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

    def __init__(self, d_model, num_heads, d_key, d_value, d_inner_hid, num_layers, dropout):
        super().__init__()
        self.slf_attn_mask = None
        self.slf_attn_layer = nn.ModuleList()
        for i in range(num_layers):
            self.slf_attn_layer.append(MultiHeadAttention(d_model, num_heads, d_key, d_value, dropout))

    def set_attn_mask(self, attn_mask):
        self.slf_attn_mask = attn_mask

    def forward(self, x1, x, x2):
        for attn_layer in self.slf_attn_layer:
            x = attn_layer(x1, x, x, attn_mask=self.slf_attn_mask)
        return x



d_model = 1
num_heads = 1
d_key = 1
d_value = 1
d_inner_hid = 1
num_layers = 1
dropout = 1

func = Model(d_model, num_heads, d_key, d_value, d_inner_hid, num_layers, dropout).to('cuda')



x = torch.randn(5, 768, 512)



x1 = torch.randn(5, 768, 512)

x2 = 1

test_inputs = [x, x1, x2]
