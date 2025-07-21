'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nanquantile\ntorch.Tensor.nanquantile(_input_tensor, q, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.Tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print('Input Tensor: ', input_tensor)
print('torch.Tensor.nanquantile(input_tensor, 0.5): ', torch.Tensor.nanquantile(input_tensor, 0.5))
print('torch.Tensor.nanquantile(input_tensor, 0.5, dim=0): ', torch.Tensor.nanquantile(input_tensor, 0.5, dim=0))
print('torch.Tensor.nanquantile(input_tensor, 0.5, dim=0, keepdim=True): ', torch.Tensor.nanquantile(input_tensor, 0.5, dim=0, keepdim=True))