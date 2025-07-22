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

    def forward(self, x1, x2):
        qk = torch.matmul(self.query, self.key.transpose((- 2), (- 1)))
        scaled_qk = qk.div(self.inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(self.value)
        return output



func = Model(query=torch.randn(16, 64, 16), key=torch.randn(16, 64, 20), value=torch.randn(16, 64, 20), inv_scale_factor=math.sqrt(64), dropout_p=0.5).to('cuda')



x1 = torch.randn(2, 8, 64, 16)



x2 = torch.randn(2, 8, 64, 20)


test_inputs = [x1, x2]
