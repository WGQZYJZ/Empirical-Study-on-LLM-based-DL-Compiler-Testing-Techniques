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

    def __init__(self, dim, num_heads, mlp_ratio):
        super().__init__()
        self.dim = dim
        self.num_heads = num_heads
        self.head_dim = (dim // num_heads)
        self.mlp_ratio = mlp_ratio
        self.norm1 = torch.nn.BatchNorm2d(dim)
        self.norm2 = torch.nn.BatchNorm2d(dim)
        self.att = torch.nn.MultiheadAttention(dim, dim, num_heads)
        self.mlp = torch.nn.Sequential(torch.nn.Conv2d(dim, (dim * mlp_ratio), 1, padding=0), torch.nn.ReLU(), torch.nn.Conv2d((dim * mlp_ratio), dim, 1, padding=0))

    def forward(self, x):
        x = x.transpose(1, (- 1)).contiguous()
        x = x.view((- 1), x.size(1), (x.size(2) * x.size(3)))
        (x1, _) = self.att(x, x, x)
        x1 = x1.view((- 1), x.size(1), x.size(2), x.size(3))
        x1 = x1.transpose(1, (- 1)).contiguous()
        x2 = self.mlp(x.transpose(1, (- 1)).contiguous())
        x2 = x2.transpose(1, (- 1)).contiguous()
        return (self.norm1(x1.reshape(x.shape)) + self.norm2(x2.reshape(x.shape)))




dim = 64


num_heads = 2


mlp_ratio = 1

func = Model(dim, num_heads, mlp_ratio).to('cuda')


dim = 64


seq_len = 32


batch_size = 1



pos_embedding = torch.randn((batch_size, seq_len, dim)).transpose(1, (- 1)).contiguous()


pos_embedding = torch.randn((batch_size, seq_len, dim)).transpose(1, (- 1)).contiguous()


dim = 64


seq_len = 32


x = pos_embedding.transpose(1, 2).reshape((seq_len, (- 1), dim))


test_inputs = [pos_embedding, x]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''