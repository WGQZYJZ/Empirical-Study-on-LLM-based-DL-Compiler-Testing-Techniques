'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.std\ntorch.Tensor.std(_input_tensor, dim, unbiased=True, keepdim=False)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
print(input_tensor)
print(input_tensor.std(dim=0, unbiased=False))
print(input_tensor.std(dim=1, unbiased=False))
print(input_tensor.std(dim=0, unbiased=False, keepdim=True))
print(input_tensor.std(dim=1, unbiased=False, keepdim=True))