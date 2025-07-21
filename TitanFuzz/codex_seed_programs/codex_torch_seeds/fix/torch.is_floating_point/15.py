'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.is_floating_point\ntorch.is_floating_point(input)\n'
import torch
input_data = torch.tensor([1.2, 2.3, 3.4])
print(torch.is_floating_point(input_data))
input_data = torch.tensor([1, 2, 3])
print(torch.is_floating_point(input_data))