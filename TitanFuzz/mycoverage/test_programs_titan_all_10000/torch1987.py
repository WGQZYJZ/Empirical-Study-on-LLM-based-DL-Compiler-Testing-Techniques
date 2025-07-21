import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
flipped_tensor = torch.Tensor.flip(input_tensor, [0])