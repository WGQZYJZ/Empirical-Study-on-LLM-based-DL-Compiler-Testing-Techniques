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
        self.query = query.squeeze(1)
        self.key = key.squeeze(1)
        self.value = value.squeeze(1)
        self.scale_factor = scale_factor
        self.dropout_p = dropout_p

    def forward(self, x1):
        qk = torch.matmul(self.query, self.key.transpose(-2, -1))
        scaled_qk = qk.div(self.scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(self.value)
        return output


query = 1
key = 1
value = 1
scale_factor = 1
dropout_p = 1
func = Model(query, key, value, scale_factor, dropout_p).to('cpu')


x1 = torch.randn(1, 1, 32)

test_inputs = [x1]
