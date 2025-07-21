'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sigmoid\ntorch.sigmoid(input, *, out=None)\n'
import torch
from torch.autograd import Variable
input_data = Variable(torch.randn(1, 1, 3, 3))
print(input_data)
output_data = torch.sigmoid(input_data)
print(output_data)