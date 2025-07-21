'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.floor\ntorch.Tensor.floor(_input_tensor)\n'
import torch
input_tensor = torch.randn(3, 3)
floor_output = torch.Tensor.floor(input_tensor)
print(floor_output)