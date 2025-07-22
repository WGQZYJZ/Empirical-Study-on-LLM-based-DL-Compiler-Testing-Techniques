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

    def __init__(self, d_model, num_heads, scale_factor=(1 / (d_model // num_heads))):
        super().__init__()
        self.num_heads = num_heads
        self.qkv_proj = torch.nn.Linear(d_model, (3 * d_model))
        self.scale_factor = scale_factor
        self.dropout = torch.nn.Dropout(0.3)

    def forward(self, x1):
        (q, k, v) = torch.chunk(self.qkv_proj(x1), 3, dim=(- 1))
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        scaled_qk = qk.mul(self.scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = self.dropout(softmax_qk)
        output = dropout_qk.matmul(v)
        return output



d_model = 1
num_heads = 1
func = Model(288, 4).to('cuda')



x1 = torch.randn(1, 49, 288)


test_inputs = [x1]
