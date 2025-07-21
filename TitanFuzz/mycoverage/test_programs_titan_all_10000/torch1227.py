import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([[1, 2], [3, 4]], dtype=torch.float)
output_data = torch.exp2(input_data)