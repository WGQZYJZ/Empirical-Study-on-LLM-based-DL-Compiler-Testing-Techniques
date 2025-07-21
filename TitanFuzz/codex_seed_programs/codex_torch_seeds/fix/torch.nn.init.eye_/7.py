'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.eye_\ntorch.nn.init.eye_(tensor)\n'
import torch
input_tensor = torch.randn(3, 3)
print('Input Tensor: \n', input_tensor)
torch.nn.init.eye_(input_tensor)
print('Resultant Tensor: \n', input_tensor)