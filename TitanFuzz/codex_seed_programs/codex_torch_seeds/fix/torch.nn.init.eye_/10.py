'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.eye_\ntorch.nn.init.eye_(tensor)\n'
import torch
input_data = torch.Tensor(2, 3).normal_(0, 1)
print('Input data: {}'.format(input_data))
torch.nn.init.eye_(input_data)
print('Output data: {}'.format(input_data))