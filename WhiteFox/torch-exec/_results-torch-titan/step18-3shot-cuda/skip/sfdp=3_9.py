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

    def __init__(self, dim, num, dropout_p=0, scale_factor=(1 / (dim ** 0.5))):
        super().__init__()
        self.query = torch.nn.Linear(dim, num, bias=True)
        self.key = torch.nn.Linear(dim, num, bias=True)
        self.value = torch.nn.Linear(dim, num, bias=True)
        self.dropout_p = dropout_p
        self.scale_factor = scale_factor

    def forward(self, query, key, value):
        q = self.query(query)
        k = self.key(key)
        v = self.value(value)
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        scaled_qk = qk.mul(self.scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(v)
        return output



dim = 1
num = 1
func = Model(256, 128, dropout_p=0.1).to('cuda')



query = torch.randn(4, 32, 256)



key = torch.randn(4, 24, 256)



value = torch.randn(4, 24, 128)


test_inputs = [query, key, value]
