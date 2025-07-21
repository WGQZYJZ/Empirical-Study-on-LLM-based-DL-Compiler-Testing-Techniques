'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.polygamma_\ntorch.Tensor.polygamma_(_input_tensor, n)\n'
import torch
input_tensor = torch.randint(1, 10, (3, 3), dtype=torch.float)
print('Input tensor:', input_tensor)
output_tensor = input_tensor.polygamma_(2)
print('Output tensor:', output_tensor)