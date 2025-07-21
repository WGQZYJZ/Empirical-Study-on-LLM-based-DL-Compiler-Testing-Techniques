import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(1, 1, 6, 6)
unfold = torch.nn.Unfold(kernel_size=(2, 2), stride=(2, 2))
output_data = unfold(input_data)