'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sort\ntorch.Tensor.sort(_input_tensor, dim=-1, descending=False)\n'
import torch
input_tensor = torch.Tensor([[1, 3, 5], [2, 4, 6]])
output_tensor = torch.Tensor.sort(input_tensor, dim=(- 1), descending=False)
print('The sorted tensor is: ', output_tensor)