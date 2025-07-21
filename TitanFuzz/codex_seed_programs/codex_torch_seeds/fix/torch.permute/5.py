'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.permute\ntorch.permute(input, dims)\n'
import torch
input_data = torch.arange(0, 24).view(2, 3, 4)
print('input_data: ', input_data)
output = torch.permute(input_data, (1, 0, 2))
print('output: ', output)