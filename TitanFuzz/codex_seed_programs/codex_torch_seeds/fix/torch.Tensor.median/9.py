'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.median\ntorch.Tensor.median(_input_tensor, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(input_tensor.median(dim=0, keepdim=True))
print(input_tensor.median(dim=1, keepdim=True))
print(input_tensor.median(dim=0, keepdim=False))
print(input_tensor.median(dim=1, keepdim=False))