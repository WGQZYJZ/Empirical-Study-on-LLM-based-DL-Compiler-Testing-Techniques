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

    def dot_product(self, query, key, scale_factor, dropout_p, dropout_train):
        if dropout_train:
            qk = torch.matmul(query, key.transpose(-2, -1))
        else:
            qk = torch.matmul(query, key.transpose(-2, -1).contiguous().dropout(p=dropout_p, train=dropout_train))
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        if dropout_train:
            dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        else:
            dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p, train=dropout_train)
        output = torch.matmul(dropout_qk, value)
        return output

class Attention(torch.nn.Module):

    def __init__(self, dropout_p):
        super().__init__()
        self.scale_factor = torch.sqrt(torch.tensor(size=(1,), dtype=torch.float32, device='cuda:0', requires_grad=False).fill_(dropout_p))
        self.dropout_p = dropout_p

    def forward(self, query, key, value, dropout_train):
        output = self.dot_product(query, key, self.scale_factor, self.dropout_p, dropout_train)
        return output


dropout_p = 1

func = Attention(dropout_p).to('cpu')


query = torch.randn(1, 16, 32)

key = torch.randn(1, 16, 64)

value = torch.randn(1, 16, 64)
dropout_train = 1

test_inputs = [query, key, value, dropout_train]
