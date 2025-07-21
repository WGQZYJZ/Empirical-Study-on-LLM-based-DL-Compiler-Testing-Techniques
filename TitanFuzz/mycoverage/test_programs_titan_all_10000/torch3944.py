import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
output_tensor = torch.reshape(input_tensor, (2, 6))
output_tensor = torch.reshape(input_tensor, (1, 12))
output_tensor = torch.reshape(input_tensor, (12, 1))