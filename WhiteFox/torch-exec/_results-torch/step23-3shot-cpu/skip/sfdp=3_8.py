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

    def __init__(self, dim, heads):
        super().__init__()
        self.scale_factor = 1 / math.sqrt(dim)
        self.dropout_p = 0.2
        self.heads = heads

    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1))
        zscore = qk.mul(self.scale_factor)
        attn_weights = zscore.softmax(dim=-1)
        dout = self.dropout_p
        dropout_attn_weights = torch.nn.functional.dropout(attn_weights, p=dout)
        output = dropout_attn_weights.matmul(value)
        return output


dim = 1
heads = 1
func = Model(input_dim, num_heads).to('cpu')

query = 1
key = 1
value = 1

test_inputs = [query, key, value]
