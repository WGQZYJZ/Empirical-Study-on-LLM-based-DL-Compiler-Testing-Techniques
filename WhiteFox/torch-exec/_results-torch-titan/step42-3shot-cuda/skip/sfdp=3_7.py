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
        self.scale_factor = (1.0 / math.sqrt(hidden_size))
        self.dropout_p = 1.0
        self.query = torch.rand(query_len, heads, hidden_size, hidden_size)
        self.key = torch.rand(query_len, heads, hidden_size, hidden_size)
        self.value = torch.rand(query_len, heads, hidden_size, hidden_size)

    def forward(self, x1):
        qk = torch.matmul(self.query, self.key.transpose((- 2), (- 1)))
        scaled_qk = qk.mul(self.scale_factor)
        softmax_qk = scaled_qk.softmax(dim=2)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(self.value)
        return output




func = Model().to('cuda')



hidden_size = 512


query_len = 128


x1 = torch.randn(query_len, hidden_size)


test_inputs = [x1]
