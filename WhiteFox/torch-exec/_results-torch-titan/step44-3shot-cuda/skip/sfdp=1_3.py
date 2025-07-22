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
        self.qk = torch.nn.Linear(dim, dim)

    def forward(self, query, key, value, inv_scale_factor, dropout_p):
        qk = self.qk(query)
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output



func = Model().to('cuda')



query = torch.randn(1, 1, 5)



key = torch.randn(1, 6, 5)



value = torch.randn(1, 6, 6)



inv_scale_factor = torch.randn(1)



dropout_p = torch.tensor(0.75)


test_inputs = [query, key, value, inv_scale_factor, dropout_p]
