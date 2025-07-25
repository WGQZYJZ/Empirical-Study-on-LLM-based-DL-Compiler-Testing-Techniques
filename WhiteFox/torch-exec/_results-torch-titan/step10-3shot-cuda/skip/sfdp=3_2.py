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

    def __init__(self, heads_count, hidden_size, dropout_p):
        super().__init__()
        self.heads_count = heads_count
        self.hidden_size = hidden_size
        self.dropout_p = dropout_p
        self.scale_factor = torch.sqrt(torch.FloatTensor([(hidden_size // heads_count)])).to(device)
        self.softmax = torch.nn.Softmax(dim=(- 1))
        self.dropout = torch.nn.Dropout(dropout_p)
        self.w = torch.nn.Linear(hidden_size, hidden_size)
        self.q = torch.nn.Linear(hidden_size, hidden_size)
        self.k = torch.nn.Linear(hidden_size, hidden_size)
        self.v = torch.nn.Linear(hidden_size, hidden_size)

    def transpose_for_scores(self, x):
        new_x_shape = (x.size()[:(- 1)] + (self.heads_count, (self.hidden_size // self.heads_count)))
        x = x.view(*new_x_shape)
        return x.permute(0, 2, 1, 3)

    def forward(self, query, key, value):
        q = self.q(query)
        k = self.k(key)
        v = self.v(value)
        q = q.to(self.scale_factor.device)
        k = k.to(self.scale_factor.device)
        v = v.to(self.scale_factor.device)
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = qk.mul(self.scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = self.dropout(softmax_qk)
        output = torch.matmul(dropout_qk, value)
        return output



heads_count = 1
hidden_size = 1
dropout_p = 1
func = Model(8, 1024, dropout_p).to('cuda')



query = torch.randn(4, 8, 1024)



key = torch.randn(4, 8, 1024)



value = torch.randn(4, 8, 1024)


test_inputs = [query, key, value]
