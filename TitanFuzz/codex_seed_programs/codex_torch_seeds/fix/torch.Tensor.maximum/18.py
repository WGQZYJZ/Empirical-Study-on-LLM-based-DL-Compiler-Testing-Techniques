'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.maximum\ntorch.Tensor.maximum(_input_tensor, other)\n'
import torch
a = torch.Tensor([[1, 2, 3], [4, 5, 6]])
b = torch.Tensor([[10, 20, 30], [40, 50, 60]])
print(torch.Tensor.maximum(a, b))