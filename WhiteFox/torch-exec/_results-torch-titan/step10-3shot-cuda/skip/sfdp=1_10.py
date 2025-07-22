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

    def __init__(self, q, k, v):
        super().__init__()
        self.m = nn.Linear(q, k)

    def forward(self, query, key, value):
        qk = self.m(query).matmul(torch.transpose(key, (- 2), (- 1)))
        inv_scale_factor = math.sqrt((key.shape[(- 1)] - 1))
        scaled_qk = (qk / inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.2)
        output = dropout_qk.matmul(value)
        return output



q = 1
k = 1
v = 1
func = Model(in_q, in_k, in_v).to('cuda')



in_q = 32


query = torch.randn(16, 8, in_q)



in_k = 64


key = torch.randn(16, 8, in_k)



in_v = 64


value = torch.randn(16, 8, in_v)


test_inputs = [query, key, value]
