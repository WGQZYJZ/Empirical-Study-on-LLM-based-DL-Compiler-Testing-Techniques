"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.norm\ntorch.Tensor.norm(_input_tensor, p='fro', dim=None, keepdim=False, dtype=None)\n"
import torch
input_tensor = torch.randn(3, 3)
output_tensor = input_tensor.norm(p=2, dim=0, keepdim=False, dtype=None)
print('Input tensor: ', input_tensor)
print('Output tensor: ', output_tensor)