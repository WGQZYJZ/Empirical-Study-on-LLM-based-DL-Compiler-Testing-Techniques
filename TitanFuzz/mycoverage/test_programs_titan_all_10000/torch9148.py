import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
indices = torch.tensor([0, 2])
output_tensor = torch.Tensor.take(input_tensor, indices)