import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[[[(- 1.0), (- 0.5), 0.0, 0.5, 1.0]]]])
output_tensor = torch.nn.functional.relu6(input_tensor)
input_tensor = torch.tensor([[[[(- 1.0), (- 0.5), 0.0, 0.5, 1.0]]]])