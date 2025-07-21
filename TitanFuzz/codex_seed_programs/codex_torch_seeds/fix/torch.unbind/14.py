'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.unbind\ntorch.unbind(input, dim=0)\n'
import torch
input_data = torch.rand(2, 3, 4)
print(torch.unbind(input_data, dim=0))