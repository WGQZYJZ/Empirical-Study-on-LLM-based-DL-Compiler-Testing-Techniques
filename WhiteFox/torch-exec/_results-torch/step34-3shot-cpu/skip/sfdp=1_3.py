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

    def __init__(self, hidden_size=64):
        super().__init__()
        self.head_dim = hidden_size // 4
        self.scale_factor = math.sqrt(self.head_dim)
        self.dropout = torch.nn.Dropout(dropout_p)

    def forward(self, query, key, value, dropout_p):
        qk = query.matmul(key.transpose(-2, -1))
        inv_scale_factor = torch.tensor(1.0 / self.scale_factor, device=qk.device)
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = torch.nn.functional.softmax(scaled_qk, dim=-1)
        dropout_qk = self.dropout(softmax_qk)
        output = dropout_qk.matmul(value)
        return output


func = Model(hidden_size=64).to('cpu')

query = 1
key = 1
value = 1
dropout_p = 1

test_inputs = [query, key, value, dropout_p]
