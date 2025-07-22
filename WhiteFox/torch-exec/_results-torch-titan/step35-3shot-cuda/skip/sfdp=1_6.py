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

    def __init__(self, query_size, key_size, value_size, dropout_p, inv_scale_factor):
        super().__init__()
        self.query_projection = torch.nn.Linear(q, k)
        self.key_projection = torch.nn.Linear(k, k)
        self.value_projection = torch.nn.Linear(v, v)
        self.inv_scale_factor = inv_scale_factor
        self.dropout_p = dropout_p

    def forward(self, query, key, value):
        q = self.query_projection.forward(query)
        k = self.key_projection.forward(key)
        v = self.value_projection.forward(value)
        qk = torch.matmul(q, k.t())
        scaled_qk = qk.div(self.inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(v)
        return output




query_size = 100


key_size = 100


value_size = 200


dropout_p = 0.5


inv_scale_factor = torch.sqrt(torch.FloatTensor([key_size]))

func = Model(query_size, key_size, value_size, dropout_p, inv_scale_factor).to('cuda')


key_size = 100




inv_scale_factor = torch.sqrt(torch.FloatTensor([key_size]))



query_size = 100


query = torch.randn(5, query_size)



key_size = 100


key = torch.randn(10, key_size)



value_size = 200


value = torch.randn(10, value_size)


test_inputs = [inv_scale_factor, query, key, value]
