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
        self.proj = Linear(query_size, key_size)

    def forward(self, query, key, scale_factor, dropout_p):
        q = self.proj(query)
        k = self.proj(key)
        qk = torch.matmul(q, k.transpose(-2, -1))
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output


func = Model().to('cpu')


scale_factor = torch.rand(1, 16)
query = 1
key = 1
dropout_p = 1

test_inputs = [scale_factor, query, key, dropout_p]
