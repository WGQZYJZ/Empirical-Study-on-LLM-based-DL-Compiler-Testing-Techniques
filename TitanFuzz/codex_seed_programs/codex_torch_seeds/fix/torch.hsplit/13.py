'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.hsplit\ntorch.hsplit(input, indices_or_sections)\n'
import torch
input_data = torch.arange(1, 17).view(4, 4)
print('Input data: ', input_data)
torch.hsplit(input_data, 2)