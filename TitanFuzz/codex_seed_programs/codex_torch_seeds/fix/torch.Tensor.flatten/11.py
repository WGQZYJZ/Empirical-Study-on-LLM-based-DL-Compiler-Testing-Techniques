'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.flatten\ntorch.Tensor.flatten(_input_tensor, start_dim=0, end_dim=-1)\n'
import torch
input_tensor = torch.randn(4, 3, 2)
print(input_tensor)
output_tensor = input_tensor.flatten(start_dim=0, end_dim=(- 1))
print(output_tensor)