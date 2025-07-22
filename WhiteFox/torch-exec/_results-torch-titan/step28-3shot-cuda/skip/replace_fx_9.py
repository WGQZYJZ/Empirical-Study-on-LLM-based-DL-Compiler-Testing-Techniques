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



class ModelRandom(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.m = torch.nn.utils.rnn.RandomLayer(1, 1, batch_first=False)

    def forward(self, input: Any) -> Any:
        x = self.m(input)
        x = x.permute(2, 1, 0).contiguous()
        x = x.view((- 1), 2)
        return x




func = ModelRandom().to('cuda')

input = 1

test_inputs = [input]
