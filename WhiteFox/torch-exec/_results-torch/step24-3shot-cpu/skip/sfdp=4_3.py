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
        self.model = torch.nn.Transformer([torch.nn.TransformerEncoderLayer(d_model=256, nhead=8)], num_encoder_layers=6)

    def forward(self, x1):
        v1 = self.model(x1, src_key_padding_mask)[0]
        return v1



func = Model().to('cpu')


mask_token = torch.cuda.LongTensor([255])

test_inputs = [mask_token]
