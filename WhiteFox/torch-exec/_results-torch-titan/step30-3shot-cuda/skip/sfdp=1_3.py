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

    def __init__(self, hidden_size):
        super().__init__()
        self.w_q = torch.nn.Linear(hidden_size, hidden_size)
        self.w_k = torch.nn.Linear(hidden_size, hidden_size)
        self.w_v = torch.nn.Linear(hidden_size, hidden_size)
        self.w_o = torch.nn.Linear(hidden_size, hidden_size)
        self.dropout = torch.nn.Dropout(p=dropout_p)

    def forward(self, q, k, v, mask):
        q = self.w_q(q)
        k = self.w_k(k)
        v = self.w_v(v)
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        scaled_qk = qk.div(self.scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = self.dropout(softmax_qk)
        output = torch.matmul(dropout_qk, v)
        return output




hidden_size = 10

func = Model(hidden_size).to('cuda')



hidden_size = 10


n = 4


query = torch.randn(n, 1, hidden_size)



hidden_size = 10


n = 4


key = torch.randn(n, 10, hidden_size)


n = 4




mask = torch.tril(torch.ones((n, 1, 10)))

q = 1

test_inputs = [query, key, mask, q]
