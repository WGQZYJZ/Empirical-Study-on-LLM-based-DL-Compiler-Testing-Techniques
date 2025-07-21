'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.full\ntorch.full(size, fill_value, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
size_tensor = torch.Size([2, 3])
fill_value = 0.1
output_tensor = torch.full(size_tensor, fill_value)
print('The output tensor is: ', output_tensor)