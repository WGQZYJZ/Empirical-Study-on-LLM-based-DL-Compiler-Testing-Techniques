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

    def __init__(self, hidden_dim, num_heads, dropout_p=0):
        super().__init__()
        self.num_heads = num_heads
        self.dropout_p = dropout_p
        self.query = torch.nn.Linear(hidden_dim, hidden_dim)
        self.key = torch.nn.Linear(hidden_dim, hidden_dim)
        self.value = torch.nn.Linear(hidden_dim, hidden_dim)

    def forward(self, x1):
        q = self.query(x1)
        k = self.key(x1)
        v = self.value(x1)
        q = q.reshape((q.shape[:2] + (self.num_heads, (q.shape[(- 1)] // self.num_heads))))
        k = k.reshape((q.shape[:2] + (self.num_heads, (k.shape[(- 1)] // self.num_heads))))
        v = v.reshape((q.shape[:2] + (self.num_heads, (v.shape[(- 1)] // self.num_heads))))
        scaled_qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        scaled_qk = scaled_qk.div((- math.sqrt(k.shape[(- 1)])))
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(v)
        output = output.reshape(x1.shape[0], x1.shape[1], k.shape[(- 1)])
        return output




hidden_dim = 1024


num_heads = 8

func = Model(hidden_dim, num_heads, dropout_p).to('cuda')



hidden_dim = 1024


x1 = torch.randn(8, 1, hidden_dim)


test_inputs = [x1]
