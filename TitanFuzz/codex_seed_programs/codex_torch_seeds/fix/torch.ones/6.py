'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ones\ntorch.ones(*size, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
input_data = torch.ones(5, 3)
print(input_data)
input_data_2 = torch.rand(5, 3)
print(input_data_2)
print(input_data.size())
input_data_3 = torch.rand(4, 4)
print(input_data_3)
print(input_data_3.size())