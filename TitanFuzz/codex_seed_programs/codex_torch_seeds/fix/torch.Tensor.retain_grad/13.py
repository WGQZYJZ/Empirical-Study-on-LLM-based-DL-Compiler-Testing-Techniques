'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.retain_grad\ntorch.Tensor.retain_grad(_input_tensor)\n'
import torch
x = torch.ones(2, 2, requires_grad=True)
print(x)
x.retain_grad()
print(x)