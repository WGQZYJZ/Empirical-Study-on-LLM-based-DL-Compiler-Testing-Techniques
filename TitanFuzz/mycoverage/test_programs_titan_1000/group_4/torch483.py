import torch
from torch import nn
from torch.autograd import Variable
input_data = [[1, 2, 3], [4, 5, 6]]
input_tensor = torch.Tensor(input_data)
output_tensor = torch.Tensor.new_tensor(input_tensor, input_data)