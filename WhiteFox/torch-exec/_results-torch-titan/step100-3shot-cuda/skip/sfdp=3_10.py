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

    def __init__(self, query, key, value, scale_factor, dropout_p):
        super().__init__()
        num_heads = query.shape[0]
        emb_dim = query.shape[1]
        self.query = query
        self.key = key
        self.value = value
        self.dropout_p = dropout_p
        self.scale_factor = scale_factor
        self.softmax = torch.nn.Softmax(dim=(- 1))
        self.dropout = torch.nn.Dropout(self.dropout_p)
        self.fc = torch.nn.Linear((num_heads * emb_dim), 1, bias=False)

    def forward(self):
        qk = torch.matmul(self.query, self.key.transpose((- 2), (- 1)))
        scaled_qk = qk.mul(self.scale_factor)
        softmax_qk = self.dropout(self.softmax(scaled_qk))
        dropout_qk = self.dropout(softmax_qk.matmul(self.value))
        return dropout_qk.matmul(self.fc(x.contiguous().view()))




query = torch.empty((2 * dim), dim)


key = torch.empty((2 * dim), emb_dim)


value = torch.empty((2 * dim), emb_dim)


scale_factor = torch.empty((2 * dim), 1)


dropout_p = torch.empty(1).uniform_()

func = Model(query, key, value, scale_factor, dropout_p).to('cuda')



dropout_p = torch.empty(1).uniform_()


test_inputs = [dropout_p]
