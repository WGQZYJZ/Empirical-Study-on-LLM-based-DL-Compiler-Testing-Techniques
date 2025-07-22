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

    def __init__(self, dim, num_heads, dropout_p):
        super().__init__()
        self.num_heads = num_heads
        self.dim = dim
        self.scaled_dot_product = ScaledDotProductAttention(dim, dropout_p, scale=(1.0 / num_heads))

    def forward(self, query, key, value):
        v1_t = query.transpose((- 2), (- 1))
        v2 = torch.matmul(key, v1_t)
        v3 = v2.div(math.sqrt(self.dim))
        v4 = self.scaled_dot_product(v3, v3, v2)
        return v4



dim = 1
num_heads = 1
dropout_p = 1
func = Model(128, 4, 0.5).to('cuda')



query = torch.randn(4, 4, 128)



key = torch.randn(4, 6, 128)



value = torch.randn(4, 6, 128)


test_inputs = [query, key, value]
