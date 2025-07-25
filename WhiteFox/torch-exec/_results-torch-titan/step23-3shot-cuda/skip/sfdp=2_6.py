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

    def __init__(self, config):
        super().__init__()
        self.dim = config.dim
        self.num_heads = config.num_heads
        self.hidden_dim = config.hidden_dim
        self.qk_lin = torch.nn.Linear(self.dim, (self.num_heads * self.hidden_dim), bias=True)
        self.v_lin = torch.nn.Linear(self.dim, (self.num_heads * self.hidden_dim), bias=True)
        self.dropout_lin = torch.nn.Linear((self.num_heads * self.hidden_dim), (self.num_heads * self.hidden_dim), bias=True)
        self.output_lin = torch.nn.Linear((self.num_heads * self.hidden_dim), self.dim, bias=True)

    def forward(self, x1, x2):
        qk = torch.matmul(x1, x2.transpose((- 2), (- 1)))
        scaled_qk = qk.div(10.0)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.3, training=True)
        output = torch.matmul(dropout_qk, x3)
        return output




config = Config()

func = Model(config).to('cuda')



x1 = torch.randn(5, 4, 10)



x2 = torch.randn(5, 2, 10)


test_inputs = [x1, x2]
