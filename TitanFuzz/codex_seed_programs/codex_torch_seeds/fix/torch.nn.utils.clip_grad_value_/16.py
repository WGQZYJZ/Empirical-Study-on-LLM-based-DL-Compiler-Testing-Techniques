'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.clip_grad_value_\ntorch.nn.utils.clip_grad_value_(parameters, clip_value)\n'
import torch
import torch.nn as nn
from torch.autograd import Variable
input_data = Variable(torch.randn(5, 5))
input_data = input_data.requires_grad_()
clip_value = 2
torch.nn.utils.clip_grad_value_(input_data, clip_value)
print(input_data.grad)