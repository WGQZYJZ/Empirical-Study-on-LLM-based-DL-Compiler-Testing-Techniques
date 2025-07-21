'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.is_floating_point\ntorch.is_floating_point(input)\n'
import torch
input_data = torch.randn(5)
print(input_data)
print(torch.is_floating_point(input_data))
print(torch.is_floating_point(input_data.type(torch.int32)))