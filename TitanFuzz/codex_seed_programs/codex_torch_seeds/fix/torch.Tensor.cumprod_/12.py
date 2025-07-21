'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cumprod_\ntorch.Tensor.cumprod_(_input_tensor, dim, dtype=None)\n'
import torch
import torch
input_tensor = torch.randint(low=0, high=10, size=(3, 3), dtype=torch.float32)
print('input_tensor:', input_tensor)
result = torch.Tensor.cumprod_(input_tensor, dim=1)
print('result:', result)