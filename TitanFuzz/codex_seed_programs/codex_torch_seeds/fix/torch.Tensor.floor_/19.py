'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.floor_\ntorch.Tensor.floor_(_input_tensor)\n'
import torch
input_tensor = torch.randn(2, 3)
print('The input tensor: ', input_tensor)
torch.Tensor.floor_(input_tensor)
print('The floor_ tensor: ', input_tensor)