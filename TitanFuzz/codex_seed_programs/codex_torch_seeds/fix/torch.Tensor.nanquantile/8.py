'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nanquantile\ntorch.Tensor.nanquantile(_input_tensor, q, dim=None, keepdim=False)\n'
import torch
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('Input Tensor: ', input_tensor)
output_tensor = torch.Tensor.nanquantile(input_tensor, 0.5, dim=None, keepdim=False)
print('Output Tensor: ', output_tensor)