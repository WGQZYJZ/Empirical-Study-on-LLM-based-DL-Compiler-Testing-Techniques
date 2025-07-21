'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.full\ntorch.full(size, fill_value, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
input_data = torch.Tensor(2, 3)
print(input_data)
input_data = torch.full((2, 3), 7)
print(input_data)
input_data = torch.full((2, 3), 7, dtype=torch.int)
print(input_data)
input_data = torch.full((2, 3), 7, dtype=torch.int, device=torch.device('cuda'))
print(input_data)