'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.map_\ntorch.Tensor.map_(_input_tensor, tensor, callable\n'
import torch
_input_tensor = torch.randn(2, 3)
output_tensor = torch.Tensor.map_(_input_tensor, torch.abs)
print(output_tensor)