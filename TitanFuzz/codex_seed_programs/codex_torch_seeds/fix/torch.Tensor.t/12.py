'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.t\ntorch.Tensor.t(_input_tensor)\n'
import torch
x = torch.randn(2, 3)
print(x)
print(x.t())
x = torch.randn(2, 3, 4)
print(x)
print(x.t())
x = torch.randn(2, 3, 4, 5)
print(x)
print(x.t())
x = torch.randn(2, 3, 4, 5, 6)
print(x)
print(x.t())