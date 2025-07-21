'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_set_to\ntorch.Tensor.is_set_to(_input_tensor, tensor)\n'
import torch
import torch.nn as nn
x = torch.randn(1, 3, 224, 224, requires_grad=True)
y = torch.randn(1, 3, 224, 224, requires_grad=True)
print(x.is_set_to(y))