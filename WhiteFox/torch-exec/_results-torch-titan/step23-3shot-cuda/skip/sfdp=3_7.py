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

    def __init__(self, scale_factor, dropout_p):
        super().__init__(scale_factor, dropout_p)
        self.dropout = torch.nn.Dropout(dropout_p)

    def forward(self, q, k, v):
        dk = math.sqrt(q.size()[(- 1)])
        scaled_qk = (torch.matmul(q, k.transpose((- 2), (- 1))) / self.scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = self.dropout(softmax_qk)
        output = torch.matmul(dropout_qk, v)
        return output




scale_factor = 10


dropout_p = 0.2

func = Model(scale_factor, dropout_p).to('cuda')



q = torch.randn(8, 16, 20)



k = torch.randn(8, 16, 20)



v = torch.randn(8, 16, 32)


test_inputs = [q, k, v]
