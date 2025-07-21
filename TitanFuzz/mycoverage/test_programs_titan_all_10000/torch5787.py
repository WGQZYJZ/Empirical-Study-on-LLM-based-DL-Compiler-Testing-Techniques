import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=torch.float32)
output_tensor = torch.Tensor.equal(input_tensor, torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=torch.float32))