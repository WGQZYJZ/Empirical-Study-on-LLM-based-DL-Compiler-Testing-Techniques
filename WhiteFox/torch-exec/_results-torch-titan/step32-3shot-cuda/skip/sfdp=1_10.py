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



class Model():

    def forward(self, query, key, value, inv_scale_factor, dropout_p):
        scaled_qk = torch.matmul(query, key.transpose((- 2), (- 1))).div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        return torch.matmul(dropout_qk, value)



func = Model().to('cuda')



query = torch.randn(1, 20, 100)



key = torch.randn(1, 20, 120)



value = torch.randn(1, 20, 120)

inv_scale_factor = 1
dropout_p = 1

test_inputs = [query, key, value, inv_scale_factor, dropout_p]
