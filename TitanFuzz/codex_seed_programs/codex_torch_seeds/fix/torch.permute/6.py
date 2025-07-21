'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.permute\ntorch.permute(input, dims)\n'
import torch
import torch
input_data = torch.randn(2, 3, 4)
output_data = torch.permute(input_data, (1, 0, 2))
print('input_data:')
print(input_data)
print('output_data:')
print(output_data)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.squeeze\ntorch.squeeze(input, dim=None, out=None) → Tensor\n'
import torch
import torch
input_data = torch.randn(2, 3, 4)
output_data = torch.squeeze(input_data)
print('input_data:')
print(input_data)
print('output_data:')