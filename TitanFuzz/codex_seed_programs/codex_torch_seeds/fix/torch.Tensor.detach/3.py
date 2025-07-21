'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.detach\ntorch.Tensor.detach(_input_tensor, )\n'
import torch
input_tensor = torch.randn(2, 3, 4)
detach_input_tensor = input_tensor.detach()
print(input_tensor)
print(detach_input_tensor)