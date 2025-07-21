'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.hypot_\ntorch.Tensor.hypot_(_input_tensor, other)\n'
import torch
_input_tensor = torch.rand(3, 5)
other = torch.rand(3, 5)
output_tensor = torch.Tensor.hypot_(_input_tensor, other)
print(output_tensor)