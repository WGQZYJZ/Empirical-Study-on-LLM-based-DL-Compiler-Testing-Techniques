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

    def __init__(self, input_dim, output_dim, dropout_p):
        super().__init__()
        self.key_linear = Linear(input_dim, output_dim)
        self.value_linear = Linear(input_dim, output_dim)
        self.scale_factor = (sqrt(input_dim) * pow(dropout_p, input_dim))
        self.dropout_p = dropout_p

    def forward(self, x1, x2):
        k1 = self.key_linear(x1).transpose((- 1), (- 2))
        v1 = self.value_linear(x1).transpose((- 1), (- 2))
        qk = torch.matmul(x2, k1)
        scaled_qk = (qk * self.scale_factor)
        softmax_qk = F.softmax(scaled_qk, dim=(- 1))
        dropout_qk = F.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(v1)
        return output



input_dim = 1
output_dim = 1
dropout_p = 1

func = Model(input_dim, output_dim, dropout_p).to('cuda')



x1 = torch.randn(1, 256)



x2 = torch.randn(1, 256)


test_inputs = [x1, x2]
