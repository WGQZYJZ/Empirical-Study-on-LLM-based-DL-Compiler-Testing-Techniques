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

    def __init__(self, d_model, num_heads, dropout_p):
        super().__init__()
        self.qk_w = torch.nn.Linear(d_model, d_model)
        self.qk_b = torch.nn.Parameter(torch.zeros(d_model), requires_grad=True)
        self.v_w = torch.nn.Linear(d_model, d_model)
        self.v_b = torch.nn.Parameter(torch.zeros(d_model), requires_grad=True)
        self.dropout_p = dropout_p
        self.softmax = torch.nn.Softmax(dim=(- 1))

    @property
    def num_heads(self):
        return (len(self.qk_w) // 3)

    def forward(self, query, value):
        qk = torch.matmul((self.qk_w(query) + self.qk_b), self.v_w(value).transpose((- 2), (- 1)))
        inv_scale_factor = math.sqrt((query.shape[(- 1)] / self.num_heads))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = self.softmax(scaled_qk)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = (dropout_qk @ self.v_w(value))
        return output



d_model = 1
num_heads = 1
dropout_p = 1
func = Model(16, 2, 0.1).to('cuda')



query = torch.randn(16, 16, 4)



value = torch.randn(16, 16, 4)


test_inputs = [query, value]

# CRASH
'''
crash:
object of type 'Linear' has no len()
'''