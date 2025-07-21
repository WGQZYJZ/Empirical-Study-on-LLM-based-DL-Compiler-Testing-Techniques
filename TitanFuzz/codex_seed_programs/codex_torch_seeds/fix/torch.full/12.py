'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.full\ntorch.full(size, fill_value, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
input_data = torch.tensor([[1, 2, 3], [4, 5, 6]])
output_data = torch.full(input_data.shape, fill_value=0)
print(output_data)