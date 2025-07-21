'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nanmedian\ntorch.Tensor.nanmedian(_input_tensor, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(input_tensor)
print(torch.Tensor.nanmedian(input_tensor, dim=0, keepdim=False))
print(torch.Tensor.nanmedian(input_tensor, dim=1, keepdim=False))
print(torch.Tensor.nanmedian(input_tensor, dim=None, keepdim=False))