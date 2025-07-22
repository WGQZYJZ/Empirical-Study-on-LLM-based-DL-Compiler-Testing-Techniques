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

    def __init__(self, *, q, k, v, n_head, scale_factor, dropout_p):
        super().__init__()
        self.scale_factor = scale_factor
        self.dropout = torch.nn.Dropout(self.dropout_p)
        self.softmax = torch.nn.Softmax(dim=(- 1))

    def forward(self, *, q, k, v):
        qk = q.matmul(k.transpose((- 2), (- 1)))
        scaled_qk = qk.div(self.scale_factor)
        softmax_qk = self.softmax(scaled_qk)
        dropout_qk = self.dropout(softmax_qk)
        output = dropout_qk.matmul(v)
        return output



func = Model().to('cuda')



q = torch.randn(1, 4, 16)



k = torch.randn(2, 4, 16)



v = torch.randn(1, 4, 128)


test_inputs = [q, k, v]
