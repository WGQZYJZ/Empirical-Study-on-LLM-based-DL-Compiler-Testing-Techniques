import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.ones(5, 3)
input_data = torch.rand(5, 3)
input_data = torch.zeros(5, 3, dtype=torch.long)
input_data = torch.tensor([5.5, 3])
input_data = input_data.new_ones(5, 3, dtype=torch.double)
input_data = torch.randn_like(input_data, dtype=torch.float)
x = torch.rand(5, 3)
y = torch.rand(5, 3)