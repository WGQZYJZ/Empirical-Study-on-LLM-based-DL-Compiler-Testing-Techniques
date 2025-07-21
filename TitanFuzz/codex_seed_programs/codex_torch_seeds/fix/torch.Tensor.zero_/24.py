'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.zero_\ntorch.Tensor.zero_(_input_tensor)\n'
import torch
input_tensor = torch.rand(2, 3)
print('Input tensor: {}'.format(input_tensor))
torch.Tensor.zero_(input_tensor)
print('Output tensor: {}'.format(input_tensor))