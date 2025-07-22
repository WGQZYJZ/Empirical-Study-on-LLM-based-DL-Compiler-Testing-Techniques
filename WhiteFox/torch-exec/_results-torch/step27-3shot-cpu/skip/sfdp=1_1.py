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

    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(5, 8, bias=False)
        self.key = torch.nn.Linear(5, 8, bias=False)
        self.value = torch.nn.Linear(5, 8, bias=False)
        self.inv_scale_factor = torch.nn.Parameter(torch.finfo(torch.float32).tiny)

    def forward(self, query, key, value, dropout_p):
        q = self.query(query)
        k = self.key(key)
        v = self.value(value)
        qk = torch.matmul(q, k.transpose(-2, -1))
        scaled_qk = qk.div(self.inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v)
        return output


func = Model().to('cpu')


query = torch.randn(1, 3, 5)

key = torch.randn(1, 6, 5)

value = torch.randn(1, 6, 5)
dropout_p = 1

test_inputs = [query, key, value, dropout_p]
