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

    def __init__(self, d_model, k_dim, v_dim, n_head, dropout_p=0.1, inv_scale_factor=1.0):
        super().__init__()
        self.d_model = d_model
        self.k = torch.nn.Linear(k_dim, d_model)
        self.v = torch.nn.Linear(v_dim, d_model)
        self.n_head = n_head
        self.scale_factor = (d_model ** (- 0.5))
        self.dropout = torch.nn.dropout(p=dropout_p)
        self.output_linear = torch.nn.Linear(d_model, d_model)

    def forward(self, query, key, value):
        d_k = key.size()[(- 1)]
        q = query.view((- 1), self.n_head, self.d_model)
        k = key.view((- 1), self.n_head, d_k).transpose(1, 2)
        v = value.view((- 1), self.n_head, d_k).transpose(1, 2)
        q = self.k(q).view((- 1), self.n_head, self.d_model, 1)
        k = self.k(k).view((- 1), self.n_head, 1, self.d_model)
        v = self.v(v).view((- 1), self.n_head, 1, self.d_model)
        qk = (q * k)
        scaled_qk = (qk * self.scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = self.dropout(softmax_qk)
        output = dropout_qk.matmul(v).transpose(1, 2)
        output = output.reshape((- 1), (self.n_head * self.d_model))
        output = self.output_linear(output)
        return output



d_model = 1
k_dim = 1
v_dim = 1
n_head = 1

func = Model(d_model, k_dim, v_dim, n_head).to('cuda')



x1 = torch.randn(1280, 512, 96)



x2 = torch.randn(1280, 512, 64)



x3 = torch.randn(1280, 512, 64)


test_inputs = [x1, x2, x3]
