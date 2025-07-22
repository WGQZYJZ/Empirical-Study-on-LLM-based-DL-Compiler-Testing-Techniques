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

    def __init__(self, dim_model, num_heads, dropout_p):
        self.dim_model = dim_model
        self.num_heads = num_heads
        self.dropout_p = dropout_p

    def forward(self, query, key, value, inv_scale_factor):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(value)
        return output



dim_model = 1
num_heads = 1
dropout_p = 1

func = Model(dim_model, num_heads, dropout_p).to('cuda')



query = torch.randn(1, 16, 512, 8)



key = torch.randn(1, 16, 896, 8)



value = torch.randn(1, 16, 896, 8)

inv_scale_factor = 1

test_inputs = [query, key, value, inv_scale_factor]
