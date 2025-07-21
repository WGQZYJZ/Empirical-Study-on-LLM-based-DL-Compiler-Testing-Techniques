'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nelement\ntorch.Tensor.nelement(_input_tensor)\n'
import torch
input_tensor = torch.rand(2, 3)
print(input_tensor)
print(input_tensor.nelement())