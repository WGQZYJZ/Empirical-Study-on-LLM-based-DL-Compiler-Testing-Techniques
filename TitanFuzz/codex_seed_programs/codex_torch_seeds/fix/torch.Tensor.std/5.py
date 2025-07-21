'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.std\ntorch.Tensor.std(_input_tensor, dim, unbiased=True, keepdim=False)\n'
import torch
import numpy as np
import torch
input_tensor_1 = torch.Tensor([[1, 2, 3], [4, 5, 6]])
input_tensor_2 = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(input_tensor_1.std(dim=0))
print(input_tensor_1.std(dim=1))
print(input_tensor_2.std(dim=0))
print(input_tensor_2.std(dim=1))