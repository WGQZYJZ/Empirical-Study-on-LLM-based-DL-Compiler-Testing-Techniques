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



class Attention(torch.nn.Module):

    def __init__(self, num_heads, embedding_dim, dropout=0.1):
        super().__init__()
        self.num_heads = num_heads
        self.embedding_dim = embedding_dim
        self.dropout = dropout
        self.query = torch.nn.Parameter(torch.empty(embedding_dim, num_heads))
        self.key = torch.nn.Parameter(torch.empty(embedding_dim, num_heads))
        self.value = torch.nn.Parameter(torch.empty(embedding_dim, num_heads))
        torch.nn.init.kaiming_normal_(self.query)
        torch.nn.init.kaiming_normal_(self.key)
        torch.nn.init.kaiming_normal_(self.value)
        self.scale_factor = float(torch.sqrt(math.sqrt(embedding_dim)))
        self.dropout_layer = nn.Dropout(dropout)

    def forward(self, query, key, value, mask=None):
        N = query.shape[0]
        q = torch.matmul(query, self.query)
        k = torch.matmul(key, self.key)
        v = torch.matmul(value, self.value)
        q = (q / self.scale_factor)
        k = (k / self.scale_factor)
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        if (mask is not None):
            qk = qk.masked_fill((mask.unsqueeze(1).unsqueeze(1) == 0), (- 100000000.0))
        qk = torch.nn.functional.softmax(qk, dim=(- 1))
        qk = self.dropout_layer(qk)
        qkv = torch.matmul(qk, v).reshape(N, (- 1), (self.num_heads * self.embedding_dim))
        return qkv



num_heads = 1
embedding_dim = 1

func = Attention(num_heads, embedding_dim).to('cuda')



x1 = torch.randn(6, 196, 32)



x2 = torch.randn(6, 196, 32)



x3 = torch.randn(6, 196, 32)



mask = torch.randn(6, 196)


test_inputs = [x1, x2, x3, mask]
