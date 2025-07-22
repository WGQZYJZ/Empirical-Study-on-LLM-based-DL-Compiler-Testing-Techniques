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

    def __init__(self, m, n, o, p):
        super().__init__()
        self.q_ = torch.nn.Linear(m, n)
        self.k_ = torch.nn.Linear(p, o)

    def forward(self, query, key, value, inv_scale_factor, dropout_p):
        q = self.q_(query).unsqueeze(1)
        k = self.k_(key).transpose((- 2), (- 1))
        qk = torch.matmul(q, k)
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output




m = Model(m=4, n=3, o=2, p=4)

n = 1
o = 1
p = 1

func = Model(m, n, o, p).to('cuda')



query = torch.randn(4, 3)



key = torch.randn(5, 4)



value = torch.randn(5, 2)



inv_scale_factor = torch.rand(1)



dropout_p = torch.rand(1)


test_inputs = [query, key, value, inv_scale_factor, dropout_p]
