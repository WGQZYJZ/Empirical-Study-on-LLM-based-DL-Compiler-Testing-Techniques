import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([[1, (- 1), 0], [2, (- 2), 0], [3, (- 3), 0]])
output_data = torch.positive(input_data)