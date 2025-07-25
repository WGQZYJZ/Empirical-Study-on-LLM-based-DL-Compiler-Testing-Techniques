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

    def __init__(self, query, key, value, dropout_p):
        super().__init__()
        self.qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        self.inv_scale_factor = (key.shape[(- 1)] ** (- 1))
        self.softmax_qk = self.qk.div(self.inv_scale_factor).softmax(dim=(- 1)).dropout(dropout_p)
        self.value = value

    def forward(self):
        v1 = self.softmax_qk
        v2 = torch.matmul(v1, self.value)
        return v2




query = torch.randn(1, 8, 16, 16)


key = torch.randn(1, 4, 16, 16)


value = torch.randn(1, 4, 16, 16)


dropout_p = 0.0


func = Model(query, key, value, dropout_p).to('cuda')



query = torch.randn(1, 8, 16, 16)



key = torch.randn(1, 4, 16, 16)


test_inputs = [query, key]
