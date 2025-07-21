'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.amin\ntorch.Tensor.amin(_input_tensor, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.randn(3, 4)
print(input_tensor)
print(input_tensor.amin(0))
print(input_tensor.amin(1))
print(input_tensor.amin(1, keepdim=True))
print(input_tensor.amin(dim=1, keepdim=True))