import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 3)
output_data = torch.nn.functional.alpha_dropout(input_data, p=0.5, training=False, inplace=False)