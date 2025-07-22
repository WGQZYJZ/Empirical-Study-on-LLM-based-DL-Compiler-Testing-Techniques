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

    def __init__(self, query, key, value, dropout_p, inv_scale_factor):
        super().__init__()
        self.query = torch.nn.Parameter(query)
        self.key = torch.nn.Parameter(key)
        self.value = torch.nn.Parameter(value)
        self.dropout_p = dropout_p
        self.inv_scale_factor = inv_scale_factor

    def forward(self, scaled_query):
        qk = torch.matmul(scaled_query, self.key.transpose((- 2), (- 1)))
        softmax_qk = qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(self.value)
        return output




query = torch.randn(1, 13, 768)


key = torch.randn(1, 13, 768)


value = torch.randn(1, 13, 768)


dropout_p = 0.2


inv_scale_factor = (1 / sqrt(768))


func = Model(query, key, value, dropout_p, inv_scale_factor).to('cuda')



query = torch.randn(1, 13, 768)



key = torch.randn(1, 13, 768)



scaled_query = torch.randn(1, 6, 768)


test_inputs = [query, key, scaled_query]
