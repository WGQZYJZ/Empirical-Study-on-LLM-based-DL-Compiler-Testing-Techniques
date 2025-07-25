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

    class Config(NamedTuple):
        dropout_p: float
        in_features: int
        num_heads: int

    def __init__(self, dropout_p, in_features, num_heads):
        super().__init__()
        self.dropout_p = dropout_p
        self.in_features = in_features
        self.num_heads = num_heads
        self.head_dim = in_features // num_heads
        self.dropout = torch.nn.Dropout(dropout_p)
        self.query = torch.nn.Parameter(torch.randn(in_features))
        self.key = torch.nn.Parameter(torch.randn(num_heads, self.head_dim))
        self.value = torch.nn.Parameter(torch.randn(num_heads, self.head_dim))
        self.scaled_dot_product = ScaledDotProduct()

    def forward(self, x):
        q = self.query.view(self.num_heads, 1, self.head_dim)
        k = self.key
        v = self.value
        q = torch.matmul(q, k)
        q = q / np.sqrt(self.head_dim)
        q = self.dropout(q)
        y = self.scaled_dot_product(q, x)
        return y


dropout_p = 1
in_features = 1
num_heads = 1

func = Model(dropout_p, in_features, num_heads).to('cpu')


x = torch.randn(3, 1, 10)

test_inputs = [x]
