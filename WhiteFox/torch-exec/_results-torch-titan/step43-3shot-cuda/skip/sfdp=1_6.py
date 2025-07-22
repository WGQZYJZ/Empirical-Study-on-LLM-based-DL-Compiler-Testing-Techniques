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

    def __init__(self, query, key, value, dropout_p, inv_scale_factor):
        super().__init__()
        self.mat = torch.nn.functional.linear
        self.qk = self.mat(query, key.transpose((- 2), (- 1)))
        self.scaled_qk = self.qk.div(inv_scale_factor)
        self.softmax_qk = torch.nn.functional.softmax(self.scaled_qk, dim=(- 1))
        self.dropout_qk = torch.nn.functional.dropout(self.softmax_qk, p=dropout_p)
        self.output = self.dropout_qk.matmul(value)

    def forward(self, query, key, value, dropout_p, inv_scale_factor):
        output = self.mat(query, key.transpose((- 2), (- 1)))
        output = output.div(inv_scale_factor)
        output = torch.nn.functional.softmax(output, dim=(- 1))
        output = torch.nn.functional.dropout(output, p=dropout_p)
        output = self.mat(query, value)
        return output



query = 1
key = 1
value = 1
dropout_p = 1
inv_scale_factor = 1
func = Model(query, key, value, dropout_p, inv_scale_factor).to('cuda')



x1 = x2 = x3 = torch.randn(1, 1152, 4, 64)

query = 1
key = 1
value = 1
dropout_p = 1

test_inputs = [x1, query, key, value, dropout_p]
