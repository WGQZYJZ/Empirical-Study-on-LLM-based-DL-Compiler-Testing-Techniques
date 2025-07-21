'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.upsample_nearest\ntorch.nn.functional.upsample_nearest(input, size=None, scale_factor=None)\n'
import torch
from torch.autograd import Variable
input_data = torch.rand(1, 1, 4, 4)
input = Variable(input_data, requires_grad=True)
output = torch.nn.functional.upsample_nearest(input, size=None, scale_factor=2)
print('input data:')
print(input_data)
print('output data:')
print(output.data)
output.backward(torch.ones(output.size()))
print('gradients:')
print(input.grad)