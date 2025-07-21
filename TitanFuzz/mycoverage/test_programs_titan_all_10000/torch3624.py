import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([1, 1, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5])
output_tensor = torch.Tensor.unique_consecutive(input_tensor)