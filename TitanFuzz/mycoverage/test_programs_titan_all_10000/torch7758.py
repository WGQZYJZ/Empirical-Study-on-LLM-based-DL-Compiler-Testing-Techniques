import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]])
output_tensor = torch.Tensor.sigmoid(input_tensor)