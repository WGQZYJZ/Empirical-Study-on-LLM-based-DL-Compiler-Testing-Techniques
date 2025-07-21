import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[0.1, 0.2, (- 0.3)], [0.4, 0.5, (- 0.6)]], dtype=torch.float32)
output_tensor = torch.Tensor.hardshrink(input_tensor, lambd=0.5)