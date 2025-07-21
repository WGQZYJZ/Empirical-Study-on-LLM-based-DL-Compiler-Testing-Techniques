import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(1, 3, 3)
index = torch.tensor([[0, 1, 2], [1, 2, 0]])
source = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
output_tensor = torch.Tensor.put_(input_tensor, index, source, accumulate=False)