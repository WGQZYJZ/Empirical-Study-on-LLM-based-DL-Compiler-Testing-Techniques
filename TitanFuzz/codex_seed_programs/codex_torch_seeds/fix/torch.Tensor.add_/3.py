'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.add_\ntorch.Tensor.add_(_input_tensor, other, *, alpha=1)\n'
import torch
x = torch.tensor([1, 2, 3, 4, 5])
y = torch.tensor([1, 1, 1, 1, 1])
x.add_(y)
print(x)