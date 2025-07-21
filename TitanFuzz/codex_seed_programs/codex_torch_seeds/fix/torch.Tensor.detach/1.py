'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.detach\ntorch.Tensor.detach(_input_tensor, )\n'
import torch
input_tensor = torch.randn(2, 3)
print(input_tensor)
detached_tensor = input_tensor.detach()
print(detached_tensor)
input_tensor.fill_(1)
print(input_tensor)
print(detached_tensor)
input_tensor.add_(1)
print(input_tensor)
print(detached_tensor)