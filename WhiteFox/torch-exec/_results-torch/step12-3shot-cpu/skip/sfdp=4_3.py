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

class MultiHeadedAttn(nn.Module):

    def __init__(self, model_dim, num_heads):
        super().__init__()
        self.d_k = model_dim // num_heads
        self._num_heads = num_heads
        self.linears = clones(nn.Linear(model_dim, model_dim), 4)

    def forward(self, query, key, value, mask=None):
        r


model_dim = 1
num_heads = 1

func = MultiHeadedAttn(model_dim, num_heads).to('cpu')

query = 1
key = 1
value = 1

test_inputs = [query, key, value]
