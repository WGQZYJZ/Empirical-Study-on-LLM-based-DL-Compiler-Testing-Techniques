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
        self.scale_factor = torch.tensor(1.0 / sqrt(q.shape[-1]), device='cuda')

    def forward(self, q, k, v, dropout_p):
        qk = torch.matmul(q, k.transpose(-2, -1))
        scaled_qk = qk.mul(self.scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v)
        return output


func = Model().to('cpu')


q = torch.randn(1, 5, 10, 4)

k = torch.randn(1, 5, 2, 4)

v = torch.randn(1, 5, 2, 6)
dropout_p = 1

test_inputs = [q, k, v, dropout_p]
