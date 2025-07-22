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
        self.dropout = torch.nn.Dropout(dropout_p)
        self.softmax = torch.nn.Softmax(dim=-1)
        self.matmul = torch.matmul

    def forward(self, q, k, v, scale_factor):
        qk = self.matmul(q, k.transpose(-2, -1))
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = self.softmax(scaled_qk)
        dropout_qk = self.dropout(softmax_qk)
        output = self.matmul(dropout_qk, v)
        return output


func = Model().to('cpu')



q = torch.tensor([[1, 2, 5]], dtype=torch.float)


k = torch.tensor([[3, 10, 7], [1, 1, 3], [0, -2, 4]], dtype=torch.float)


v = torch.tensor([[1, 8, -1], [0, 1, -3], [1, 1, -1]], dtype=torch.float)
scale_factor = 1

test_inputs = [q, k, v, scale_factor]
