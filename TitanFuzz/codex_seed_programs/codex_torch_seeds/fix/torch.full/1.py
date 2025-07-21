'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.full\ntorch.full(size, fill_value, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
input_data = torch.Tensor([[1, 2, 3], [4, 5, 6]])
print(input_data)
print(input_data.shape)
output_data = torch.full(size=input_data.shape, fill_value=7)
print(output_data)
print(output_data.shape)