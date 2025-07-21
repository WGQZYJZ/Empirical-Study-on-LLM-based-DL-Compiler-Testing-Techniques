import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[1, 2, 3, 4], [4, 3, 2, 1]])
input_tensor = torch.tensor([[1, 2, 3, 4], [4, 3, 2, 1]])
output_tensor = torch.Tensor.fliplr(input_tensor)