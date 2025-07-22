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

    def __init__(self, num_heads, dropout):
        super().__init__()
        self.q_linear = torch.nn.Linear(dim_model, (num_heads * dimension_per_head))
        self.k_linear = torch.nn.Linear(dim_model, (num_heads * dimension_per_head))
        self.v_linear = torch.nn.Linear(dim_model, (num_heads * dimension_per_head))
        self.out_linear = torch.nn.Linear((num_heads * dimension_per_head), dim_model)
        self.dropout1 = torch.nn.Dropout(dropout)
        self.dropout2 = torch.nn.Dropout(dropout)

    def forward(self, x1, x2):
        v1 = self.q_linear(x1)
        v2 = self.k_linear(x2)
        v3 = self.v_linear(x2)
        v4 = torch.matmul(v1, v2.transpose((- 2), (- 1)))
        v5 = (v4 * inv_scale_factor)
        v6 = v5.softmax(dim=(- 1))
        v7 = self.dropout1(v6)
        v8 = torch.matmul(v7, v3)
        v9 = self.out_linear(v8)
        v10 = self.dropout2(v9)
        return v10



num_heads = 1
dropout = 1
func = Model(num_heads, dropout).to('cuda')

x1 = 1
x2 = 1

test_inputs = [x1, x2]
