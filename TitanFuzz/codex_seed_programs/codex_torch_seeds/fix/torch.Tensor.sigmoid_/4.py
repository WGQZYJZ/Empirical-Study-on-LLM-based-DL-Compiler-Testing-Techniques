'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sigmoid_\ntorch.Tensor.sigmoid_(_input_tensor)\n'
import torch
input_tensor = torch.randn(2, 3)
print('input_tensor:', input_tensor)
torch.Tensor.sigmoid_(input_tensor)
print('input_tensor:', input_tensor)