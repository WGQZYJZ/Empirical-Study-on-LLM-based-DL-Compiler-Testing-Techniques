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

    def __init__(self, dim):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(dim, 1, dropout=p)

    def forward(self, x1, x2, x3, mask):
        query = x1
        key = x2
        value = x3
        qk = self.attn.forward_query(query, key)
        dk = self.attn.forward_key(query, key)
        dv = self.attn.forward_value(key)
        dk = (dk * ((float(mask.size(1)) / mask.sum((- 1), keepdim=True)) ** 0.5))
        qk = qk.div(((float(mask.size(0)) / mask.sum((- 2), keepdim=True)) ** 0.5))
        scaled_qk = qk.softmax((- 1))
        dropout_qk = self.attn.dropout_module(scaled_qk)
        output = dropout_qk.matmul(dv.transpose((- 2), (- 1)))
        return output



dim = 1
func = Model(dim).to('cuda')




mask = torch.ones(size=(1, 100), dtype=bool)

x1 = 1
x2 = 1
x3 = 1

test_inputs = [mask, x1, x2, x3]
