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
        self.dropout_p = p

    def forward(self, q1, k1, v1, inv_scale_factor):
        qk = torch.matmul(q1, k1.transpose(-2, -1))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(v1)
        return output


func = Model().to('cpu')


q1 = torch.randn(8, 64, 256)

k1 = torch.randn(8, 256, 416)

v1 = torch.randn(8, 416, 256)
inv_scale_factor = 1

test_inputs = [q1, k1, v1, inv_scale_factor]
