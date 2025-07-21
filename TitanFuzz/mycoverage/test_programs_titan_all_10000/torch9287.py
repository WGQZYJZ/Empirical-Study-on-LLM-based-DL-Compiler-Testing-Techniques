import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3)
output_tensor = torch.Tensor.gather(input_tensor, 1, torch.tensor([[0, 1, 2], [1, 2, 0]]))