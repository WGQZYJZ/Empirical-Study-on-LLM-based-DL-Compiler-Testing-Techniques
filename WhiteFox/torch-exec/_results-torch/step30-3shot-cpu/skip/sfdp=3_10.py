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
        self.attention = torch.nn.MultiheadAttention(n_head, d_model, dropout_p)

    def forward(self, query, key, value):
        (vq, vv) = self.attention(query, key, value)
        return vq



func = Model().to('cpu')


d_model = 10
query = torch.randn(10, 30, d_model)

d_model = 10
key = torch.randn(20, 30, d_model)

d_model = 10
value = torch.randn(20, 30, d_model)

test_inputs = [query, key, value]
