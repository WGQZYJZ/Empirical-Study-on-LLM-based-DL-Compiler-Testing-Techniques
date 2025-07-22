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

    def __init__(self, hidden_size, num_heads, dropout_p=0.1):
        super().__init__()
        self.num_heads = num_heads
        self.query = torch.nn.Linear(hidden_size, hidden_size)
        self.key = torch.nn.Linear(hidden_size, hidden_size)
        self.value = torch.nn.Linear(hidden_size, hidden_size)
        self.matmul1 = torch.matmul
        self.matmul2 = torch.matmul
        weight = torch.empty(num_heads, (hidden_size // num_heads), hidden_size, dtype=torch.float32)
        nn.init.xavier_uniform_(weight)
        bias = torch.empty(num_heads, (hidden_size // num_heads), dtype=torch.float32)
        nn.init.normal_(bias)
        self.matmul1.weight = nn.Parameter(weight)
        self.matmul1.bias = nn.Parameter(bias)
        self.matmul2.weight = nn.Parameter(torch.transpose(weight, 1, 2))
        self.matmul2.bias = nn.Parameter(0)
        self.softmax = torch.nn.Softmax(dim=3)
        self.dropout = torch.nn.Dropout(p=dropout_p)

    def forward(self, query_tensor, key_tensor, value_tensor, query_mask, input_mask):
        q = self.query(query_tensor).view(query_tensor.shape[0], query_tensor.shape[1], (- 1)).transpose(1, 2)
        k = self.key(key_tensor).view(key_tensor.shape[0], key_tensor.shape[1], (- 1))
        v = self.value(key_tensor).view(key_tensor.shape[0], value_tensor.shape[1], (- 1))
        qk = self.matmul1(q, torch.transpose(k, 1, 2)).div(math.sqrt(q.shape[(- 1)]))
        scaled_qk = qk.masked_fill(mask=query_mask, value=float('-inf')).softmax(dim=(- 1))
        dropout_qk = self.dropout(scaled_qk)
        output = self.matmul2(dropout_qk, v.transpose(1, 2))
        return (output, query_mask, input_mask)




hidden_size = 64


num_heads = 8


func = Model(hidden_size, num_heads).to('cuda')



hidden_size = 64


query_tensor = torch.randn(1, hidden_size)



hidden_size = 64


key_tensor = torch.randn(2, hidden_size)



hidden_size = 64


value_tensor = torch.randn(2, hidden_size)



query_mask = torch.zeros((1, 8, 2))



input_mask = torch.zeros((2, 8, 2))


test_inputs = [query_tensor, key_tensor, value_tensor, query_mask, input_mask]
