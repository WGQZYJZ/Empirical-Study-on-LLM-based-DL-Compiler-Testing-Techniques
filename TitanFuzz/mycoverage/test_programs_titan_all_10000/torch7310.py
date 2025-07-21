import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(4, 4)
eye_data = torch.eye(4, 4)
output = torch.mm(input_data, eye_data)
output = torch.matmul(input_data, eye_data)
output = (input_data @ eye_data)
output = input_data.mm(eye_data)
output = input_data.matmul(eye_data)