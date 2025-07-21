'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.lerp_\ntorch.Tensor.lerp_(_input_tensor, end, weight)\n'
import torch
input_tensor = torch.randn(1, 3, 4)
output_tensor = torch.Tensor.lerp_(input_tensor, torch.randn(1, 3, 4), 0.5)
print(output_tensor)