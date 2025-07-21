import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([[(- 1.0), (- 0.5), 0.0, 0.5, 1.0]])
tanh = torch.nn.Tanh()
output_data = tanh(input_data)