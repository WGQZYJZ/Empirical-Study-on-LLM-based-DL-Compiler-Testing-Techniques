'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.clamp\ntorch.Tensor.clamp(_input_tensor, min=None, max=None)\n'
import torch
input_tensor = torch.randn(3, 3)
min_value = (- 0.5)
max_value = 0.5
clamped_tensor = input_tensor.clamp(min=min_value, max=max_value)
print('input_tensor:')
print(input_tensor)
print('clamped tensor:')
print(clamped_tensor)