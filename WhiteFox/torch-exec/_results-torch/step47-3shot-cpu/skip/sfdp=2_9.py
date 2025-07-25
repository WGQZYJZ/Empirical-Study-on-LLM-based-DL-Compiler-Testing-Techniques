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

    def __init__(self, attention_head_dim, nb_self_attention_layer, nb_self_attention_head):
        super(Model).init__()
        embedding_dim = 128
        num_head = nb_self_attention_head
        embedding_dim //= num_head
        self.q = torch.nn.Linear(embedding_dim * attention_head_dim, embedding_dim * attention_head_dim)
        self.k = torch.nn.Linear(embedding_dim * attention_head_dim, embedding_dim * attention_head_dim)
        self.v = torch.nn.Linear(embedding_dim * attention_head_dim, embedding_dim * attention_head_dim)

    def forward(self, query, key, value):
        q = self.q(query)
        k = self.k(key)
        v = self.v(value)
        query_dim = 2
        key_dim = 3
        dot_prod = torch.matmul(q, k.transpose(-2, -1))
        inv_scale_factor = (key_dim / query_dim) ** 0.5
        scaled_dot_prod = dot_prod / inv_scale_factor
        softmax_dot_prod = scaled_dot_prod.softmax(dim=-1)
        dropout_dot_prod = nn.functional.dropout(softmax_dot_prod, p=embedding_dropout_p)
        attention_output = torch.matmul(dropout_dot_prod, v)
        return attention_output


attention_head_dim = 1
nb_self_attention_layer = 1
nb_self_attention_head = 1
func = Model(32, 3, 4).to('cpu')


query = torch.rand([128, 2, 32])

key = torch.rand([128, 3, 32])

value = torch.rand([128, 3, 32])

test_inputs = [query, key, value]
