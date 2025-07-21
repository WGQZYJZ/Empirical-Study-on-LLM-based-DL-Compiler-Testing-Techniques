'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.full\ntorch.full(size, fill_value, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
import torch
input_data = torch.Tensor([[1, 2], [3, 4]])
output = torch.full(size=input_data.size(), fill_value=10)
print('Output: ', output)