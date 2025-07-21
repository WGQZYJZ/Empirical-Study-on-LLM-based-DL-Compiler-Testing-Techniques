'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.median\ntorch.Tensor.median(_input_tensor, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
input_tensor_median = torch.Tensor.median(input_tensor)
print(input_tensor_median)
input_tensor_median_dim = torch.Tensor.median(input_tensor, dim=0)
print(input_tensor_median_dim)
input_tensor_median_dim_keepdim = torch.Tensor.median(input_tensor, dim=0, keepdim=True)
print(input_tensor_median_dim_keepdim)