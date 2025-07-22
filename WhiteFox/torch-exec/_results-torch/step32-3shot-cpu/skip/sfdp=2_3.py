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

    def __init__(self, size, number_heads, projection_size, dropout_p):
        super().__init__()
        self.size = size
        self.number_heads = number_heads
        self.projection_size = projection_size
        self.scale_factor = 1
        if encoder_normalize_before:
            self.scale_factor = self.scale_factor / (self.number_heads * math.sqrt(self.size))
        self.projection = torch.nn.Linear(size, projection_size, bias=False)
        self.dropout = torch.nn.Dropout(dropout_p)

    def forward(self, query, key, value, mask=None):
        v1 = torch.matmul(query, key.transpose(-2, -1))
        v2 = v1 * self.scale_factor
        v3 = F.softmax(v2, dim=-1)
        v4 = self.dropout(v3)
        v5 = torch.matmul(v4, value)
        return v5


size = 1
number_heads = 1
projection_size = 1
dropout_p = 1

func = Model(size, number_heads, projection_size, dropout_p).to('cpu')


query = torch.randn(1, 32, 16)

key = torch.randn(1, 32, 16)

value = torch.randn(1, 32, 16)

test_inputs = [query, key, value]
