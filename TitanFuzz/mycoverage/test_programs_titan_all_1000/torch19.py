import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.arange(1, 25, dtype=torch.float).view(1, 1, 4, 6)
unfold = torch.nn.Unfold(kernel_size=(2, 2))
output = unfold(input_data)
fold = torch.nn.Fold(output_size=(4, 6), kernel_size=(2, 2))
output = fold(output)