import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 3)
index = torch.tensor([0, 2])
source = torch.tensor([0.0, (- 1.0)])
output_tensor = torch.Tensor.put_(input_tensor, index, source, accumulate=False)