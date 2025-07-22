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



class model(torch.nn.Module):

    def __init__(self, input_tensor):
        super().__init__()
        self.input_tensor = torch.rand_like(input_tensor)

    def forward(self, input_tensor):
        out = self.input_tensor
        return out



input_tensor = 1

func = model(input_tensor).to('cuda')



x1 = torch.randn(1, 2, 2)


test_inputs = [x1]
