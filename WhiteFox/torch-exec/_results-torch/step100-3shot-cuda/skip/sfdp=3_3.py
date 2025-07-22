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

    def __init__(self, dropout_p):
        super().__init__()
        self.scale_factor = math.sqrt(len(self.query_shape))
        self.query = torch.nn.Parameter(torch.randn(*self.query_shape))
        self.key = torch.nn.Parameter(torch.randn(*self.key_shape))
        self.value = torch.nn.Parameter(torch.randn(*self.value_shape))
        self.dropout_p = dropout_p

    def forward(self, x):
        xq = torch.matmul(x, self.query)
        xk = torch.matmul(x, self.key.transpose(-2, -1))
        scaled_qk = xk.mul(self.scale_factor)
        soft_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(soft_qk, p=self.dropout_p)
        output = torch.matmul(dropout_qk, self.value)
        return output


dropout_p = 1
func = Model(0.1).to('cuda')


x = torch.randn(1, 50, 36)

test_inputs = [x]
