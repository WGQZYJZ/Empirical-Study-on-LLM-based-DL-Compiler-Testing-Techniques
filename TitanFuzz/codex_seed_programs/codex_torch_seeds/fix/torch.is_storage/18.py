'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.is_storage\ntorch.is_storage(obj)\n'
import torch
input_data = torch.rand(2, 3, 4)
print(input_data)
print(torch.is_storage(input_data))