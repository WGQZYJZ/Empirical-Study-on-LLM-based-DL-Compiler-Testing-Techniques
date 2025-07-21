'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nanquantile\ntorch.Tensor.nanquantile(_input_tensor, q, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.randn(4, 4)
input_tensor[(1, 1)] = torch.tensor(float('nan'))
input_tensor[(2, 2)] = torch.tensor(float('nan'))
output_tensor = torch.Tensor.nanquantile(input_tensor, 0.5)
print('Input tensor:\n', input_tensor)
print('Output tensor:\n', output_tensor)