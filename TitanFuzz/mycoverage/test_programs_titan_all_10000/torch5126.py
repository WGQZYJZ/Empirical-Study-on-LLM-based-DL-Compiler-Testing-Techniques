import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(5, 3)
other_data = torch.randn(5, 3)
output_data = torch.add(input_data, other_data)
output_data2 = torch.empty(5, 3)
torch.add(input_data, other_data, out=output_data2)
input_data.add_(other_data)
output_data3 = torch.empty(5, 3)
torch.add(input_data, other_data, alpha=0.5, out=output_data3)