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



class Model(nn.Module):

    def __init__(self, emb_size, heads=8, dropout=0.0, bias=True):
        super().__init__()
        self.emb_size = emb_size
        self.heads = heads
        self.head_dim = (emb_size // heads)
        self.scale_factor = (self.head_dim ** (- 0.5))
        self.dropout_p = dropout
        self.qkv = nn.Linear(emb_size, (3 * emb_size), bias=bias)
        dpr = [x.item() for x in torch.linspace(0, dropout, emb_size)]
        self.dropout = nn.Dropout2d(drop=(((dpr[0] + dpr[(- 1)]) / 2) if (len(dpr) > 1) else dpr[0]))
        self.proj = nn.Linear((3 * emb_size), emb_size)

    def forward(self, query, key, value, mask=None):
        qkv = self.qkv(query)
        qkv_shape = qkv.shape
        batch_size = qkv_shape[0]
        seq_length = qkv_shape[1]
        qkv_length = qkv_shape[2]
        qkv = qkv.view(batch_size, seq_length, self.heads, (3 * self.head_dim)).permute(0, 2, 1, 3)
        query = qkv[:, :, :, :self.head_dim]
        key = qkv[:, :, :, self.head_dim:(2 * self.head_dim)]
        value = qkv[:, :, :, (2 * self.head_dim):]
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = qk.div(self.scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(value)
        output = output.permute(0, 2, 1, 3)
        output = output.reshape(batch_size, seq_length, (- 1))
        output = self.dropout(output)
        output = self.proj(output)
        return output



emb_size = 1

func = Model(emb_size).to('cuda')



x1 = torch.randn(1, 20, 256)



x2 = torch.randn(1, 15, 256)



x3 = torch.randn(1, 15, 256)

query = 1

test_inputs = [x1, x2, x3, query]
