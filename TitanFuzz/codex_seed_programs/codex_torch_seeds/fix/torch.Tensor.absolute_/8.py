'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.absolute_\ntorch.Tensor.absolute_(_input_tensor)\n'
import torch
input_tensor = torch.randn(5, 3)
print(input_tensor)
torch.Tensor.absolute_(input_tensor)
print(input_tensor)