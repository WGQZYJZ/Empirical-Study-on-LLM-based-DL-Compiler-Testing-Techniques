'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.reshape_as\ntorch.Tensor.reshape_as(_input_tensor, other)\n'
import torch
import torch
x = torch.randn(4, 4)
y = torch.randn(4, 4)
torch.Tensor.reshape_as(x, y)
print(x)
print(y)