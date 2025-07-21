import torch
from torch import nn
from torch.autograd import Variable
input_tensor_1 = torch.randn(2, 3)
input_tensor_2 = torch.randn(2, 3)
output_tensor = torch.column_stack((input_tensor_1, input_tensor_2))