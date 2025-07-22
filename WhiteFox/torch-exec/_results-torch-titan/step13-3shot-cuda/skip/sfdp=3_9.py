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

    def __init__(self, hidden_size, dropout_p=0.05, scale_factor=(1 / (hidden_size ** 0.4))):
        super(MultiHeadAttention, self).__init__()
        self.hidden_size = hidden_size
        self.dropout_p = dropout_p
        self.proj = Linear(hidden_size, hidden_size)
        self.dropout = nn.Dropout(p=dropout_p)
        self.softmax = nn.Softmax(dim=(- 1))
        self.scale_factor = scale_factor

    def forward(self, queries, keys, values):
        query_proj = self.proj(queries)
        key_proj = self.proj(keys)
        queries_and_keys = self.dropout((query_proj.unsqueeze((- 2)) + key_proj.unsqueeze((- 3))))
        attention_weights = (self.scale_factor * queries_and_keys.sum((- 1)))
        attention_weights = self.softmax(attention_weights).unsqueeze((- 1))
        scores = torch.matmul(attention_weights, values).squeeze((- 1))
        return scores



hidden_size = 1

func = Model(hidden_size).to('cuda')



x1 = torch.randn(2, 1284, 3136)



x2 = torch.randn(2, 1284, 3136)



x3 = torch.randn(2, 1284, 3136)


test_inputs = [x1, x2, x3]
