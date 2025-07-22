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
        pass

    def forward(self, input_tensors):
        x = torch.cat(input_tensors, dim=1)
        x = x[:, 0:9223372036854775807]
        x = x[:, 0:size]
        x = torch.cat([x, x], dim=1)
        return x



func = Model().to('cuda')



x1 = torch.randn(1, 320)



x2 = torch.randn(1, 384)



x3 = torch.randn(1, 320)


test_inputs = [x1, x2, x3]
