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

    def __init__(self, query, key, value, scale_factor=(1.0 / (10 ** 2)), dropout_p=0.2):
        super().__init__()
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        self.register_buffer('dropout_qk', dropout_qk)
        self.register_buffer('value', value)

    def forward(self, x):
        scaled_qk = torch.matmul(x, self.dropout_qk.transpose((- 2), (- 1)))
        output = scaled_qk.matmul(self.value)
        return output




query = torch.randn(1, 1, 16, 8)


key = torch.randn(1, 1, 8, 8)


value = torch.randn(1, 1, 16, 8)


func = Model(query, key, value).to('cuda')



b = torch.tensor([1.2, 2.3, 3.4], requires_grad=True)


b = torch.tensor([1.2, 2.3, 3.4], requires_grad=True)


c = b.clone()



x = torch.randn(1, 1, 16, 8)



query = torch.randn(1, 1, 16, 8)



key = torch.randn(1, 1, 8, 8)


test_inputs = [b, c, x, query, key]
