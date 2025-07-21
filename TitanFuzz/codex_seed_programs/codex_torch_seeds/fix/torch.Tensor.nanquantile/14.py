'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nanquantile\ntorch.Tensor.nanquantile(_input_tensor, q, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3, 4], [4, 3, 2, 1], [5, 6, 7, 8]])
result_tensor = torch.Tensor.nanquantile(input_tensor, 0.5)
print('The result is:', result_tensor)