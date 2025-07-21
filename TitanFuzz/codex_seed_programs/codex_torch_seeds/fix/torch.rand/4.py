'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.rand\ntorch.rand(*size, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
input_data = torch.rand(2, 3)
print(input_data)
print(input_data[0])
print(input_data[1])
print(input_data[0][0])
print(input_data[0][1])
print(input_data[0][2])
print(input_data[1][0])
print(input_data[1][1])
print(input_data[1][2])