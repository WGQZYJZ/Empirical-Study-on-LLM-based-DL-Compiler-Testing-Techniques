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
    qk = ((Q3 @ K3.transpose((- 2), (- 1))) / math.sqrt(Q3.size((- 1))))

    def __init__(self):
        super().__init__()

    def forward(self, Q4, K, V6, mask):
        qk = ((Q4 @ K.transpose((- 2), (- 1))) / math.sqrt(Q4.size((- 1))))
        qk = (qk + mask)
        attn_weight = torch.softmax(qk, dim=(- 1))
        output = (attn_weight @ V6)
        return output




func = Model().to('cuda')



Q = torch.randn(1, 64, 56, 56)



K = torch.randn(1, 64, 56, 56)



V = torch.randn(1, 64, 56, 56)



mask = (torch.rand(1, 56, 56) > 0.7).fill_((- 1000000000.0))


test_inputs = [Q, K, V, mask]
