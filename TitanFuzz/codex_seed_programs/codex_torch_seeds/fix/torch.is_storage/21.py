'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.is_storage\ntorch.is_storage(obj)\n'
import torch
input_data = torch.randn(2, 3)
print('Input data: ', input_data)
print('torch.is_storage(input_data): ', torch.is_storage(input_data))