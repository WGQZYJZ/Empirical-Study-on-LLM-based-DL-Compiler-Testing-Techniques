'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sum\ntorch.sum(input, dim, keepdim=False, *, dtype=None)\n'
import torch
import torch
input_data = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
output_data = torch.sum(input_data, dim=0)
print(output_data)
output_data = torch.sum(input_data, dim=1)
print(output_data)
output_data = torch.sum(input_data, dim=1, keepdim=True)
print(output_data)
output_data = torch.sum(input_data, dim=1, keepdim=True, dtype=torch.float32)
print(output_data)