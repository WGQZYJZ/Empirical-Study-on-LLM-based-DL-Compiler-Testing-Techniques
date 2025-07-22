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

    def __init__(self, num_heads, d_model, d_qk, d_v, device):
        super().__init__()
        self.num_heads = num_heads
        self.d_model = d_model
        self.d_qk = d_qk
        self.d_v = d_v
        self.scale = (d_qk ** (- 0.5))
        self.w_q = torch.nn.Linear(d_model, (d_qk * num_heads), bias=False)
        self.w_k = torch.nn.Linear(d_model, (d_qk * num_heads), bias=False)
        self.w_v = torch.nn.Linear(d_model, (d_v * num_heads), bias=False)
        self.dropout = torch.nn.Dropout(0.1)
        self.dropout_p = 0.1
        self.w_q.to(device)
        self.w_k.to(device)
        self.w_v.to(device)

    def forward(self, query, key, value):
        q = self.w_q(query)
        k = self.w_k(key)
        v = self.w_v(value)
        q = q.reshape(q.shape[0], q.shape[1], self.num_heads, self.d_qk).transpose((- 3), (- 2))
        k = k.reshape(k.shape[0], k.shape[1], self.num_heads, self.d_qk).transpose((- 3), (- 2))
        v = v.reshape(v.shape[0], v.shape[1], self.num_heads, self.d_v).transpose((- 3), (- 2))
        qk = torch.matmul(q, k.transpose((- 1), (- 2)))
        scaled_qk = (qk * self.scale)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = self.dropout(softmax_qk)
        output = torch.matmul(dropout_qk, v).transpose((- 3), (- 2))
        output = output.reshape(output.shape[0], output.shape[1], (output.shape[2] * output.shape[3]))
        return output




num_heads = 8


d_model = 128


d_qk = 64


d_v = 64


device = torch.device('xpu')

func = Model(num_heads, d_model, d_qk, d_v, device).to('cuda')



d_model = 128


seq_len = 4


num_batches = 1


query = torch.randn(num_batches, seq_len, d_model)



d_model = 128


seq_len = 4


num_batches = 1


key = torch.randn(num_batches, seq_len, d_model)



d_model = 128


seq_len = 4


num_batches = 1


value = torch.randn(num_batches, seq_len, d_model)


test_inputs = [query, key, value]
