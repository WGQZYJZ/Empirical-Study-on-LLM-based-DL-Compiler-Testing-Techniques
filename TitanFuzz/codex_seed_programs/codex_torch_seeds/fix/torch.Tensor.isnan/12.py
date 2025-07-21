'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.isnan\ntorch.Tensor.isnan(_input_tensor)\n'
import torch
input_tensor = torch.randn(2, 3)
print(input_tensor)
print(input_tensor.isnan())