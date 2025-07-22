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

class ComputeAttention(nn.Module):

    def __init__(self, dropout):
        super().__init__()
        self.dropout = torch.nn.Dropout(dropout)
        self.softmax1 = torch.nn.Softmax(dim=-1)

    def forward(self, query, key, value, scale):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.div(scale)
        softmax_qk = self.softmax1(scaled_qk)
        dropout_qk = self.dropout(softmax_qk)
        output = torch.matmul(dropout_qk, value)
        return (output, dropout_qk)

class Model(nn.Module):

    def __init__(self, input_dim, output_dim, dropout=0.2):
        super().__init__()
        self.conv1 = nn.Conv1d(input_dim, 1000, 1)
        self.preact_layernorm = nn.LayerNorm(1000, eps=layer_norm_eps)
        self.self_attention = ComputeAttention(dropout)
        self.conv2 = nn.Conv1d(1000, output_dim, 1)

    def forward(self, x):
        h1 = self.conv1(x)
        h1_preact = self.preact_layernorm(h1)
        (h2, _) = self.self_attention(h1_preact, h1_preact, h1, scale=1000 ** (-1) / 2.0)
        out = self.conv2(h2)
        return out


input_dim = 1
output_dim = 1

func = Model(input_dim, output_dim).to('cpu')


x = torch.randn(13, 14, 7).cuda()

test_inputs = [x]
