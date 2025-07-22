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

    def __init__(self, query, key, value, inv_scale_factor):
        self.query = query
        self.key = key
        self.value = value
        self.inv_scale_factor = inv_scale_factor

    def forward(self, query, key, value, inv_scale_factor, dropout_p):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output




query = torch.randn(1, 3, 64, 64)


key = torch.randn(1, 3, 64, 64)


value = torch.randn(1, 3, 64, 64)


inv_scale_factor = 8

func = Model(query, key, value, inv_scale_factor).to('cuda')



query = torch.randn(1, 3, 64, 64)



key = torch.randn(1, 3, 64, 64)



value = torch.randn(1, 3, 64, 64)

inv_scale_factor = 1
dropout_p = 1

test_inputs = [query, key, value, inv_scale_factor, dropout_p]
