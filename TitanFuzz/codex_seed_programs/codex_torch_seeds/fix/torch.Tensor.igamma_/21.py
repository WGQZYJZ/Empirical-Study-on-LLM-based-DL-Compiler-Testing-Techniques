'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.igamma_\ntorch.Tensor.igamma_(_input_tensor, other)\n'
import torch
x = torch.rand(1, 10)
y = torch.rand(1, 10)
torch.Tensor.igamma_(x, y)
print(x)