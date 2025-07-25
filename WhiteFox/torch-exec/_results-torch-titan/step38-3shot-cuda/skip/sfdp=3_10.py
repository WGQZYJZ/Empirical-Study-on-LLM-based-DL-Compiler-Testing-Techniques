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

    def __init__(self, *, dim, heads, dropout):
        super().__init__()
        self.scale_factor = np.sqrt(dim)
        self.query = torch.nn.Linear(dim, dim)
        self.key = torch.nn.Linear(dim, dim)
        self.value = torch.nn.Linear(dim, dim)
        self.dropout = torch.nn.Dropout(dropout)
        self.out = nn.Linear(dim, dim)

    def forward(self, x, context):
        q = self.query(x)
        k = self.key(context)
        v = self.value(context)
        q = q.view((- 1), heads, dim)
        k = k.view((- 1), heads, dim)
        v = v.view((- 1), heads, dim)
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        scaled_qk = (qk * self.scale_factor)
        softmax_qk = torch.softmax(scaled_qk, dim=(- 1))
        dropout_qk = self.dropout(softmax_qk)
        output = (dropout_qk @ v)
        return self.out(output)



func = Model(dim=dim_model, heads=heads, dropout=dropout).to('cuda')



dim = 32


x = torch.randn(8, 8, dim)



dim_context = 32


context = torch.randn(8, 4, dim_context)


test_inputs = [x, context]
