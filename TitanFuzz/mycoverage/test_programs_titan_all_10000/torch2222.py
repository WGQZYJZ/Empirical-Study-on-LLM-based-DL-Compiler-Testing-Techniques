import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([[1.1, 2.3, 4.5], [6.7, 8.9, 10.1]], dtype=torch.float32)
output_data = torch.floor(input_data)