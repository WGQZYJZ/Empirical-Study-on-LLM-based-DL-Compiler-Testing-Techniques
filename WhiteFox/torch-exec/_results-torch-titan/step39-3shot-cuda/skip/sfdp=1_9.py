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
        self.embedding_dim = embedding_dim
        self.num_heads = num_heads
        self.dropout_prob = dropout_p
        self.total_key_depth = (self.num_heads * self.embedding_dim)
        self.total_value_depth = (self.num_heads * self.embedding_dim)
        self.input_depth = (total_key_depth + total_value_depth)
        self.qkv_transform = torch.nn.Linear(total_key_depth, (3 * self.total_value_depth))

    def forward(self, q):
        qkv = self.qkv_transform(q)
        qkv = torch.chunk(qkv, 3, dim=(- 1))
        q = qkv[0]
        k = qkv[1]
        v = qkv[2]
        return (q, k, v)



func = Model().to('cuda')



q = torch.randn(1, 1, 256)


test_inputs = [q]
