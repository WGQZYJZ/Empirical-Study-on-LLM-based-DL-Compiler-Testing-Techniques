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
        self.embedding = torch.nn.Embedding(1, 1, padding_idx=1)

    def forward(self, x1):
        v1 = x1.int()
        v2 = self.embedding(v1)
        v3 = v2.squeeze(1)
        return v3



func = Model().to('cpu')


x1 = torch.tensor([0])

test_inputs = [x1]
