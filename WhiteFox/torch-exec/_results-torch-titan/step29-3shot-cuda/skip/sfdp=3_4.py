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
        self.scale_factor = (1 / (sqrt(query.shape[(- 1)]) * sqrt(key.shape[(- 1)])))

    def forward(self, __query__, __key__, __value__):
        qk = torch.matmul(__query__, __key__.transpose((- 2), (- 1)))
        scaled_qk = qk.mul(self.scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(__value__)
        return output



func = Model().to('cuda')



__query__ = torch.randn(1, 16, 8)



__key__ = torch.randn(1, 16, 8)



__value__ = torch.randn(1, 128, 8)


test_inputs = [__query__, __key__, __value__]
