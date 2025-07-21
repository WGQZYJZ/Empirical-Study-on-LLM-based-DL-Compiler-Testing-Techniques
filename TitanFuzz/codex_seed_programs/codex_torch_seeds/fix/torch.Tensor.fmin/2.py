'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.fmin\ntorch.Tensor.fmin(_input_tensor, other)\n'
import torch
x = torch.Tensor([1, 2, 3, 4, 5])
y = torch.Tensor([6, 7, 8, 9, 10])
print(torch.__version__)
print(x)
print(y)
print(x.fmin(y))
print(y.fmin(x))