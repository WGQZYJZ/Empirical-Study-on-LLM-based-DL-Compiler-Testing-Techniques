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



class scaled_dot_product_attention(torch.nn.Module):

    def __init__(self, dropout=0.1):
        super().__init__()
        self.scale_factor = torch.nn.Parameter(0.1, requires_grad=True)
        self.dropout = torch.nn.Dropout(dropout)

    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = qk.mul(self.scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = self.dropout(softmax_qk)
        output = dropout_qk.matmul(value)
        return output



func = scaled_dot_product_attention(dropout=0.1).to('cuda')



query = torch.randn(1, 24, 512)



key = torch.randn(1, 8, 512)



value = torch.randn(1, 8, 512)


test_inputs = [query, key, value]
