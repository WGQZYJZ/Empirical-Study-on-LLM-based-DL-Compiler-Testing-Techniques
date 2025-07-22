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



class ModelTanh(torch.nn.Module):

    def __init__(self):
        pass

    def forward(self, x):
        v1 = x.permute(0, 2, 3, 1)
        v1 = torch.tanh(v1)
        v2 = v1.permute(0, 3, 1, 2)
        return v2




func = ModelTanh().to('cuda')



x = torch.randn(1, 224, 224, 3)


test_inputs = [x]
