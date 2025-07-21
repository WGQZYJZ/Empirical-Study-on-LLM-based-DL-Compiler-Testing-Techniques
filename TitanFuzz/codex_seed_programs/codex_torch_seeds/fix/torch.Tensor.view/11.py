'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.view\ntorch.Tensor.view(_input_tensor, *shape)\n'
import torch
x = torch.randn(4, 4)
print(x)
y = x.view(16)
z = x.view((- 1), 8)
print(y)
print(z)