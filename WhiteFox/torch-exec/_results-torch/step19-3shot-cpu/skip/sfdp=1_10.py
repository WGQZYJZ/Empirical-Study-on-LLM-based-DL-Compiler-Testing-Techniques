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

    def __init__(self, query, key, value, inv_scale_factor, dropout_p):
        super().__init__()
        self.matmul1 = torch.nn.MatMul()
        self.matmul2 = torch.nn.MatMul()
        self.div = torch.nn.Div()
        self.softmax = torch.nn.Softmax(dim=-1)
        self.dropout = torch.nn.Dropout(dropout_p)
        self.matmul3 = torch.nn.MatMul()

    def forward(self, query, key, value):
        matmul1_out = self.matmul1(query, key.t())
        matmul2_out = self.matmul2(matmul1_out, inv_scale_factor, dim=1)
        softmax_qk = self.softmax(matmul2_out)
        dropout_qk = self.dropout(softmax_qk)
        matmul_out = self.matmul3(dropout_qk, value)
        return matmul_out


query = torch.randn(1, 8, 64)
key = torch.randn(1, 8, 64)
value = torch.randn(1, 128, 64)
inv_scale_factor = torch.tensor([float(1.0 / (8 * 64 ** 0.5))])
dropout_p = torch.tensor([0.0])
func = Model(query, key, value, inv_scale_factor, dropout_p).to('cpu')


query = torch.randn(1, 8, 64)

key = torch.randn(1, 8, 64)

value = torch.randn(1, 128, 64)


inv_scale_factor = torch.tensor([float(1.0 / (8 * 64 ** 0.5))])

dropout_p = torch.tensor([0.0])

test_inputs = [query, key, value, inv_scale_factor, dropout_p]
