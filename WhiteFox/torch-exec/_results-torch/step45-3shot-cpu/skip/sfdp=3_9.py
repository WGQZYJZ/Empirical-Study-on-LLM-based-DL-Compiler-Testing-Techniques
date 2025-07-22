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
        self.scale_factor = 1 / math.sqrt(embedding_dim)

    def forward(self, qk, val, dropout_p):
        scale_qk = qk * self.scale_factor
        softmax_qk = scale_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(val)
        return output


func = Model().to('cpu')


qk = torch.randn(1, 6, 8, 64)

val = torch.randn(1, 2, 8, 64)
dropout_p = 1

test_inputs = [qk, val, dropout_p]
