'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.reshape_as\ntorch.Tensor.reshape_as(_input_tensor, other)\n'
import torch
x = torch.ones(4, 4)
y = torch.zeros(5, 5)
z = x.reshape_as(y)
print(z)