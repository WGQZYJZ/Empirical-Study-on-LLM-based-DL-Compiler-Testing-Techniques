import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([[3.0, 3.3], [4.0, 3.9], [2.0, 3.7], [3.2, 3.2], [3.0, 3.0], [0.0, 3.0], [1.0, 3.0], [3.0, 3.0], [3.0, 3.0], [3.0, 3.0]])
output_data = torch.empty(10, 2)
output_data = torch.zeros(10, 2)
output_data = torch.rand(10, 2)
output_data = torch.randn(10, 2)