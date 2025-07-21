'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cummin\ntorch.cummin(input, dim, *, out=None)\n'
import torch
input_data = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(input_data)
output_data = torch.cummin(input_data, dim=0)
print(output_data)
output_data = torch.cummin(input_data, dim=1)
print(output_data)