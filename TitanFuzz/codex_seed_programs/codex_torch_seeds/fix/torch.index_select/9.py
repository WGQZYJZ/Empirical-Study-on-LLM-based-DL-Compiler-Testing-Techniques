'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.index_select\ntorch.index_select(input, dim, index, *, out=None)\n'
import torch
import torch
input_data = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float)
print('input_data:', input_data)
output_data = torch.index_select(input_data, 0, torch.tensor([0, 2]))
print('output_data:', output_data)