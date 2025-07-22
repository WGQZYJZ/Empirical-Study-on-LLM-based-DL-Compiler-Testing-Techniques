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
        self.scale_factor = np.power(d_k, 0.5)

    def forward(self, query, key, value, dropout_p):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = qk.mul(self.scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output



func = Model().to('cuda')



d_k = 1024


query = torch.randn(1024, 1, d_k)



d_k = 1024


key = torch.randn(1024, 40, d_k)



d_k = 1024


value = torch.randn(1024, 40, d_k)

dropout_p = 1

test_inputs = [query, key, value, dropout_p]
