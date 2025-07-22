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

    def __init__(self, q, k, v, q_dim, k_dim, v_dim, dropout):
        super().__init__()
        self.w = q.new_randn(v_dim, q_dim)
        self.q = q
        self.k = k
        self.v = v
        self.dropout = dropout

    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        inv_scale_factor = torch.tensor((1.0 / float(value.shape[(- 1)]))).to(query)
        v3 = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = torch.matmul(dropout_qk, value)
        return output




q = torch.randn(5, 8, 3)


k = torch.randn(5, 6, 3)


v = torch.randn(5, 6, 16)

q_dim = 1
k_dim = 1
v_dim = 1
dropout = 1
func = Model(q, k, v, 8, 6, 16, 0.5).to('cuda')



q = torch.randn(5, 8, 3)



k = torch.randn(5, 6, 3)



v = torch.randn(5, 6, 16)



query = torch.randn(1, 4, 8)



key = torch.randn(1, 2, 6)



value = torch.randn(1, 2, 16)


test_inputs = [q, k, v, query, key, value]
