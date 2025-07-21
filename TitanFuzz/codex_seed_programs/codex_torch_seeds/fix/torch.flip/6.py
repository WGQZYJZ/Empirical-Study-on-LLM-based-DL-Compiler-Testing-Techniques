'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.flip\ntorch.flip(input, dims)\n'
import torch
input_data = torch.randn(2, 3)
print('input data: ', input_data)
result = torch.flip(input_data, [1])
print('flip result: ', result)