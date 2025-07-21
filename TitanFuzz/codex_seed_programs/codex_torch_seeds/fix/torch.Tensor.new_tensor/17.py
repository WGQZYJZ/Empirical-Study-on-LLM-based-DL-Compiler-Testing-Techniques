'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.new_tensor\ntorch.Tensor.new_tensor(_input_tensor, data, dtype=None, device=None, requires_grad=False)\n'
import torch
input_tensor = torch.ones(3, 3)
output_tensor = torch.Tensor.new_tensor(input_tensor, data=[1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=torch.float32)
print('input_tensor:', input_tensor)
print('output_tensor:', output_tensor)