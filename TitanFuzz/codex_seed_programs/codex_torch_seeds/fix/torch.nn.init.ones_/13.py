'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.ones_\ntorch.nn.init.ones_(tensor)\n'
import torch
input_data = torch.randn(2, 3)
print('Input data: \n', input_data)
torch.nn.init.ones_(input_data)
print('After initialization: \n', input_data)