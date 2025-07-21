import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([(- 1.0), 1.0, (- 3.0), 5.0])
output_data = torch.nn.functional.relu_(input_data)
input_data = torch.tensor([(- 1.0), 1.0, (- 3.0), 5.0])
output_data = torch.nn.functional.relu(input_data)