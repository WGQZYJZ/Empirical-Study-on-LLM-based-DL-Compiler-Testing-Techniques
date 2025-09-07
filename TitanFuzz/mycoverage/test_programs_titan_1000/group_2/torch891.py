import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(5, 5)
output_data = torch.special.exp2(input_data)
output_data = torch.rand(5, 5)
torch.special.exp2(input_data, out=output_data)