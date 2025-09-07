import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([[2.0, 3.0]])
output_data = torch.tan(input_data)
output_data = torch.tan_(input_data)