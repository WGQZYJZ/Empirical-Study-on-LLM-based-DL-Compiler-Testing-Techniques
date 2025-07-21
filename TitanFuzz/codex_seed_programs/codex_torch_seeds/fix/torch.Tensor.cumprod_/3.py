'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cumprod_\ntorch.Tensor.cumprod_(_input_tensor, dim, dtype=None)\n'
import torch
input_tensor = torch.rand(3, 3)
print(input_tensor)
input_tensor.cumprod_(dim=1, dtype=torch.float32)
print(input_tensor)