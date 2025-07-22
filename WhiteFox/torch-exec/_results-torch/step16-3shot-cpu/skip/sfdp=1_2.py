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

class Model(nn.Module):

    def __init__(self, dim_in):
        super().__init__()
        self.dim_in = dim_in
        self.m = nn.MultiHeadAttention(dim_in, 1)

    def forward(self, q1, k2, v3, inv_scale_factor=None, dropout_p=0.0):
        q = q1.transpose(-2, -1)
        v = v3.transpose(-2, -1)
        output = self.m(q, k2, v, attn_mask=None, key_padding_mask=None, need_weights=False, static_k=None, static_v=None)[0]
        return output


dim_in = 64
func = Model(dim_in).to('cpu')


dim_in = 64
q1 = torch.randn(1, 64, dim_in)

dim_in = 64
k2 = torch.randn(1, 16, dim_in)

dim_in = 64
v3 = torch.randn(1, 16, dim_in)

test_inputs = [q1, k2, v3]
