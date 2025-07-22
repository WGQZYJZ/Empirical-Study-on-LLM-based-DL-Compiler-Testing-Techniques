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

    def __init__(self, query, key, value, attn_mask=None, dropout_p=0.1):
        super().__init__()
        self.dropout_p = dropout_p
        self.scale_factor = (query.shape[(- 1)] ** (- 0.5))
        self.query = torch.nn.Parameter(query)
        self.key = torch.nn.Parameter(key)
        self.value = torch.nn.Parameter(value)

    def drop_rows_or_cols(self, t):
        r = (t * torch.rand((t.shape[0], 1))).floor()
        return (t * (r / r.sum(keepdim=True)))

    def forward(self, x):
        dropout_qk = torch.nn.functional.dropout((torch.matmul(self.query, self.key.transpose((- 2), (- 1))) / self.scale_factor), self.dropout_p)
        return torch.matmul(self.drop_rows_or_cols(dropout_qk), self.value)



query = 1
key = 1
value = 1

func = Model(query, key, value).to('cuda')



d_model = 64


tgt_len = 10


batch_size = 3


x1 = torch.randn(batch_size, tgt_len, d_model)



d_model = 64


tgt_len = 10


batch_size = 3


x2 = torch.randn(batch_size, tgt_len, d_model)



d_model = 64


tgt_len = 10


batch_size = 3


x3 = torch.randn(batch_size, tgt_len, d_model)


test_inputs = [x1, x2, x3]
