'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.flatten\ntorch.Tensor.flatten(_input_tensor, start_dim=0, end_dim=-1)\n'
import torch
input_tensor = torch.rand((3, 5))
flatten_tensor = input_tensor.flatten()
print('input_tensor: ', input_tensor)
print('flatten_tensor: ', flatten_tensor)