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
        self.matmul1 = torch.nn.Linear(config.d, config.d)
        self.matmul2 = torch.nn.Linear(config.d, config.d)
        self.matmul3 = torch.nn.Linear(config.d, config.d)
        self.matmul4 = torch.nn.Linear(config.d, config.d)
        self.matmul5 = torch.nn.Linear(config.d, config.d)

    def forward(self, x, y):
        q = self.matmul1(x)
        k = self.matmul2(y)
        v = self.matmul3(y)
        qy = self.matmul4(x)
        inv_scale_factor = self.matmul5(x)
        qk = torch.matmul(qy, k.transpose((- 2), (- 1)))
        qk = qk.div(inv_scale_factor)
        softmax_qk = qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=config.attention_dropout_prob)
        output = dropout_qk.matmul(v)
        return output



config = 1
func = Model(conf).to('cuda')

x = 1
y = 1

test_inputs = [x, y]
