'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.permute\ntorch.permute(input, dims)\n'
import torch
import torch
input_data = torch.randn(2, 3, 5)
print('input_data.shape: ', input_data.shape)
output_data = torch.permute(input_data, (1, 0, 2))
print('output_data.shape: ', output_data.shape)